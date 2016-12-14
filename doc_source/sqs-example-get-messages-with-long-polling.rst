.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-sqs-example-get-messages-with-long-polling:

#####################################
Receiving Messages Using Long Polling
#####################################

The following example waits up to 10 seconds to display the bodies of up to 10 messages in the |SQS|
queue with the URL :code:`URL` in the :code:`us-west-2` region.

If you do not specify a wait time, the default value is **0** (|SQS| does not wait).

.. literalinclude:: ./example_code/sqs/sqs-ruby-example-get-messages-with-long-polling.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby