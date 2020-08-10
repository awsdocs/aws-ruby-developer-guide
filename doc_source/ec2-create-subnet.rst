.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-create-subnet:

##################################
Creating a Public Subnet for |EC2|
##################################

.. meta::
    :description:
        Create public subnets for Amazon EC2 using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following example creates a public subnet :code:`MyGroovySubnet` in the :code:`us-west-2` region
and the Availablity Zone :code:`us-west-2a`. The example attaches the public subnet to a VPC with the ID :code:`VPC_ID` that uses the CIDR block :code:`10.200.10.0/24`, and then
displays the subnet's ID.

The public subnet created in this example has 256 private IP addresses within the VPC.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-create-subnet.rb
   :dedent: 0
   :language: ruby
