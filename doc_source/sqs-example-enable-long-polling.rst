.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-enable-long-polling:

##############################
Enabling Long Polling in |SQS|
##############################

.. meta::
   :description: Enable long polling in Amazon SQS using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, SQS

Long polling helps lower your cost of using |SQS| by reducing the number of empty responses and eliminating
false empty responses. For more information about long polling, see :SQS-dg:`Amazon SQS Long Polling <sqs-long-polling>`.

In this example, you use the |sdk-ruby| with |SQS| to:

#. Create a queue and set it for long polling by using :aws-ruby-sqs-client-method:`create_queue`.
#. Set long polling for an existing queue by using :aws-ruby-sqs-client-method:`set_queue_attributes`.
#. Set long polling when receiving messages for a queue by using :aws-ruby-sqs-client-method:`receive_message`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You also need to create the queues `existing-queue` and `receive-queue`, which you can do in the |SQS| console.

*******
Example
*******

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-enable-long-polling.rb
   :dedent: 0
   :language: ruby
