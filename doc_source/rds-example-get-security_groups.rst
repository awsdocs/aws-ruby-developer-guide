.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-rds-example-get-security_groups:

###################################################
Getting Information about All |RDS| Security Groups
###################################################

.. meta::
    :description:
        Get information about Amazon RDS security groups using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, RDS

The following example lists the names of all of your |RDS| security groups in the :code:`us-west-2` region.

.. note:: |RDS| security groups are only applicable when you are using the |EC2|-Classic platform.
   If you are using |EC2|-VPC, use VPC security groups. Both are shown in the example.

.. literalinclude:: ./example_code/rds/rds-ruby-example-list-security-groups.rb
   :dedent: 0
   :language: ruby
