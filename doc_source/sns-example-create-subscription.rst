.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sns-example-create-subscription:

#########################################
Creating a Subscription in an |SNS| Topic
#########################################

.. meta::
    :description:
        Create a subscription in an Amazon SNS topic using the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby code examples, SNS

The following example creates a subscription for the topic with the ARN
:code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic` for a user who has the email address
:code:`MyGroovyUser@MyGroovy.com` in the :code:`us-west-2` region, and displays the resulting ARN.
Initially the ARN value is pending confirmation. When the user confirms their email address, this
value becomes a true ARN.

.. literalinclude:: ./example_code/sns/sns-ruby-example-create-subscription.rb
   :dedent: 0
   :language: ruby
