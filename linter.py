###
# Erlang linter plugin for SublimeLinter3
# Uses erlc, make sure it is in your PATH
#
# Copyright (C) 2014  Clement 'cmc' Rey <cr.rey.clement@gmail.com>
#
# MIT License
###

"""This module exports the Erlc plugin class."""

from SublimeLinter.lint import Linter, util


class Erlc(Linter):

    """Provides an interface to erlc."""

    syntax = (
        "erlang",
        "erlang improved"
    )

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
        command = [self.executable_path, '-W']

        settings = self.get_view_settings()
        dirs = settings.get('include_dirs', [])
        pa_dirs = settings.get('pa_dirs', [])
        pz_dirs = settings.get('pz_dirs', [])

        for d in dirs:
            command.extend(["-I", d])

        for d in pa_dirs:
            command.extend(["-pa", d])

        for d in pz_dirs:
            command.extend(["-pz", d])

        return command
