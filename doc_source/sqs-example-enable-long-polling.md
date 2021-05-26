# Enabling Long Polling in Amazon SQS<a name="sqs-example-enable-long-polling"></a>

Long polling helps lower your cost of using Amazon SQS by reducing the number of empty responses and eliminating false empty responses\. For more information about long polling, see [Amazon SQS Long Polling](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-long-polling.html)\.

In this example, you use the AWS SDK for Ruby with Amazon SQS to:

1. Create a queue and set it for long polling by using [Aws::SQS::Client\#create\_queue](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#create_queue-instance_method)\.

1. Set long polling for an existing queue by using [Aws::SQS::Client\#set\_queue\_attributes](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#set_queue_attributes-instance_method)\.

1. Set long polling when receiving messages for a queue by using [Aws::SQS::Client\#receive\_message](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#receive_message-instance_method)\.

## Prerequisites<a name="prerequisites"></a>

Before running the example code, you need to install and configure the AWS SDK for Ruby, as described in:
+  [Installing the AWS SDK for Ruby](setup-install.md#aws-ruby-sdk-setup-install) 
+  [Configuring the AWS SDK for Ruby](setup-config.md#aws-ruby-sdk-setup-config) 

You also need to create the queues *existing\-queue* and *receive\-queue*, which you can do in the Amazon SQS console\.

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
# 1. Create a queue and set it for long polling.
# 2. Set long polling for an existing queue.
# 3. Set long polling when receiving messages for a queue.

require 'aws-sdk-sqs'  # v2: require 'aws-sdk'

sqs = Aws::SQS::Client.new(region: 'us-east-1')

# Create a queue and set it for long polling.
new_queue_name = "new-queue"

create_queue_result = sqs.create_queue({
  queue_name: new_queue_name,
  attributes: {
    "ReceiveMessageWaitTimeSeconds" => "20" # Wait 20 seconds to receive messages.
  },
})
  
puts create_queue_result.queue_url

# Set long polling for an existing queue.
begin
  existing_queue_name = "existing-queue"
  existing_queue_url = sqs.get_queue_url(queue_name: existing_queue_name).queue_url

  sqs.set_queue_attributes({
    queue_url: existing_queue_url,
    attributes: { 
      "ReceiveMessageWaitTimeSeconds" => "20" # Wait 20 seconds to receive messages.
    },
  })
rescue Aws::SQS::Errors::NonExistentQueue
  puts "Cannot set long polling for a queue named '#{existing_queue_name}', as it does not exist."
end

# Set long polling when receiving messages for a queue.

# 1. Using receive_message.
begin
  receive_queue_name = "receive-queue"
  receive_queue_url = sqs.get_queue_url(queue_name: receive_queue_name).queue_url

  puts "Begin receipt of any messages using receive_message..."
  receive_message_result = sqs.receive_message({
    queue_url: receive_queue_url,
    attribute_names: ["All"], # Receive all available built-in message attributes.
    message_attribute_names: ["All"], # Receive any custom message attributes.
    max_number_of_messages: 10 # Receive up to 10 messages, if there are that many.
  })

  puts "Received #{receive_message_result.messages.count} message(s)."
rescue Aws::SQS::Errors::NonExistentQueue
  puts "Cannot receive messages using receive_message for a queue named '#{receive_queue_name}', as it does not exist."
end 

# 2. Using Aws::SQS::QueuePoller.
begin
  puts "Begin receipt of any messages using Aws::SQS::QueuePoller..."
  puts "(Will keep polling until no more messages available for at least 60 seconds.)"
  poller = Aws::SQS::QueuePoller.new(receive_queue_url)

  poller_stats = poller.poll({
    max_number_of_messages: 10,
    idle_timeout: 60 # Stop polling after 60 seconds of no more messages available (polls indefinitely by default).
  }) do |messages|
    messages.each do |message|
      puts "Message body: #{message.body}"
    end
  end
  # Note: If poller.poll is successful, all received messages are automatically deleted from the queue.

  puts "Poller stats:"
  puts "  Polling started at: #{poller_stats.polling_started_at}"
  puts "  Polling stopped at: #{poller_stats.polling_stopped_at}"
  puts "  Last message received at: #{poller_stats.last_message_received_at}"
  puts "  Number of polling requests: #{poller_stats.request_count}"
  puts "  Number of received messages: #{poller_stats.received_message_count}"
rescue Aws::SQS::Errors::NonExistentQueue
  puts "Cannot receive messages using Aws::SQS::QueuePoller for a queue named '#{receive_queue_name}', as it does not exist."
end
```