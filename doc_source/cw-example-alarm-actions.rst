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

An |CWlong| alarm watches a single metric over a time period you specify. The |CW| alarm performs one
or more actions based on the value of the metric, relative to a given threshold over a number of time
periods. For more information, see :CW-ug:`Creating Amazon CloudWatch Alarms <AlarmThatSendsEmail>` in
the |CW-ug|.

In this example, you use the |sdk-ruby| with |CW| to:

#. Enable an action for a |CW| alarm by using `Aws::CloudWatch::Client#put_metric_alarm <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/CloudWatch/Client.html#put_metric_alarm-instance_method>`_.
#. Disable all actions for an alarm by using `Aws::CloudWatch::Client#disable_alarm_actions <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/CloudWatch/Client.html#disable_alarm_actions-instance_method>`_.

The `complete code <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/cloudwatch/cw-ruby-example-alarm-actions.rb>`_
for this example is available on GitHub.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You also need to replace `arn:aws:sns:REGION-ID:ACCOUNT-ID:TOPIC-NAME` with the ARN for a valid |SNS| topic.

*******
Example
*******

.. literalinclude:: ./example_code/cloudwatch/cw-ruby-example-alarm-actions.rb
   :dedent: 0
   :language: ruby
