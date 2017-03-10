.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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
   :description:
   :keywords: AWS SDK for Ruby code examples

|CWE| delivers a near real-time stream of system events that describe changes in Amazon Web Services (AWS) resources to AWS Lambda functions or other targets. To learn more, see :CWE-dg:`What is Amazon CloudWatch Events? <WhatIsCloudWatchEvents>`.

In this example, you use the |sdk-ruby| with |CWE| to:

#. Create a rule in Amazon CloudWatch Events by using :aws-ruby-cwe-client-method:`put_rule`.
#. Add a target to the rule by using :aws-ruby-cwe-client-method:`put_targets`.
#. Send an event to Amazon CloudWatch Events so that it can be matched to the rule.
#. View the results in Amazon CloudWatch Metrics and Logs by using :aws-ruby-cw-client-method:`get_metric_statistics` and :aws-ruby-cwl-client-method:`describe_log_streams`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You will also need to:

#. Replace the placeholder value assigned to `lambda_function_arn` with an actual AWS Lambda function ARN.
#. Replace the placeholder value assigned to `cwe_service_role_arn` with an appropriate AWS IAM service role ARN.
#. Replace the placeholder value assigned to `instance_id` with an actual EC2 instance ID.

For details, see the comments in the `example code on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cw/cw-ruby-example-send-events-ec2.rb>`_.

*******
Example
*******

.. literalinclude:: ./example_code/cw/cw-ruby-example-send-events-ec2.rb
   :lines: 68-189
   :dedent: 0
   :language: ruby
