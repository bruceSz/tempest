# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from lxml import etree

from tempest.common.rest_client import RestClientXML
from tempest import config
from tempest.services.compute.xml.common import xml_to_json

CONF = config.CONF


class ExtensionsClientXML(RestClientXML):

    def __init__(self, auth_provider):
        super(ExtensionsClientXML, self).__init__(auth_provider)
        self.service = CONF.volume.catalog_type

    def _parse_array(self, node):
        array = []
        for child in node:
            array.append(xml_to_json(child))
        return array

    def list_extensions(self):
        url = 'extensions'
        resp, body = self.get(url)
        body = self._parse_array(etree.fromstring(body))
        return resp, body
