.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-working-with-security-groups:

##################################
Working with |EC2| Security Groups
##################################

.. meta::
    :description:
        Learn to work with Amazon EC2 security groups using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

An |EC2| security group acts as a virtual firewall that controls the traffic for one or more instances.
You add rules to each security group to allow traffic to or from its associated instances. You can modify the rules for a security group at any time. The new rules are automatically applied to all instances that are associated with the security group.

For more information about the |EC2| security groups, see:

* `Amazon EC2 Amazon Security Groups for Linux Instances <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html>`_
* `Amazon EC2 Security Groups for Windows Instances <http://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/using-network-security.html>`_

In this example, we use the |sdk-ruby| with |EC2| to:

#. Create a security group.
#. Add rules to the security group.
#. Get information about security groups.
#. Delete the security group.

The full sample script containing all of the following examples is `available on GitHub <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/ec2/ec2-ruby-example-security-group.rb>`_.

*************
Prerequisites
*************

Before working with the code below, you need to install and configure the |sdk-ruby|. See the following:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You'll also need to `create a VPC <http://docs.aws.amazon.com/AmazonVPC/latest/GettingStartedGuide/getting-started-ipv4.html#getting-started-create-vpc>`_ and note the VPC ID.

*****************
Configure the SDK
*****************

First you need the |sdk-ruby|, and you need to create an EC2 client. Then provide a name for the security
group you'll create. You also need to provide the ID of our VPC, which is available in the console
after the VPC is created. **Be sure that you replace ``VPC-ID`` with your actual VPC ID.**

You use the ``security_group_created`` variable later in the script to determine if a security
group was created and can therefore be deleted.

***********************
Create a Security Group
***********************

Create a security group that allows access over ports 22 (SSH) and 80 (HTTP) from all addresses (CIDR
block ``0.0.0.0/0``).

If the ``begin`` block executes without exception, set ``security_group_created`` to ``true``.

**************************************
Get Information about a Security Group
**************************************

Having created a security group, you output information about your existing security groups and their IP
permissions.

***********************
Delete a Security Group
***********************

At the end of the script, assuming that you successfully created a security group and the ``security_group_created``
flag is set to ``true``, you delete the security group.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-security-group.rb
   :dedent: 0
   :language: ruby
