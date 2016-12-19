.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cw-example-create_alarm:
            
#################
Creating an Alarm
#################

The following example creates a |CW| alarm *my-alarm* that sends a message through the |SNS| topic with the ARN :code:`ARN`
when the |S3| bucket *my-bucket* has more than 50 items in a 24-hour period.

.. literalinclude:: ./example_code/cw/cw-ruby-example-create-alarm.rb
   :lines: 13-52
   :dedent: 0
   :language: ruby