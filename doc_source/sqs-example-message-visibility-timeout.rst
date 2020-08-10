.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-message-visibility-timeout:

##################################################
Specifying the Message Visibility Timeout in |SQS|
##################################################

.. meta::
   :description:
       Specify a message's visibility timeout in Amazon SQS using this AWS SDK for Ruby code
       example.
   :keywords: AWS SDK for Ruby code examples, SQS

In |SQS|, immediately after a message is received, it remains in the queue. To prevent other consumers
from processing the message again, |SQS| sets a visibility timeout. This is a period of time during which
|SQS| prevents other consuming components from receiving and processing the message. To learn more, see
:SQS-dg:`Visibility Timeout <sqs-visibility-timeout>`.

In this example, you use the |sdk-ruby| with |SQS| to:

#. Get the URL of an existing queue by using :aws-ruby-sqs-client-method:`get_queue_url`.
#. Receive up to 10 messages by using :aws-ruby-sqs-client-method:`receive_message`.
#. Specify the time interval during which messages are not visible after they are received, by using :aws-ruby-sqs-client-method:`change_message_visibility`.

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

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-message-visibility-timeout.rb
   :dedent: 0
   :language: ruby
