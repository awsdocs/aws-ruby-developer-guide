.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-using-elastic-ip-addresses:

########################################
Using Elastic IP Addresses in Amazon EC2
########################################

An Elastic IP address is a static IP address designed for dynamic cloud computing. An Elastic IP address is associated with your AWS account. It is a public IP address, which is reachable from the Internet. If your instance does not have a public IP address, you can associate an Elastic IP address with your instance to enable communication with the Internet.

For more information about Elastic IP addresses in Amazon EC2, see `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html>`_ in the Amazon EC2 User Guide for Linux Instances or `Elastic IP Addresses <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/elastic-ip-addresses-eip.html>`_ in the Amazon EC2 User Guide for Windows Instances.

In this example, we use the |sdk-ruby| with |EC2| to:

#. Allocate an Elastic IP address, using `Aws::EC2::Client#allocate_address <https://docs.aws.amazon.com/sdkforruby/api/Aws/EC2/Client.html#allocate_address-instance_method>`_.
#. Associate the address with an Amazon EC2 instance, using `Aws::EC2::Client#associate_address <https://docs.aws.amazon.com/sdkforruby/api/Aws/EC2/Client.html#associate_address-instance_method>`_.
#. Get information about addresses associated with the instance, using `Aws::EC2::Client#describe_addresses <https://docs.aws.amazon.com/sdkforruby/api/Aws/EC2/Client.html#describe_addresses-instance_method>`_.
#. Release the address, using `Aws::EC2::Client#release_address <https://docs.aws.amazon.com/sdkforruby/api/Aws/EC2/Client.html#release_address-instance_method>`_.

The full sample script is `available on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/ec2/ec2-ruby-example-elastic-ips.rb>`_.

*************
Prerequisites
*************

Before working with the code below, you need to install and configure the |sdk-ruby|, as described in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You'll also need to `launch an EC2 instance <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance_linux>`_ and note the instance ID. **NOTE:** Before running the code below, you'll need to replace the ``INSTANCE-ID`` string with your actual instance ID, which will be something like ``i-0a123456b7c8defg9``.

**************
Example Script
**************

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-elastic-ips.rb
   :lines: 19-74
   :dedent: 0
   :language: ruby
