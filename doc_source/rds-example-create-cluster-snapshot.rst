.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-rds-example-create-cluster-snapshot:

#######################################
Creating a Snapshot of an |RDS| Cluster
#######################################

.. meta::
    :description:
        Create snapshots of Amazon RDS clusters using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, RDS

The following example creates a snapshot for the |RDS| cluster represented by *cluster_name* in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/rds/rds-ruby-example-create-cluster-snapshot.rb
   :dedent: 0
   :language: ruby
