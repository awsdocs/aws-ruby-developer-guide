.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cw-example-get-metrics-info:

#####################################################
Getting Information about Custom Metrics for |CWlong|
#####################################################

.. meta::
   :description: Get custom metrics information for Amazon CloudWatch using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, CloudWatch

A |CW| alarm watches a single metric over a time period you specify. The |CW| alarm performs
one or more actions based on the value of the metric, relative to a given threshold over a number of time periods. For more information, see :CW-ug:`Creating Amazon CloudWatch Alarms <AlarmThatSendsEmail>`.

In this example, you use the |sdk-ruby| with |CW| to:

#. Send custom metrics to |CW| by using `Aws::CloudWatch::Client#put_metric_data <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/CloudWatch/Client.html#put_metric_data-instance_method>`_.
#. Get information about custom metrics by using `Aws::CloudWatch::Client#list_metrics-instance <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/CloudWatch/Client.html#list_metrics-instance_method>`_.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

*******
Example
*******

.. literalinclude:: ./example_code/cloudwatch/cw-ruby-example-metrics-basics.rb
   :dedent: 0
   :language: ruby
