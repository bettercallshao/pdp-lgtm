from setuptools import find_packages, setup

version = '0.1.2'

with open('README.md') as f:
    long_description = f.read()

setup(
    name='pdp-lgtm',
    version=version,
    description="party of dope pajamas looks good to me.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Shaoqing Tan',
    author_email='tansq7@gmail.com',
    url='https://github.com/timlyrics/pdp-lgtm',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['pdp=pdp_lgtm.pdp:main'],
    },
)
