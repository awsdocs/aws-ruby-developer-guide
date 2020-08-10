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

An Elastic IP address is a static IP address, designed for dynamic cloud computing, that is
associated with your AWS account. It's a public IP address, which is reachable from the internet.
If your instance doesn't have a public IP address, you can use an Elastic IP address with your instance
so that it can communicate with the internet.

For more information about Elastic IP addresses in |EC2|, see :EC2-ug:`Elastic IP Addresses <elastic-ip-addresses-eip>`
in the |EC2-ug| or :EC2-ug-win:`Elastic IP Addresses <elastic-ip-addresses-eip>`
in the |EC2-ug-win|.

In this example, you use the |sdk-ruby| with |EC2| to:

#. Allocate an Elastic IP address by using the
   `Aws::EC2::Client#allocate_address <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/EC2/Client.html#allocate_address-instance_method>`_
   method.
#. Associate the address with an |EC2| instance by using the
   `Aws::EC2::Client#associate_address <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/EC2/Client.html#associate_address-instance_method>`_ method.
#. Get information about addresses associated with the instance by using the
   `Aws::EC2::Client#describe_addresses <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/EC2/Client.html#describe_addresses-instance_method>`_ method.
#. Release the address by using the
   `Aws::EC2::Client#release_address <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/EC2/Client.html#release_address-instance_method>`_ method.

The `complete code <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/ec2/ec2-ruby-example-elastic-ips.rb>`_
for this example is available on GitHub.

*************
Prerequisites
*************

Before working with the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You also need to :EC2-ug:`launch an EC2 instance <ec2-launch-instance_linux>`
and note the instance ID.

.. note:: Before you run the following code, you must replace the ``INSTANCE-ID`` string with
          your actual instance ID. This will be something like ``i-0a123456b7c8defg9``.

*******
Example
*******

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-elastic-ips.rb
   :dedent: 0
   :language: ruby
