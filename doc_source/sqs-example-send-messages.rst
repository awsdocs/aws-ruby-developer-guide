.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-send-messages:

#########################
Sending Messages in |SQS|
#########################

.. meta::
    :description:
        Learn how to send messages to Amazon SQS queues using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, SQS

The following example sends the message "Hello world" through the |SQS| queue with the URL
:code:`URL` in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-send-message.rb
   :dedent: 0
   :language: ruby

The following example sends the messages "Hello world" and "How is the weather?" through the |SQS|
queue with the URL :code:`URL` in the :code:`us-west-2` region.

.. note:: If your queue is a FIFO queue, you must include a
	  :code:`message_group_id` parameter in addition to the
          :code:`id` and :code:`message_body` parameters.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-send-message-batch.rb
   :dedent: 0
   :language: ruby
