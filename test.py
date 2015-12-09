#!/usr/bin/env python

# Copyright 2014-5 42Lines, Inc.
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

''' Simple test of CronScript functionality '''

from pycronscript import CronScript
import logging
from optparse import make_option
import time

OPTIONS = []
OPTIONS.append(make_option("--snarf", action="store_true",
                           help="Snarf snarf snarf"))
OPTIONS.append(make_option("--foobar", type="string",
                           default='barbaz',
                           help="Mew mew mew, default %default"))
USAGE = "usage: %prog [options] arg1 arg2"

with CronScript(options=OPTIONS, usage=USAGE) as options:
    LOGGER = logging.getLogger(__name__)
    LOGGER.info('Does this work?')

    print "Options are: %s" % options
    time.sleep(900)
