# Specifying the Message Visibility Timeout in Amazon SQS<a name="sqs-example-message-visibility-timeout"></a>

In Amazon SQS, immediately after a message is received, it remains in the queue\. To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout\. This is a period of time during which Amazon SQS prevents other consuming components from receiving and processing the message\. To learn more, see [Visibility Timeout](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html)\.

In this example, you use the AWS SDK for Ruby with Amazon SQS to:

1. Get the URL of an existing queue by using [Aws::SQS::Client\#get\_queue\_url](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#get_queue_url-instance_method)\.

1. Receive up to 10 messages by using [Aws::SQS::Client\#receive\_message](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#receive_message-instance_method)\.

1. Specify the time interval during which messages are not visible after they are received, by using [Aws::SQS::Client\#change\_message\_visibility](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#change_message_visibility-instance_method)\.

## Prerequisites<a name="prerequisites"></a>

Before running the example code, you need to install and configure the AWS SDK for Ruby, as described in:
+  [Installing the AWS SDK for Ruby](setup-install.md#aws-ruby-sdk-setup-install) 
+  [Configuring the AWS SDK for Ruby](setup-config.md#aws-ruby-sdk-setup-config) 

You also need to create the queue *my\-queue*, which you can do in the Amazon SQS console\.

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

# Demonstrates how to specify the time interval during which messages to a queue are not visible after being received.

require 'aws-sdk-sqs'  # v2: require 'aws-sdk'

sqs = Aws::SQS::Client.new(region: 'us-east-1')

begin
  queue_name = "my-queue"
  queue_url = sqs.get_queue_url(queue_name: queue_name).queue_url

  receive_message_result_before = sqs.receive_message({
    queue_url: queue_url,    
    max_number_of_messages: 10 # Receive up to 10 messages, if there are that many.
  })

  puts "Before attempting to change message visibility timeout: received #{receive_message_result_before.messages.count} message(s)."

  receive_message_result_before.messages.each do |message|
    sqs.change_message_visibility({
      queue_url: queue_url,
      receipt_handle: message.receipt_handle,
      visibility_timeout: 30 # This message will not be visible for 30 seconds after first receipt.
    })    
  end  

  # Try to retrieve the original messages after setting their visibility timeout. 
  receive_message_result_after = sqs.receive_message({
    queue_url: queue_url,
    max_number_of_messages: 10
  })

  puts "\nAfter attempting to change message visibility timeout: received #{receive_message_result_after.messages.count} message(s)."

rescue Aws::SQS::Errors::NonExistentQueue
  puts "Cannot receive messages for a queue named '#{receive_queue_name}', as it does not exist."
end
```