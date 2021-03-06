# -*- coding: utf-8 -*-
# Copyright 2020, CS GROUP - France, http://www.c-s.fr
#
# This file is part of EODAG project
#     https://www.github.com/CS-SI/EODAG
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import absolute_import, print_function, unicode_literals

import logging

from eodag.plugins.base import PluginTopic

logger = logging.getLogger("eodag.plugins.apis.base")


class Api(PluginTopic):
    """Plugins API Base plugin"""

    def query(self, *args, **kwargs):
        """Implementation of how the products must be searched goes here.

        This method must return a list of EOProduct instances (see eodag.api.product module) which will
        be processed by a Download plugin.
        """
        raise NotImplementedError("A Api plugin must implement a method named query")

    def download(self, *args, **kwargs):
        """Implementation of how the products must be downloaded."""
        raise NotImplementedError("A Api plugin must implement a method named download")
