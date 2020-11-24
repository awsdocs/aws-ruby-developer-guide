.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cw-example-sending-events:

###########################
Sending Events to |CWElong|
###########################

.. meta::
   :description: Send events to Amazon CloudWatch Events using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, CloudWatch Events

The following code example shows how to create and trigger a rule in |CWElong|. This rule sends a notification to the specified
topic in |SNSlong| (|SNS|) whenever an available instance in |EC2long| (|EC2|) changes to a running state. Also, related event
information is logged to a log group in |CWE|.

.. literalinclude:: ./example_code/cloudwatch/cw-ruby-example-send-events-ec2.rb
   :dedent: 0
   :language: ruby
