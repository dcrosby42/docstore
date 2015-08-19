# Borrowed from https://raw.githubusercontent.com/jkbrzt/httpie/master/setup.py

import sys
import codecs

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand



install_requires = [
    'nose>=1.3.7',
    'wheel>=0.24.0'
]



setup(
    name='docstore',
    version=docstore.__version__,
    description=docstore.__doc__.strip(),
    long_description="The docstore long desc",
    url='http://github.com/dcrosby42/docstore/',
    download_url='http://github.com/dcrosby42/docstore/',
    author=docstore.__author__,
    author_email='dcrosby42@gmail.com',
    license=docstore.__licence__,
    packages=find_packages(),
    # entry_points={
    #     'console_scripts': [
    #         'http = httpie.__main__:main',
    #     ],
    # },
    # extras_require=extras_require,
    install_requires=install_requires,
    # tests_require=tests_require,
    # cmdclass={'test': PyTest},
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: System :: Networking',
        'Topic :: Terminals',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
