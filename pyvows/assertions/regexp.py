#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pyVows testing engine
# https://github.com/heynemann/pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 Bernardo Heynemann heynemann@gmail.com

import re

from pyvows import Vows, VowsAssertionError

@Vows.assertion
def to_match(topic, expected):
    if not re.match(expected, topic):
        raise VowsAssertionError('Expected topic(%s) to match the regular expression %s', topic, expected)

@Vows.assertion
def not_to_match(topic, expected):
    if re.match(expected, topic):
        raise VowsAssertionError('Expected topic(%s) not to match the regular expression %s', topic, expected)

