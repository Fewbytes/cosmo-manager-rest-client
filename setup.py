########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
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

__author__ = 'ran'

from setuptools import setup

version = '0.3'

setup(
    name='cosmo-manager-rest-client',
    version=version,
    author='ran',
    author_email='ran@gigaspaces.com',
    packages=['cosmo_manager_rest_client',
              'cosmo_manager_rest_client.swagger',
              'cosmo_manager_rest_client.swagger''.models'],
    license='LICENSE',
    description='the cosmo manager rest client',
    install_requires=['requests']
)
