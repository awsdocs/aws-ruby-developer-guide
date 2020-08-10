.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-get-messages:

###########################
Receiving Messages in |SQS|
###########################

.. meta::
   :description: Receive messages in Amazon SQS using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, SQS

The following example displays the body of up to 10 messages in the |SQS| queue with the URL
:code:`URL` in the :code:`us-west-2` region.

.. note:: :code:`receive_message` does not guarantee to get all messages (see `Properties of
   Distributed Queues
   <http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/DistributedQueues.html>`_),
   and by default does not delete the message.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-get-messages.rb
   :dedent: 0
   :language: ruby
