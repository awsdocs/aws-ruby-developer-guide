.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-poll-messages:

#######################################################
Receiving Messages Using the QueuePoller Class in |SQS|
#######################################################

.. meta::
   :description:
        Receive messages using the Amazon SQS QueuePoller class with this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, SQS

The following example uses the :code:`QueuePoller` utility class to display the body of all messages
in the |SQS| queue with the URL :code:`URL` in the :code:`us-west-2` region, and deletes the message.
After approximately 15 seconds of inactivity, the script times out.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-poll-messages.rb
   :dedent: 0
   :language: ruby

The following example loops through the |SQS| queue with the URL :code:`URL`, and waits up to *duration* seconds.

You can get the correct URL by executing the |SQS| example in :ref:`aws-ruby-sdk-sqs-example-show-queues`.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-long-polling.rb
   :dedent: 0
   :language: ruby

The following example loops through the |SQS| queue with the URL :code:`URL`, and gives you up to
the visibility *timeout* seconds to process the message, represented by the method
:code:`do_something`.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-visibility-timeout.rb
   :dedent: 0
   :language: ruby

The following example loops through the |SQS| queue with the URL :code:`URL`, and changes the
visibility *timeout* seconds, for any message that needs additional processing by the method
:code:`do_something2`.

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-visibility-timeout2.rb
   :dedent: 0
   :language: ruby
