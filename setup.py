#!/usr/bin/env python
#
# Copyright 2014 42Lines, Inc.
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


setup_args = {
    "name": "pycronscript",
    "version": "0.1.0",
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
    "classifiers": [
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: System :: Systems Administration"
        ]
}

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(**setup_args)
