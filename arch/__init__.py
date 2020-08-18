#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:ts=4:et:sw=4:

import importlib

from . import zx48k


__all__ = [
    'zx48k',
]

AVAILABLE_ARCHITECTURES = __all__
target = None


def set_target_arch(target_arch: str):
    global target
    assert target_arch in AVAILABLE_ARCHITECTURES
    target = importlib.import_module(f'.{target_arch}', 'arch')


set_target_arch(AVAILABLE_ARCHITECTURES[0])
