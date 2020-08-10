.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sns-example-show-subscriptions:

#############################################################
Getting Information about All Subscriptions in an |SNS| Topic
#############################################################

.. meta::
    :description:
        Get information about all Amazon SNS topic subscriptions using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, SNS

The following example lists the email addresses of the |SNS| subscriptions for the topic with the ARN
:code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic` in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/sns/sns-ruby-example-show-subscriptions.rb
   :dedent: 0
   :language: ruby
