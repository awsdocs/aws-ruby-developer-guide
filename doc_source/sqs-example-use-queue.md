# Working with Queues in Amazon SQS<a name="sqs-example-use-queue"></a>

Amazon SQS provides highly scalable hosted queues for storing messages as they travel between applications or microservices\. To learn more about queues, see [How Amazon SQS Queues Work](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-how-it-works.html)\.

In this example, you use the AWS SDK for Ruby with Amazon SQS to:

1. Get a list of your queues by using [Aws::SQS::Client\#list\_queues](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#list_queues-instance_method)\.

1. Create a queue by using [Aws::SQS::Client\#create\_queue](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#create_queue-instance_method)\.

1. Get the queue’s URL by using [Aws::SQS::Client\#get\_queue\_url](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#get_queue_url-instance_method)\.

1. Delete the queue by using [Aws::SQS::Client\#delete\_queue](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#delete_queue-instance_method)\.

## Prerequisites<a name="prerequisites"></a>

Before running the example code, you need to install and configure the AWS SDK for Ruby, as described in:
+  [Installing the AWS SDK for Ruby](setup-install.md#aws-ruby-sdk-setup-install) 
+  [Configuring the AWS SDK for Ruby](setup-config.md#aws-ruby-sdk-setup-config) 

## Example<a name="example"></a>

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

# Demonstrates how to:
# 1. Get a list of your queues.
# 2. Create a queue.
# 3. Get the queue's URL.
# 4. Delete the queue.

require 'aws-sdk-sqs'  # v2: require 'aws-sdk'

sqs = Aws::SQS::Client.new(region: 'us-east-1')

# Get a list of your queues.
sqs.list_queues.queue_urls.each do |queue_url|
  puts queue_url
end

# Create a queue.
queue_name = "my-queue"

begin
  sqs.create_queue({
    queue_name: queue_name,
    attributes: {
      "DelaySeconds" => "60", # Delay message delivery for 1 minute (60 seconds).
      "MessageRetentionPeriod" => "86400" # Delete message after 1 day (24 hours * 60 minutes * 60 seconds).    
    }
  })
rescue Aws::SQS::Errors::QueueDeletedRecently
  puts "A queue with the name '#{queue_name}' was recently deleted. Wait at least 60 seconds and try again."
  exit(false)
end

# Get the queue's URL.
queue_url = sqs.get_queue_url(queue_name: queue_name).queue_url
puts queue_url

# Delete the queue.
sqs.delete_queue(queue_url: queue_url)
```