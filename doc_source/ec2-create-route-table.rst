.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-create-route-table:

##############################################################
Creating an |EC2| Route Table and Associating It with a Subnet
##############################################################

.. meta::
    :description:
        Create an Amazon EC2 route table using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following example creates a route table named :code:`MyGroovyRouteTable` in :code:`us-west-2` region
on a VPC with the ID :code:`VPC_ID`.
The route table uses the route with the CIDR block :code:`0.0.0.0/0`, and the gateway with the ID :code:`IGW_ID`.
The example associates the route table with the subnet that has ID :code:`SUBNET_ID`, and then displays the route table's ID.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-create-route-table.rb
   :dedent: 0
   :language: ruby
