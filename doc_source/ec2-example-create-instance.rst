.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-example-create-instance:

##########################
Creating an |EC2| Instance
##########################

.. meta::
    :description:
        Create Amazon EC2 instances using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following example creates an |EC2| instance :code:`MyGroovyInstance`, with the tag :code:`Group` and value :code:`MyGroovyGroup`. The instance is created
in Availability Zone :code:`us-west-2a`. The instance has the machine image :code:`MACHINE_IMAGE`
for the account with ID :code:`ACCOUNT_ID`,
the security group with the ID :code:`SECURITY_GROUP_ID`, and the subnet
with the ID :code:`SUBNET_ID`. Then it displays the instance's ID and public IP address.

.. note:: In the empty script value, you can add instructions that your |EC2| instance executes when it starts.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-create-instance.rb
   :dedent: 0
   :language: ruby
