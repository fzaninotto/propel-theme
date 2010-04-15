'''
Setup file for Propel ORM Trac theme.

@author: Benjamin Boerngen-Schmidt <info@boerngen-schmidt.de>
@license: GPLv2 http://www.gnu.org/licenses/gpl-2.0.txt
'''
from setuptools import setup

setup(
    name = 'TracPropelTheme',
    version = '1.0',
    packages = ['propeltheme'],
    package_data = { 'propeltheme': ['templates/*.html', 'htdocs/*.png', 'htdocs/*.css', 'htdocs/img/*.png' ] },

    author = 'Benjamin Boerngen-Schmidt',
    author_email = 'info@boerngen-schmidt.de',
    description = 'Theme for the PropelORM Trac',
    license = 'GPLv2',
    keywords = 'trac plugin theme propel',
    url = 'http://www.propelorm.org',
    classifiers = [
        'Framework :: Trac',
    ],
    
    install_requires = ['Trac', 'TracThemeEngine>=2.0'],

    entry_points = {
        'trac.plugins': [
            'propeltheme.theme = propeltheme.theme',
        ]
    },
)