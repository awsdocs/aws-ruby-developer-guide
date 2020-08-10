.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-get-users:

#####################################
Getting Information about |IAM| Users
#####################################

.. meta::
    :description:
        Get information about IAM users with this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following example lists the groups, policies, and access key IDs of the
|IAM| users in the :code:`us-west-2` region.
If there are more than 100 users, :code:`iam.list_users.IsTruncated` is **true**
and :code:`iam.list_users.Marker` contains a value you can use to get information
about additional users.
See the `Aws::IAM::Client.list_users <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/IAM/Client.html#list_users-instance_method>`_
topic for further information.

.. literalinclude:: ./example_code/iam/iam-ruby-example-list-all-users.rb
   :dedent: 0
   :language: ruby
