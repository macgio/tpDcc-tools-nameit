#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tool that manages the nomenclature of your pipelines
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from tpDcc.core import tool
from tpDcc.libs.qt.widgets import toolset

# Defines ID of the tool
TOOL_ID = 'tpDcc-tools-nameit'

# We skip the reloading of this module when launching the tool
no_reload = True


class NameItTool(tool.DccTool, object):
    def __init__(self, *args, **kwargs):
        super(NameItTool, self).__init__(*args, **kwargs)

    def launch(self, *args, **kwargs):
        return self.launch_frameless(*args, **kwargs)


class NameItToolset(toolset.ToolsetWidget, object):
    ID = TOOL_ID

    def __init__(self, *args, **kwargs):
        super(NameItToolset, self).__init__(*args, **kwargs)

    def contents(self):

        from tpDcc.tools.nameit.widgets import nameit

        name_it = nameit.NameIt()
        return [name_it]
