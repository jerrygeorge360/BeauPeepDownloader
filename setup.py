from setuptools import setup,find_packages
setup(name='BeauPeepDownloader',
version='0.1',
description='A Python package for downloading comic pages from the Beau Peep series',
url='https://github.com/jerrygeorge360/BeauPeepDownloader',
author='jerrygeorge360',
author_email='jbotrex@email.com',
license='MIT',
packages=find_packages(),
    install_requires=[
        'requests', 'beautifulsoup4'
    ],
    zip_safe=False
)