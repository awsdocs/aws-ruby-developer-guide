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

* Replace the placeholder value assigned to `lambda_function_arn` with an actual AWS Lambda function ARN.

  #. Create a Lambda function, as described `here <http://docs.aws.amazon.com/AmazonCloudWatch/latest/events/LogEC2InstanceState.html#ec2-create-lambda-function>`_.
  #. Name the function `LogEC2InstanceStateChange`.
  #. For a Role, select **Choose an Existing Role**; for the existing role, select **lambda_basic_execution**.
  #. After you've created the function, copy the ARN and paste it into your code.

* Replace the placeholder value assigned to `cwe_service_role_arn` with an appropriate AWS IAM service role ARN.

  #. In the |IAM| console, create a role and attach a policy that grants full access to CloudWatch Events.
  #. Ensure that the role has a trust relationship to `events.amazonaws.com`. For an example policy and role, see the comments in the `example code on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cw/cw-ruby-example-send-events-ec2.rb>`_.
  #. After you've created the role, attached the policy, and established the trust relationship, copy the role ARN and paste it into your code.

* Replace the placeholder value assigned to `instance_id` with an actual EC2 instance ID.

*******
Example
*******

.. literalinclude:: ./example_code/cw/cw-ruby-example-send-events-ec2.rb
   :lines: 68-189
   :dedent: 0
   :language: ruby
