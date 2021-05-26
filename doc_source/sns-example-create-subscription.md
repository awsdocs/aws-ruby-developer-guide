# Creating a Subscription in an Amazon SNS Topic<a name="sns-example-create-subscription"></a>

The following example creates a subscription for the topic with the ARN `arn:aws:sns:us-west-2:123456789:MyGroovyTopic` for a user who has the email address `MyGroovyUser@MyGroovy.com` in the `us-west-2` region, and displays the resulting ARN\. Initially the ARN value is pending confirmation\. When the user confirms their email address, this value becomes a true ARN\.

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

require 'aws-sdk-sns'  # v2: require 'aws-sdk'

sns = Aws::SNS::Resource.new(region: 'us-west-2')

topic = sns.topic('arn:aws:sns:us-west-2:123456789:MyGroovyTopic')

sub = topic.subscribe({
  protocol: 'email',
  endpoint: 'MyGroovyUser@MyGroovy.com'
})

puts sub.arn
```