.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cw-example-create_alarm:

##########################
Creating an |CWlong| Alarm
##########################

.. meta::
    :description:
        Create Amazon CloudWatch alarms using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, CloudWatch alarms

The following example creates a |CW| alarm named *my-alarm* that sends a message through the |SNS| topic
with the ARN named :code:`ARN`
when the |S3| bucket named *my-bucket* has more than 50 items in a 24-hour period.

.. literalinclude:: ./example_code/cloudwatch/cw-ruby-example-create-alarm.rb
   :dedent: 0
   :language: ruby

See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/cloudwatch/cw-ruby-example-create-alarm.rb>`_
on GitHub.
