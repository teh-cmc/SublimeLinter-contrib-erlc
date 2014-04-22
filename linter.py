###
# Erlang linter plugin from SublimeLinter3
# Uses erlc, make sure it is in your PATH
#
# Copyright (C) 2014  Clement 'cmc' Rey <cr.rey.clement@gmail.com>
#
# MIT License
###

"""This module exports the Erlc plugin class."""

import shlex
from SublimeLinter.lint import Linter, util


class Erlc(Linter):

    """Provides an interface to escript."""

    syntax = (
        "erlang",
        "erlang improved"
    )

    cmd = None
    executable = "erlc"
    tempfile_suffix = "erl"

    # ERROR FORMAT # <file>:<line>: [Warning:|] <message> #
    regex = (
        r".+:(?P<line>\d+):"
        r"(?:(?P<warning>\sWarning:\s)|(?P<error>\s))"
        r"+(?P<message>.+)"
    )

    error_stream = util.STREAM_STDOUT

    defaults = {
        "include_dirs": []
    }

    def cmd(self):
        """
        return the command line to execute.

        this func is overridden so we can handle included directories.
        """
        ret = "erlc -W"

        settings = self.get_view_settings()
        dirs = settings.get('include_dirs', [])

        if dirs:
            ret += " " + " ".join(["-I" + shlex.quote(i) for i in dirs])

        return ret