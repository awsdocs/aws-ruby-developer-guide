# Working with a Dead Letter Queue in Amazon SQS<a name="sqs-example-dead-letter-queue"></a>

Amazon SQS provides support for dead letter queues\. A dead letter queue is a queue that other \(source\) queues can target for messages that can’t be processed successfully\. You can set aside and isolate these messages in the dead letter queue to determine why their processing didn’t succeed\. For more information about dead letter queues, see [Using Amazon SQS Dead Letter Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)\.

In this example, you use the AWS SDK for Ruby with Amazon SQS to:

1. Create a queue that represents a dead letter queue by using [Aws::SQS::Client\#create\_queue](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#create_queue-instance_method)\.

1. Associate the dead letter queue with an existing queue by using [Aws::SQS::Client\#set\_queue\_attributes](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#set_queue_attributes-instance_method)\.

1. Send a message to the existing queue by using [Aws::SQS::Client\#send\_message](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#send_message-instance_method)\.

1. Poll the queue by using [Aws::SQS::QueuePoller](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/SQS/QueuePoller.html)\.

1. Receive messages in the dead letter queue by using [Aws::SQS::Client\#receive\_message](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#receive_message-instance_method)\.

## Prerequisites<a name="prerequisites"></a>

Before running the example code, you need to install and configure the AWS SDK for Ruby, as described in:
+  [Installing the AWS SDK for Ruby](setup-install.md#aws-ruby-sdk-setup-install) 
+  [Configuring the AWS SDK for Ruby](setup-config.md#aws-ruby-sdk-setup-config) 

You also need to use the AWS Management Console to create the existing queue, *my\-queue*\.

**Note**  
For the sake of simplicity, this example code doesn’t demonstrate [Aws::SQS::Client\#add\_permission](https://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/Client.html#add_permission-instance_method)\. In a real\-world scenario, you should always restrict access to actions such as SendMessage, ReceiveMessage, DeleteMessage, and DeleteQueue\. Not doing so could cause information disclosure, denial of service, or injection of messages into your queues\.

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
# 1. Create a queue representing a dead letter queue.
# 2. Associate the dead letter queue with an existing queue.

require 'aws-sdk-sqs'  # v2: require 'aws-sdk'

# Uncomment for Windows.
# Aws.use_bundled_cert!

sqs = Aws::SQS::Client.new(region: 'us-east-1')

# Create a queue representing a dead letter queue.
dead_letter_queue_name = "dead-letter-queue"

sqs.create_queue({
  queue_name: dead_letter_queue_name
})

# Get the dead letter queue's URL and ARN, so that you can associate it with an existing queue.
dead_letter_queue_url = sqs.get_queue_url(queue_name: dead_letter_queue_name).queue_url

dead_letter_queue_arn = sqs.get_queue_attributes({
  queue_url: dead_letter_queue_url,
  attribute_names: ["QueueArn"]
}).attributes["QueueArn"]

# Associate the dead letter queue with an existing queue.
begin
  queue_name = "my-queue"
  queue_url = sqs.get_queue_url(queue_name: queue_name).queue_url

  # Use a redrive policy to specify the dead letter queue and its behavior.
  redrive_policy = {
    "maxReceiveCount" => "5", # After the queue receives the same message 5 times, send that message to the dead letter queue.
    "deadLetterTargetArn" => dead_letter_queue_arn
  }.to_json

  sqs.set_queue_attributes({
    queue_url: queue_url,
    attributes: {
      "RedrivePolicy" => redrive_policy
    }
  })

rescue Aws::SQS::Errors::NonExistentQueue
  puts "A queue named '#{queue_name}' does not exist."
  exit(false)
end

# Send a message to the queue.
puts "Sending a message..."

sqs.send_message({
  queue_url: queue_url,
  message_body: "I hope I get moved to the dead letter queue."
})

30.downto(0) do |i|
  print "\rWaiting #{i} second(s) for sent message to be receivable..."
  sleep(1)
end

puts "\n"

poller = Aws::SQS::QueuePoller.new(queue_url)
# Receive 5 messages max and stop polling after 20 seconds of no received messages.
poller.poll(max_number_of_messages:5, idle_timeout: 20) do |messages|
  messages.each do |msg|
    puts "Received message ID: #{msg.message_id}"
  end
end

# Check to see if Amazon SQS moved the message to the dead letter queue.
receive_message_result = sqs.receive_message({
  queue_url: dead_letter_queue_url,
  max_number_of_messages: 1
})

if receive_message_result.messages.count > 0
  puts "\n#{receive_message_result.messages[0].body}"
else
  puts "\nNo messages received."
end
```