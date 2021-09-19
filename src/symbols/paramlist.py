#!/usr/bin/python
# -*- coding: utf-8 -*-
# vim: ts=4:et:sw=4:

# ----------------------------------------------------------------------
# Copyleft (K), Jose M. Rodriguez-Rosa (a.k.a. Boriel)
#
# This program is Free Software and is released under the terms of
#                    the GNU General License
# ----------------------------------------------------------------------

from .symbol_ import Symbol


class SymbolPARAMLIST(Symbol):
    """Defines a list of parameters definitions in a function header"""

    def __init__(self, *params):
        super(SymbolPARAMLIST, self).__init__(*params)
        self.size = 0

    def __getitem__(self, key):
        return self.children[key]

    def __setitem__(self, key, value):
        self.children[key] = value

    def __len__(self):
        return len(self.children)

    @classmethod
    def make_node(cls, node, *params):
        """This will return a node with a param_list
        (declared in a function declaration)
        Parameters:
            -node: A SymbolPARAMLIST instance or None
            -params: SymbolPARAMDECL instances
        """
        if node is None:
            node = cls()

        if node.token != "PARAMLIST":
            return cls.make_node(None, node, *params)

        for i in params:
            if i is not None:
                node.append_child(i)

        return node

    def append_child(self, param):
        """Overrides base class."""
        Symbol.append_child(self, param)
        if param.offset is None:
            param.offset = self.size
            self.size += param.size
