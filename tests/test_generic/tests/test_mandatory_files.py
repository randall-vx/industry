# Part of Odoo. See LICENSE file for full copyright and licensing details.

from difflib import unified_diff
import io
import os
from pathlib import Path
import re

from odoo import release
from odoo.tests import get_db_name, tagged
from odoo.tools.translate import trans_export

from .industry_case import IndustryCase, get_industry_path


@tagged('post_install', '-at_install')
class FileTest(IndustryCase):

    def test_required_files(self):
        for module in self.installed_modules:
            required_files = {
                'icon': '/static/description/icon.png',
                'image': '/images/main.png',
                'pot file': f'/i18n/{module}.pot',
                'tour': '/static/src/js/my_tour.js',
            }
            for f, path in required_files.items():
                is_file = os.path.isfile(get_industry_path() + module + path)
                self.assertTrue(is_file, "Missing %s at %s" % (f, module + path))

            tx_config = Path(get_industry_path() + '.tx/config').read_text(encoding="utf-8")
            self.assertTrue(re.search(module, tx_config), "Missing module in .tx/config")
            if release.version_info[3] != 'final':
                # skip test if master
                continue
            odoo_version = release.serie
            if odoo_version.split('.')[1] != '0':
                odoo_version = odoo_version.replace('.', '-').split('~')[-1]
            else:
                odoo_version = odoo_version.split('.')[0]
            self.assertTrue(
                re.search(odoo_version + ':r:' + module, tx_config), "Wrong version in .tx/config"
            )

            db_name = get_db_name()
            if not db_name.endswith('imported_with_demo'):
                return
            with io.BytesIO() as buf:
                trans_export(False, [module], buf, 'po', self.env.cr)
                new = buf.getvalue().decode("utf-8")
            old = Path(get_industry_path() + module + '/i18n/' + module + '.pot').read_text(encoding="utf-8")
            diff = list(unified_diff(old, new))
            diff_str = ''.join(d.replace('+','').replace('-','') for d in diff)
            assert len(diff_str.split('\n')) < 6, "You forgot to export the pot file.\n" + diff_str
