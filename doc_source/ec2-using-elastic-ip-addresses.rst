.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-using-elastic-ip-addresses:

###################################
Using Elastic IP Addresses in |EC2|
###################################

.. meta::
   :description: Learn to use Elastic IP addresses in Amazon EC2 using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following code example:

#. Displays information about any addresses associated with an Amazon Elastic Compute Cloud (Amazon EC2) instance.
#. Creates an Elastic IP address in Amazon Virtual Private Cloud (Amazon VPC).
#. Associates the address with the instance.
#. Displays information again about addresses associated with the instance. This time, the new address association should display.
#. Releases the address.
#. Displays information again about addresses associated with the instance. This time, the released address should not display.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-elastic-ips.rb
   :dedent: 0
   :language: ruby
