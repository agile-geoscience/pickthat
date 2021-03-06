#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An object to hold a set of picks.

:copyright: 2015 Agile Geoscience
:license: Apache 2.0
"""


class Pick(object):
    def __init__(self, data):
        self.__dict__ = dict(data)
        for k, v in data.items():
            if k and v:
                setattr(self, k, v)
