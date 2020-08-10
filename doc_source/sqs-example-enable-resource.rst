.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-enable-resource:

##################################################
Enabling a Resource to Publish to a Queue in |SQS|
##################################################

.. meta::
   :description: Enable resources to publish to Amazon SQS queues using this AWS SDK for Ruby.
   :keywords: AWS SDK for Ruby code examples, SQS

The following example enables the resource with the ARN :code:`my-resource-arn` to publish to the
queue with the ARN :code:`my-queue-arn` and URL :code:`my-queue-url` in the :code:`us-west-2`
region.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-enable-resource.rb
   :dedent: 0
   :language: ruby
