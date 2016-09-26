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

You can use the following recipes to access |EC2long| (|EC2|) using the |sdk-ruby|. For more information about |EC2|, see the `Amazon EC2 Documentation <http://aws.amazon.com/documentation/ec2/>`_.

**Recipes**

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

Creating a VPC
======================================

The following example creates the virtual private cloud (VPC) :code:`MyGroovyVPC` with the CIDR block :code:`10.200.0.0/16`, and then displays the VPC's ID.

The example creates a virtual network with 65,536 private IP addresses.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-vpc.rb
   :lines: 13-31
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-attach-igw-vpc:

Creating an Internet Gateway and Attaching It to a VPC
======================================================

The following example creates an Internet gateway :code:`MyGroovyIGW`, attaches it to a VPC that has ID :code:`VPC_ID`, and then displays the Internet gateway's ID.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-attach-igw-vpc.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-subnet:

Creating a Public Subnet
========================

The following example creates a public subnet :code:`MyGroovySubnet` in the :code:`us-west-2` region
and the Availablity Zone :code:`us-west-2a`. The example attaches the public subnet to a VPC with the ID :code:`VPC_ID` that uses the CIDR block :code:`10.200.10.0/24`, and then 
displays the subnet's ID.

The public subnet created in this example has 256 private IP addresses within the VPC.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-subnet.rb
   :lines: 13-24
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-route-table:

Creating a Route Table and Associating It with a Subnet
=======================================================

The following example creates a route table :code:`MyGroovyRouteTable` in :code:`us-west-2` region on a VPC with the ID :code;`VPC_ID`.
The route table uses the route with the CIDR block :code:`0.0.0.0/0` and the gateway with the ID :code:`IGW_ID`.
The example associates the route table with the subnet that has ID :code:`SUBNET_ID`, and then displays the route table's ID.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-route-table.rb
   :lines: 13-32
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-security-group:

Creating a Security Group
=========================

The following example creates a security group :code:`MyGroovySecurityGroup` in the :code:`us-west-2` region on a VPC with the ID :code:`VPC_ID`.
In the example, the security group is allowed access over port 22 (SSH) from all addresses (CIDR block :code:`0.0.0.0/0`) and
is given the description "Security group for MyGroovyInstance". Then, the security group's ID is displayed.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-security-group.rb
   :lines: 13-33
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-create-key-pair:

Creating a Key Pair
===================

You need a key pair when you connect to your |EC2| instance. The following example creates an unencrypted, PEM-encoded RSA private key :file:`MyGroovyKeyPair.pem` in your home folder.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-key-pair.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instances:

Getting Information about All Instances
=======================================

The following example lists the IDs and states (pending, running, shutting down, terminated, stopping, or stopped)
for all of your |EC2| instances in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-get-all-instance-info.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instance-by-tag:

Getting Information about All Instances with a Specific Tag Value
=================================================================

The following example lists the ID and state (pending, running, shutting down, terminated, stopping, or stopped)
of an |EC2| instance with the tag :code:`Group` and tag value :code:`MyGroovyGroup` in the :code:`us-west-2` region.

.. note:: The tag name and value are case-sensitive.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-get-instance-info-by-tag.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-get-instance:

Getting Information about a Specific Instance
=============================================

The following example lists the state of an instance :code:`i-123abc` in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-list-state-instance-i-123abc.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-create-instance:

Creating an Instance
====================

The following example creates an |EC2| instance :code:`MyGroovyInstance`, with the tag :code:`Group` and value :code:`MyGroovyGroup`. The instance is created
in Availability Zone :code:`us-west-2a` with the machine image :code:`MACHINE_IMAGE` for the account with ID :code:`ACCOUNT_ID`,
the security group with the ID :code:`SECURITY_GROUP_ID`, and the subnet with the ID :code:`SUBNET_ID`. Then, it displays the instance's public DNS and IP address.

.. note:: In the empty script value, you can add instructions that your |EC2| instance executes when it starts.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-create-instance.rb
   :lines: 13-50
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-stop-instance:

Stopping an Instance
====================

The following example stops the instance :code:`i-123abc` in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-stop-instance-i-123abc.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-start-instance:

Starting an Instance
====================

The following example starts the instance :code:`i-123abc` in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-start-instance-i-123abc.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-reboot-instance:

Rebooting an Instance
=====================

The following example reboots the instance :code:`i-123abc` in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-reboot-instance-i-123abc.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-ec2-recipe-terminate-instance:

Terminating an Instance
=======================

The following example terminates the instance :code:`i-123abc` in the :code:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/ec2/ec2-ruby-example-terminate-instance-i-123abc.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby
