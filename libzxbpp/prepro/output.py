#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:sw=4:

""" Common output functions for the preprocessor.
Need the global OPTION object
"""

import src.api.errmsg

CURRENT_FILE = []  # The current file being processed


def error(lineno, str_):
    src.api.errmsg.error(lineno, str_)


def warning(lineno, str_):
    src.api.errmsg.warning(lineno, str_)
