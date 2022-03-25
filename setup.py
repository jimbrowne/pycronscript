#!/usr/bin/env python3
#
# Copyright 2014-2022 42Lines, Inc.
# Original Author: Jim Browne
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from pycronscript import __version__

setup_args = {
    "name": "pycronscript",
    "version": __version__,
    "platforms": ["any"],
    "description": "Context manager handling common cron script functions",
    "long_description": """\
CronScript implements a context manager for use with cron scripts.  It handles
logging, locking, and splaying (random sleep on startup.)
""",
    "author": "Jim Browne",
    "author_email": "jbrowne@jbrowne.com",
    "maintainer": "Jim Browne",
    "maintainer_email": "jbrowne@jbrowne.com",
    "url": 'https://github.com/jimbrowne/pycronscript',
    "license": "Apache Software License",
    "packages": ["pycronscript"],
    "keywords": ["cron", "pycronscript"],
    "install_requires": ['lockfile'],
    "python_requires": '>=3',
    "scripts": ["cronwrap"],
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
        "Topic :: System :: Systems Administration"
        ]
}

from distutils.core import setup

setup(**setup_args)
