.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sns-recipes:

#############
|SNS| Recipes
#############

This section provides some recipes you can use to access |SNSlong| (|SNS|) using the |sdk-ruby|. For
more information about |SNS|, see the `Amazon SNS documentation <http://aws.amazon.com/documentation/sns/>`_.

This section contains the following recipes:

* :ref:`aws-ruby-sdk-sns-recipe-show-topics`

* :ref:`aws-ruby-sdk-sns-recipe-create-topic`

* :ref:`aws-ruby-sdk-sns-recipe-show-subscriptions`

* :ref:`aws-ruby-sdk-sns-recipe-create-subscription`

* :ref:`aws-ruby-sdk-sns-recipe-send-message`

* :ref:`aws-ruby-sdk-sns-recipe-enable-resource`

.. _aws-ruby-sdk-sns-recipe-show-topics:

Getting Information about all Topics
====================================

The following example lists the ARNs of your SNS topics in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/sns-ruby-example-show-topics.rb
   :lines: 13-19
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-sns-recipe-create-topic:

Creating a new Topic
====================

The following example creates the topic :code:`MyGroovyTopic` in the region :code:`us-west-2` and displays the resulting topic ARN.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/sns-ruby-example-create-topic.rb
   :lines: 13-18
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-sns-recipe-show-subscriptions:

Getting Information about all Subscriptions in a Topic
======================================================

The following example lists the email addresses of the SNS subscriptions for the topic with the ARN
:code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/sns-ruby-example-show-subscriptions.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-sns-recipe-create-subscription:

Creating a new Subscription in a Topic
======================================

The following example creates a subscription for the topic with the ARN :code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic`
for a user with the email address :code:`MyGroovyUser@MyGroovy.com` in the region :code:`us-west-2` and displays the resulting ARN.
Note that initially the ARN value is pending confirmation. Once the user has confirmed their email address, this value becomes a true ARN.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/
   :lines: 13-
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-sns-recipe-send-message:

Sending a Message to all Topic Subscribers
==========================================

The following example sends the message "Hello!" to all of the subscribers to the topic with the ARN
:code:`arn:aws:sns:us-west-2:123456789:MyGroovyTopic`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/sns-ruby-example-send-message.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-sns-recipe-enable-resource:

Enabling a Resource to Publish to a Topic
=========================================

The following example enables the resource with the ARN
:code:`my-resource-arn` to publish to the topic with the :code:`ARN my-topic-arn` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/sns/sns-ruby-example-enable-resource.rb
   :lines: 13-38
   :dedent: 0
   :language: ruby
