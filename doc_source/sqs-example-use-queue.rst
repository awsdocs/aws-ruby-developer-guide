.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-working-with-queues:

############################
Working with Queues in |SQS|
############################

.. meta::
    :description:
        Learn how to work with Amazon SQS queues using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, SQS

|SQS| provides highly scalable hosted queues for storing messages as they travel between applications
or microservices. To learn more about queues, see :SQS-dg:`How Amazon SQS Queues Work <sqs-how-it-works>`.

In this example, you use the |sdk-ruby| with |SQS| to:

#. Get a list of your queues by using :aws-ruby-sqs-client-method:`list_queues`.
#. Create a queue by using :aws-ruby-sqs-client-method:`create_queue`.
#. Get the queue's URL by using :aws-ruby-sqs-client-method:`get_queue_url`.
#. Delete the queue by using :aws-ruby-sqs-client-method:`delete_queue`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

*******
Example
*******

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-using-queues.rb
   :dedent: 0
   :language: ruby
