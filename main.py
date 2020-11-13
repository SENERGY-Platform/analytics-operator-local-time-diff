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
import typing
from datetime import datetime, timezone

from senergy_local_analytics import App, Input, Output


def process(inputs: typing.List[Input]):
    timestamp_string = ""
    message_id = ""
    dt = datetime.now()
    timestamp_now = dt.replace(tzinfo=timezone.utc).timestamp()
    for inp in inputs:
        if inp.current_value is not None:
            if inp.name == "timestamp" and inp.current_value is not None:
                timestamp_string = inp.current_value
            if inp.name == "message_id" and inp.current_value is not None:
                message_id = inp.current_value
    timestamp_then = datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%S.%fZ').replace(tzinfo=timezone.utc).timestamp()
    return Output(True, {"message_id": message_id, "time_diff": timestamp_now - timestamp_then})


if __name__ == '__main__':
    app = App()

    input1 = Input("timestamp")
    input2 = Input("message_id")

    app.config([input1, input2])
    print("start operator", flush=True)
    app.process_message(process)
    app.main()
