.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-rds-example-get-snapshots:

#######################################
Getting Information about All Snapshots
#######################################

The following example lists the names (IDs) and status of all of your |RDS| (instance) snapshots in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/rds/rds-ruby-example-list-instance-snapshots.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby