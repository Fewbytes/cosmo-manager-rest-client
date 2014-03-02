########
# Copyright (c) 2014 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#    * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    * See the License for the specific language governing permissions and
#    * limitations under the License.

import unittest
from cosmo_manager_rest_client.cosmo_manager_rest_client\
    import CosmoManagerRestClient


class RestClientUrlTest(unittest.TestCase):

    def test_ip(self):
        ip = '1.2.3.4'
        c = CosmoManagerRestClient(ip)
        self.assertEquals(
            'http://' + ip + ':8100', c._blueprints_api.api_client.apiServer)

    def test_url(self):
        url = 'https://example.com/api'
        c = CosmoManagerRestClient(url)
        self.assertEquals(
            url, c._blueprints_api.api_client.apiServer)
