#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4:et:sw=4:

# ----------------------------------------------------------------------
# Copyleft (K), Jose M. Rodriguez-Rosa (a.k.a. Boriel)
#
# This program is Free Software and is released under the terms of
#                    the GNU General License
# ----------------------------------------------------------------------
from typing import List

from src.api import global_

from src.api.constants import CLASS
from .symbol_ import Symbol
from .id_ import SymbolID


class SymbolLABEL(SymbolID):
    prefix = global_.MANGLE_CHR

    def __init__(self, name: str, lineno: int, filename: str = None):
        super().__init__(name=name, lineno=lineno, filename=filename)
        self.mangled = f"{global_.LABELS_NAMESPACE}.{self.prefix}{name}"
        self.class_ = CLASS.label
        self._scope_owner = []  # list of nested functions containing this label (scope)
        self.aliased_by: List[Symbol] = []  # Which variables are an alias of this one

    @property
    def accessed(self):
        return self._accessed

    @accessed.setter
    def accessed(self, value):
        self._accessed = bool(value)
        if self._accessed:
            for entry in self.scope_owner:
                entry.accessed = True

    @property
    def scope_owner(self):
        return list(self._scope_owner)

    @scope_owner.setter
    def scope_owner(self, entries):
        assert all(isinstance(x, Symbol) for x in entries)
        self._scope_owner = list(entries)
        self.accessed = self._accessed  # if true, refresh scope_owners

    @property
    def t(self):
        return self.mangled

    def add_alias(self, entry: SymbolID):
        """Adds id to the current list 'aliased_by'"""
        assert isinstance(entry, SymbolID)
        self.aliased_by.append(entry)
