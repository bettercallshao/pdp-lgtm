from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pdp-lgtm',
    version=version,
    description="party of dope pajamas looks good to me.",
    author='Shaoqing Tan',
    author_email='tansq7@gmail.com',
    url='https://github.com/timlyrics/pdp-lgtm',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    scripts=['bin/pdp'],
    entry_points = {
        'console_scripts': ['pdp.py=pdp_lgtm.pdp:main'],
    },
)
