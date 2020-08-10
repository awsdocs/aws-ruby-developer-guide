.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-send-and-receive-messages:

#######################################
Sending and Receiving Messages in |SQS|
#######################################

.. meta::
    :description:
        Send and receive messages to Amazon SQS queues using this AWS SDK for Ruby
        code example.
    :keywords: AWS SDK for Ruby code examples, SQS

After you create a queue in |SQS|, you can send a message to it and then consume it. To learn more, see :SQS-dg:`Tutorial: Sending a Message to an Amazon SQS Queue <sqs-send-message>` and :SQS-dg:`Tutorial: Receiving and Deleting a Message from an Amazon SQS Queue <sqs-receive-delete-message>`.

In this example, you use the |sdk-ruby| with |SQS| to:

1. Send a message to a queue by using :aws-ruby-sqs-client-method:`send_message`.

.. note:: If your queue is a FIFO queue, you must include a
   :code:`message_group_id` parameter in addition to the
   :code:`id` and :code:`message_body` parameters.

2. Receive the message in the queue by using :aws-ruby-sqs-client-method:`receive_message`.
3. Display information about the message.
4. Delete the message from the queue by using :aws-ruby-sqs-client-method:`delete_message`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You also need to create the queue `my-queue`, which you can do in the |SQS| console.

*******
Example
*******

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-send-receive-messages.rb
   :dedent: 0
   :language: ruby
