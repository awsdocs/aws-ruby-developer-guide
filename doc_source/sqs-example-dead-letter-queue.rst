.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-dead-letter-queues:

################################
Working with a Dead Letter Queue
################################

.. meta::
   :description:
   :keywords: AWS SDK for Ruby code examples

|SQSlong| provides support for dead letter queues. A dead letter queue is a queue that other (source) queues can target for messages that can't be processed successfully. You can set aside and isolate these messages in the dead letter queue to determine why their processing did not succeed. For more information about dead letter queues, see :SQS-dg:`Using Amazon SQS Dead Letter Queues <sqs-dead-letter-queues>`.

In this example, you use the |sdk-ruby| with |SQS| to:

#. Create a queue representing a dead letter queue, using :aws-ruby-sqs-client-method:`create_queue`.
#. Associate the dead letter queue with an existing queue, using :aws-ruby-sqs-client-method:`set_queue_attributes`.
#. Send a message to the existing queue, using :aws-ruby-sqs-client-method:`send_message`.
#. Poll the queue, using `Aws::SQS::QueuePoller <http://docs.aws.amazon.com/sdkforruby/api/Aws/SQS/QueuePoller.html>`_.
#. Receive messages in the dead letter queue, using :aws-ruby-sqs-client-method:`receive_message`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You will also need to use the AWS Console to create the existing queue, `my-queue`.

*******
Example
*******

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-dead-letter-queue.rb
   :lines: 17-95
   :dedent: 0
   :language: ruby
