.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cw-example-alarm-actions:

#############################################
Enabling and Disabling |CWlong| Alarm Actions
#############################################

.. meta::
   :description: Enable and disable Amazon CloudWatch alarm actions using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, CloudWatch alarms

The following code example:

#. Creates and enables a new |CW| alarm (or updates an existing alarm, if an alarm with the specified name already exists). 
#. Disables the new or existing alarm. To enable the alarm again, call ``enable_alarm_actions``.

.. literalinclude:: ./example_code/cloudwatch/cw-ruby-example-alarm-actions.rb
   :dedent: 0
   :language: ruby
