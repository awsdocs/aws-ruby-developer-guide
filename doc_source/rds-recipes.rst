.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-rds-recipes:

#################
|RDSlong| Recipes
#################

This section provides recipes you can use to access |RDSlong| (|RDS|) using the |sdk-ruby|. For more
information about |RDS|, see the `Amazon Relational Datbase Service User Guide <http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/>`_.

.. note:: Some examples in this section use methods that were introduced in the :code:`2.2.18` version of the
    :code:`Aws::RDS::Resource`class; you must use that or a later version of the :code:`aws-sdk` gem
    to run these examples.

This section contains the following recipes:

* :ref:`aws-ruby-sdk-rds-recipe-get-instances`

* :ref:`aws-ruby-sdk-rds-recipe-get-snapshots`

* :ref:`aws-ruby-sdk-rds-recipe-get-cluster-snapshots`

* :ref:`aws-ruby-sdk-rds-recipe-get-security_groups`

* :ref:`aws-ruby-sdk-rds-recipe-get-subnet-groups`

* :ref:`aws-ruby-sdk-rds-recipe-get-parameter_groups`

* :ref:`aws-ruby-sdk-rds-recipe-create-snapshot`

* :ref:`aws-ruby-sdk-rds-recipe-create-cluster-snapshot`

.. _aws-ruby-sdk-rds-recipe-get-instances:

Getting Information about all Instances
=======================================

The following example lists the name (ID) and status of all of your |RDS| instances in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-all-instances.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-get-snapshots:

Getting Information about all Snapshots
=======================================

The following example lists the names (IDs) and status of all of your |RDS| (instance) snapshots in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-instance-snapshots.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-get-cluster-snapshots:

Getting Information about all Clusters and their Snapshots
==========================================================

The following example lists the name (ID) and status of all of your |RDS| clusters
and the name (ID) and status of their snapshots in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-cluster-snapshots.rb
   :lines: 13-25
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-get-security_groups:

Getting Information about all Security Groups
=============================================

The following example lists the names of all of your |RDS| security groups in the region :code:`us-west-2`
Note that |RDS| security groups are only applicable when you are using the EC2 classic platform.
If you are using EC2 VPC, use VPC security groups. Both are shown in the example.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-security-groups.rb
   :lines: 13-35
   :dedent: 0
   :language: ruby
              
.. _aws-ruby-sdk-rds-recipe-get-subnet-groups:

Getting Information about all Subnet Groups
===========================================

The following example lists the name and status of all of your |RDS| subnet groups in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-subnet-groups.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-get-parameter_groups:

Getting Information about all Parameter Groups
==============================================

The following example lists the names and descriptions of all of your |RDS| parameter groups in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-list-parameter-groups.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-create-snapshot:

Creating a Snapshot of an Instance
==================================

The following example creates a snapshot for the |RDS| instance represented by *instance_name* in the region :code:`us-west-2`
Note that if your instance is a member of a cluster, you cannot create a snapshot of the instance, but instead must create a snapshot of the cluster (see the next recipe).

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-create-snapshot.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-rds-recipe-create-cluster-snapshot:

Creating a Snapshot of a Cluster
================================

The following example creates a snapshot for the |RDS| cluster represented by *cluster_name* in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/rds/rds-ruby-example-create-cluster-snapshot.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby
