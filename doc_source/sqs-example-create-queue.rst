.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-create-queue:

#########################
Creating a Queue in |SQS|
#########################

.. meta::
    :description:
        Create an Amazon SQS queue using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, SQS

The following example creates the |SQS| queue named :code:`MyGroovyQueue` in the :code:`us-west-2` region
and displays its URL.

.. literalinclude:: ./sqs/sqs-ruby-example-create-queue.rb
   :lines: 13-19
   :dedent: 0
   :language: ruby
