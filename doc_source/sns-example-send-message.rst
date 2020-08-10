.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sns-example-send-message:

################################################
Sending a Message to All |SNS| Topic Subscribers
################################################

.. meta::
    :description:
        Send messages to all Amazon SNS topic subscribers using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, SNS

The following example sends the message "Hello!" to all subscribers to the |SNS| topic with the ARN
:code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic`.

.. literalinclude:: ./example_code/sns/sns-ruby-example-send-message.rb
   :dedent: 0
   :language: ruby
