###
# Erlang linter plugin from SublimeLinter3
# Using escript, make sure it is in your PATH
#
# Copyright (C) 2014  Clement 'cmc' Rey <cr.rey.clement@gmail.com>
#
# MIT License
###

"""
This module exports the Escript plugin class
"""

import shlex
from SublimeLinter.lint import Linter, util, persist


class Erlc(Linter):
    """
    Provides an interface to escript
    """