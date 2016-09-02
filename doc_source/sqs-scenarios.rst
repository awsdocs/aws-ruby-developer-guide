.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-scenarios:

#####
|SQS|
#####

This section provides solutions to some common |SQS| scenarios using the |sdk-ruby|. For more
information about |SQS|, see the `SQS-dg`_.

You can find more examples of using the |sdk-ruby| with |SQS| in :ref:`aws-ruby-sdk-sqs-recipes`.

This section contains the following solutions:

* :ref:`aws-ruby-sdk-sns-scenario-enable-long-polling`

* :ref:`aws-ruby-sdk-sns-scenario-visibility-timeout`

* :ref:`aws-ruby-sdk-sns-scenario-sending-receiving-messages`

* :ref:`aws-ruby-sdk-sns-scenario-queues`

* :ref:`aws-ruby-sdk-sns-scenario-dead-letter-queues`

.. _aws-ruby-sdk-sns-scenario-enable-long-polling:

Enabling Long Polling
=====================

You poll messages in |SQS| to read and delete messages in one loop. Long polling configures the
|SQS| service to wait until a message is available in the queue before sending a response.


.. _aws-ruby-sdk-sns-scenario-visibility-timeout:

Managing Visibility Timeout
===========================

You have a fixed amount of time, called the *visibility timeout period*, to process a message before
it is added back into the queue (processed messages are automatically deleted). The following
examples show you two ways to manage visibility timeout in |SQS|.


.. _aws-ruby-sdk-sns-scenario-sending-receiving-messages:

Sending and Receiving Messages
==============================

You can send individual messages or a batch of up to 10 messages at a time.


.. _aws-ruby-sdk-sns-scenario-queues:

Using Queues
============


.. _aws-ruby-sdk-sns-scenario-dead-letter-queues:

Using Dead Letter Queues
========================



