.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-rds-example-create-snapshot:

########################################
Creating a Snapshot of an |RDS| Instance
########################################

.. meta::
    :description:
        Create snapshots of Amazon RDS instances using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example creates a snapshot for the |RDS| instance represented by *instance_name* in the :code:`us-west-2` region.

.. note:: If your instance is a member of a cluster, you can't create a snapshot of the instance.
     Instead, you must create a snapshot of the cluster (see :ref:`aws-ruby-sdk-rds-example-create-cluster-snapshot`).

.. literalinclude:: ./example_code/rds/rds-ruby-example-create-snapshot.rb
   :dedent: 0
   :language: ruby
