.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-create-security-group:

################################
Creating an |EC2| Security Group
################################

.. meta::
    :description:
        Create a security group for Amazon EC2 using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following example creates a security group named :code:`MyGroovySecurityGroup` in the :code:`us-west-2`
region on a VPC with the ID :code:`VPC_ID`.
In the example, the security group is allowed access over port 22 (SSH) from all addresses (CIDR block :code:`0.0.0.0/0`), and
is given the description "Security group for MyGroovyInstance". Then, the security group's ID is displayed.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-create-security-group.rb
   :dedent: 0
   :language: ruby
