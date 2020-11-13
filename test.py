#  Copyright 2020 InfAI (CC SES)
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import unittest
from datetime import datetime, timezone


class TestMainMethods(unittest.TestCase):

    def test_conv(self):
        timestamp_string = "2020-11-13T10:20:54.463207Z"
        timestamp_then = datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(
            tzinfo=timezone.utc).timestamp()
        self.assertEqual(1605262854.463207, timestamp_then)
