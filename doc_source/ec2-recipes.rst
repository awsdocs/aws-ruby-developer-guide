.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-recipes:

#############
|EC2| Recipes
#############

This section provides recipes you can use to access |EC2long| (|EC2|) using the |sdk-ruby|. For more
information about |EC2|, see the `Amazon EC2 Documentation <http://aws.amazon.com/documentation/ec2/>`_.

This section contains the following recipes:

* :ref:`aws-ruby-sdk-ec2-create-vpc`

* :ref:`aws-ruby-sdk-ec2-attach-igw-vpc`

* :ref:`aws-ruby-sdk-ec2-create-subnet`

* :ref:`aws-ruby-sdk-ec2-create-route-table`

* :ref:`aws-ruby-sdk-ec2-create-security-group`

* :ref:`aws-ruby-sdk-ec2-create-key-pair`

* :ref:`aws-ruby-sdk-ec2-recipe-get-instances`

* :ref:`aws-ruby-sdk-ec2-recipe-get-instance-by-tag`

* :ref:`aws-ruby-sdk-ec2-recipe-get-instance`

* :ref:`aws-ruby-sdk-ec2-recipe-create-instance`

* :ref:`aws-ruby-sdk-ec2-recipe-stop-instance`

* :ref:`aws-ruby-sdk-ec2-recipe-start-instance`

* :ref:`aws-ruby-sdk-ec2-recipe-reboot-instance`

* :ref:`aws-ruby-sdk-ec2-recipe-terminate-instance`

.. _aws-ruby-sdk-ec2-create-vpc:

Creating a Virtual Private Cloud (VPC)
======================================

The following example creates the VPC :code:`MyGroovyVPC` with the CIDR block :code:`10.200.0.0/16` and displays its ID.
This example creates a virtual network with 65,536 private IP addresses.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-vpc.rb
   :lines: 13-31
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-attach-igw-vpc:

Creating an Internet Gateway and attaching it to a VPC
======================================================

The following example creates the internet gateway :code:`MyGroovyIGW`, attaches it to the VPC with ID :code:`VPC_ID`, and displays its ID.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-attach-igw-vpc.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-subnet:

Creating a Public Subnet
========================

The following example creates the public subnet :code:`MyGroovySubnet` in the region :code:`us-west-2`,
and the availablity zone :code:`us-west-2a`,
attaches it to the VPC with the ID :code:`VPC_ID` using the CIDR block of :code:`10.200.10.0/24`,
and displays its ID
The example creates a subnet of 256 private IP addresses within the VPC.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-subnet.rb
   :lines: 13-24
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-route-table:

Creating a Route Table and associating it with a Subnet
=======================================================

The following example creates the route table :code:`MyGroovyRouteTable` in region :code:`us-west-2`, the VPC with the ID :code;`VPC_ID`,
the route with the CIDR block :code:`0.0.0.0/0` and the gateway with the ID :code:`IGW_ID`,
associates it with the subnet with the ID :code:`SUBNET_ID`, and displays its ID.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-route-table.rb
   :lines: 13-32
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-security-group:

Creating a Security Group
=========================

The following example creates the security group :code:`MyGroovySecurityGroup` in the region :code:`us-west-2`, the VPC with the ID :code:`VPC_ID`,
allows access over port 22 (SSH) from all addresses (CIDR block :code:`0.0.0.0/0`),
gives it the description "Security group for MyGroovyInstance", and displays its ID.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-security-group.rb
   :lines: 13-33
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-key-pair:

Creating a Key-Pair
===================

The following example creates an unencrypted, PEM-encoded RSA private key in your home folder as :file:`MyGroovyKeyPair.pem`.
You need a key pair when you connect to your Amazon EC2 instance.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-key-pair.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instances:

Getting Information about All Instances
=======================================

The following example lists the IDs and state (pending, running, shutting down, terminated, stopping, or stopped)
of all of your EC2 instances in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-get-all-instance-info.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instance-by-tag:

Getting Information about All Instances with a Specific Tag Value
=================================================================

The following example lists the ID and state (pending, running, shutting down, terminated, stopping, or stopped)
of the EC2 instance with the tag :code:`Group` and tag value :code:`MyGroovyGroup` in the region :code:`us-west-2`.
Note that both the tag name and value are case-sensitive.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-get-instance-info-by-tag.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instance:

Getting Information about a Specific Instance
=============================================

The following example lists the state of the instance :code:`i-123abc` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-list-state-instance-i-123abc.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-create-instance:

Creating an Instance
====================

The following example creates the EC2 instance :code:`MyGroovyInstance` with the tag :code:`Group` and value :code:`MyGroovyGroup`
in the availability zone :code:`us-west-2a` with the machine image :code:`MACHINE_IMAGE` for the account with ID :code:`ACCOUNT_ID`,
the security group with the ID :code:`SECURITY_GROUP_ID`, the subnet with the ID :code:`SUBNET_ID`, and displays its public DNS and IP address.
Note the empty script value. You can add instructions here that your EC2 instance executes when it starts.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-instance.rb
   :lines: 13-50
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-stop-instance:

Stopping an Instance
====================

The following example stops the instance :code:`i-123abc` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-stop-instance-i-123abc.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-start-instance:

Starting an Instance
====================

The following example starts the instance :code:`i-123abc` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-start-instance-i-123abc.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-reboot-instance:

Rebooting an Instance
=====================

The following example reboots the instance :code:`i-123abc` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-reboot-instance-i-123abc.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-terminate-instance:

Terminating an Instance
=======================

The following example terminates the instance :code:`i-123abc` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-terminate-instance-i-123abc.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby
