# Receiving Messages Using Long Polling in Amazon SQS<a name="sqs-example-get-messages-with-long-polling"></a>

The following example waits up to 10 seconds to display the bodies of up to 10 messages in the Amazon SQS queue with the URL `URL` in the `us-west-2` region\.

If you do not specify a wait time, the default value is **0** \(Amazon SQS does not wait\)\.

```
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

require 'aws-sdk-sqs'  # v2: require 'aws-sdk'

sqs = Aws::SQS::Client.new(region: 'us-west-2')

resp = sqs.receive_message(queue_url: URL, max_number_of_messages: 10, wait_time_seconds: 10)

resp.messages.each do |m|
  puts m.body
end
```