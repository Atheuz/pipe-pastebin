#!/usr/bin/python
"""Upload file contents to Pastebin."""
from pastebin import VERSION
from distutils.core import setup

setup_kwargs = dict(
    name="pastebin",
    version=VERSION,
    description="Upload file contents to Pastebin",
    author="Lasse Vang Gravesen",
    author_email="gravesenlasse@gmail.com",
    packages=[
        "pastebin/",
    ],
    scripts=[
        "bin/pastebin",
    ],
    long_description=" ".join(__doc__.strip().splitlines()),
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)

setup(**setup_kwargs)
