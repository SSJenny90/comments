#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages
from comments import __version__

REPO_URL = "https://github.com/SSJenny90/comments"

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='comments',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    author='Sam Jennings',
    author_email='samuel.jennings@pm.me',
    license='MIT',
    description='Commenting app built off django-comments-xtd',
    url=REPO_URL,
    install_requires=[
        "Django>=3,<4",    
        "django-contrib-comments==2.1.0 ",    
        "django-comments-xtd==2.9.5",   
        ],
    keywords='scientific django',
    classifiers=[
        'Development Status :: 1 - Development',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'Natural Language :: English',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)