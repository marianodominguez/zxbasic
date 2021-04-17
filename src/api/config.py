#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:ts=4:et:sw=4:

# ----------------------------------------------------------------------
# Copyleft (K), Jose M. Rodriguez-Rosa (a.k.a. Boriel)
#
# This program is Free Software and is released under the terms of
#                    the GNU General License
# ----------------------------------------------------------------------

import os
import sys
import configparser

from src import api

# The options container
from . import options
from . import global_

from .options import ANYTYPE, Actions


# ------------------------------------------------------
# Common setup and configuration for all tools
# ------------------------------------------------------
class ConfigSections:
    ZXBC = 'zxbc'
    ZXBASM = 'zxbasm'
    ZXBPP = 'zxbpp'


class OPTION:
    OUTPUT_FILENAME = 'output_filename'
    INPUT_FILENAME = 'input_filename'
    STDERR_FILENAME = 'stderr_filename'
    DEBUG = 'debug_level'
    PROJECT_FILENAME = 'project_filename'

    # File IO
    STDIN = 'stdin'
    STDOUT = 'stdout'
    STDERR = 'stderr'

    O_LEVEL = 'optimization_level'
    CASE_INS = 'case_insensitive'
    ARRAY_BASE = 'array_base'
    STR_BASE = 'string_base'
    DEFAULT_BYREF = 'default_byref'
    MAX_SYN_ERRORS = 'max_syntax_errors'

    MEMORY_MAP = 'memory_map'

    USE_BASIC_LOADER = 'use_basic_loader'
    AUTORUN = 'autorun'
    OUTPUT_FILE_TYPE = 'output_file_type'
    INCLUDE_PATH = 'include_path'

    CHECK_MEMORY = 'memory_check'
    CHECK_ARRAYS = 'array_check'

    STRICT_BOOL = 'strict_bool'

    ENABLE_BREAK = 'enable_break'
    EMIT_BACKEND = 'emit_backend'

    EXPLICIT = 'explicit'
    STRICT = 'strict'

    ARCH = 'architecture'
    EXPECTED_WARNINGS = 'expected_warnings'
    HIDE_WARNING_CODES = 'hide_warning_codes'

    # ASM Options
    ASM_ZXNEXT = 'zxnext'
    FORCE_ASM_BRACKET = 'force_asm_brackets'


OPTIONS = options.Options()
OPTIONS_NOT_SAVED = {
    OPTION.STDERR, OPTION.STDIN, OPTION.STDOUT, 'sinclair', OPTION.INPUT_FILENAME, OPTION.OUTPUT_FILENAME,
    OPTION.PROJECT_FILENAME, 'heap_start_label', 'heap_size_label'
}


def load_config_from_file(filename: str, section: str, options_: options.Options = None, stop_on_error=True) -> bool:
    """ Opens file and read options from the given section. If stop_on_error is set,
    the program stop. Otherwise the result of the operation will be
    returned (True on success, False on failure)
    """
    if options_ is None:
        options_ = OPTIONS

    try:
        cfg = configparser.ConfigParser()
        cfg.read(filename, encoding='utf-8')
    except (configparser.DuplicateSectionError, configparser.DuplicateOptionError):
        api.errmsg.msg_output(f"Invalid config file '{filename}': it has duplicated fields")
        if stop_on_error:
            sys.exit(1)
        return False
    except FileNotFoundError:
        api.errmsg.msg_output(f"Config file '{filename}' not found")
        if stop_on_error:
            sys.exit(1)
        return False

    if section not in cfg.sections():
        api.errmsg.msg_output(f"Section '{section}' not found in config file '{filename}'")
        if stop_on_error:
            sys.exit(1)
        return False

    parsing = {
        int: cfg.getint,
        float: cfg.getfloat,
        bool: cfg.getboolean
    }

    for opt in cfg.options(section):
        options_[opt].value = parsing.get(options_[opt].type, cfg.get)(section=section, option=opt)

    return True


def save_config_into_file(filename: str, section: str, options_: options.Options = None, stop_on_error=True) -> bool:
    """ Save config into config ini file into the given section. If stop_on_error is set,
    the program stop. Otherwise the result of the operation will be
    returned (True on success, False on failure)
    """
    if options_ is None:
        options_ = OPTIONS

    cfg = configparser.ConfigParser()
    if os.path.exists(filename):
        try:
            cfg.read(filename, encoding='utf-8')
        except (configparser.DuplicateSectionError, configparser.DuplicateOptionError):
            api.errmsg.msg_output(f"Invalid config file '{filename}': it has duplicated fields")
            if stop_on_error:
                sys.exit(1)
            return False

    cfg[section] = {}
    for opt_name, opt in options_().items():
        if opt_name.startswith('__') or opt.value is None or opt_name in OPTIONS_NOT_SAVED:
            continue

        if opt.type == bool:
            cfg[section][opt_name] = str(opt.value).lower()
            continue

        cfg[section][opt_name] = str(opt.value)

    try:
        with open(filename, 'wt', encoding='utf-8') as f:
            cfg.write(f)
    except IOError:
        api.errmsg.msg_output(f"Can't write config file '{filename}'")
        if stop_on_error:
            sys.exit(1)
        return False

    return True


def init():
    """
    Default Options and Compilation Flags

    optimization -- Optimization level. Use -O flag to change.
    case_insensitive -- Whether user identifiers are case insensitive
                             or not
    array_base -- Default array lower bound
    param_byref --Default parameter passing. TRUE => By Reference
    """

    OPTIONS(Actions.CLEAR)

    OPTIONS(Actions.ADD, name=OPTION.OUTPUT_FILENAME, type=str)
    OPTIONS(Actions.ADD, name=OPTION.INPUT_FILENAME, type=str)
    OPTIONS(Actions.ADD, name=OPTION.STDERR_FILENAME, type=str)
    OPTIONS(Actions.ADD, name=OPTION.DEBUG, type=int, default=0)

    # Default console redirections
    OPTIONS(Actions.ADD, name=OPTION.STDIN, type=ANYTYPE, default=sys.stdin)
    OPTIONS(Actions.ADD, name=OPTION.STDOUT, type=ANYTYPE, default=sys.stdout)
    OPTIONS(Actions.ADD, name=OPTION.STDERR, type=ANYTYPE, default=sys.stderr)

    OPTIONS(Actions.ADD, name=OPTION.O_LEVEL, type=int, default=global_.DEFAULT_OPTIMIZATION_LEVEL)
    OPTIONS(Actions.ADD, name=OPTION.CASE_INS, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.ARRAY_BASE, type=int, default=0)
    OPTIONS(Actions.ADD, name=OPTION.DEFAULT_BYREF, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.MAX_SYN_ERRORS, type=int, default=global_.DEFAULT_MAX_SYNTAX_ERRORS)
    OPTIONS(Actions.ADD, name=OPTION.STR_BASE, type=int, default=0)
    OPTIONS(Actions.ADD, name=OPTION.MEMORY_MAP, type=str, default=None)
    OPTIONS(Actions.ADD, name=OPTION.FORCE_ASM_BRACKET, type=bool, default=False)

    OPTIONS(Actions.ADD, name=OPTION.USE_BASIC_LOADER, type=bool, default=False)  # Whether to use a loader

    # Whether to add autostart code (needs basic loader = true)
    OPTIONS(Actions.ADD, name=OPTION.AUTORUN, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.OUTPUT_FILE_TYPE, type=str, default='bin')  # bin, tap, tzx etc...
    OPTIONS(Actions.ADD, name=OPTION.INCLUDE_PATH, type=str, default='')  # Include path, like '/var/lib:/var/include'

    OPTIONS(Actions.ADD, name=OPTION.CHECK_MEMORY, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.STRICT_BOOL, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.CHECK_ARRAYS, type=bool, default=False)

    OPTIONS(Actions.ADD, name=OPTION.ENABLE_BREAK, type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.EMIT_BACKEND, type=bool, default=False)
    OPTIONS(Actions.ADD, name='__DEFINES', type=dict, default={})
    OPTIONS(Actions.ADD, name=OPTION.EXPLICIT, type=bool, default=False)
    OPTIONS(Actions.ADD, name='sinclair', type=bool, default=False)
    OPTIONS(Actions.ADD, name=OPTION.STRICT, type=bool, default=False)  # True to force type checking
    OPTIONS(Actions.ADD, name=OPTION.ASM_ZXNEXT, type=bool, default=False)  # True to enable ZX Next ASM opcodes
    OPTIONS(Actions.ADD, name=OPTION.ARCH, type=str, default=None)  # Architecture
    OPTIONS(Actions.ADD, name=OPTION.EXPECTED_WARNINGS, type=int, default=0)  # Expected Warnings that will be silenced

    # Whether to show WXXX warning codes or not
    OPTIONS(Actions.ADD, name=OPTION.HIDE_WARNING_CODES, type=bool, default=False)

    OPTIONS(Actions.ADD, name=OPTION.PROJECT_FILENAME, type=str, default=os.path.join(os.path.abspath(os.path.curdir),
                                                                                      'project.ini'))


init()
