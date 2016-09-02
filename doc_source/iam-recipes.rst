.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-recipes:

#################
|IAMlong| Recipes
#################

This section provides recipes you can use to access |IAMlong| (|IAM|) using the |sdk-ruby|. For more
information about |IAM|, see the `IAM documentation <http://aws.amazon.com/documentation/iam/>`_.

This section contains the following recipes:

* :ref:`aws-ruby-sdk-iam-recipe-get-users`

* :ref:`aws-ruby-sdk-iam-recipe-add-user`

* :ref:`aws-ruby-sdk-iam-recipe-create-user-access-keys`

* :ref:`aws-ruby-sdk-iam-recipe-add-managed-policy`

* :ref:`aws-ruby-sdk-iam-recipe-create-role`

.. _aws-ruby-sdk-iam-recipe-get-users:

Getting Information about all Users
===================================

The following example lists the groups, policies, and and access key IDs of all of IAM users in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/iam/iam-ruby-example-list-all-users.rb
   :lines: 13-37
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-iam-recipe-add-user:

Adding a new User
=================

The following example creates the IAM user :code:`my_groovy_user` in the region :code:`us-west-2` with the password :code:`REPLACE_ME`,
and displays the user's account ID. If a user with that name already exists, it displays a message and does not create a new user.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/iam/iam-ruby-example-add-new-user.rb
   :lines: 13-27
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-iam-recipe-create-user-access-keys:

Create User's Access Keys
=========================

The following example creates a new access key and secret key for the IAM user :code:`my_groovy_user` in the region :code-:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/iam/iam-ruby-example-create-user-access-keys.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-iam-recipe-add-managed-policy:

Adding a Managed Policy
=======================

The following example adds the managed policy :code:`AmazonS3FullAccess` to the IAM user :code:`my_groovy_user in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/iam/iam-ruby-example-add-managed-policy.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-iam-recipe-create-role:

Creating a Role
===============

The following example creates the role :code:`my_groovy_role` so that |EC2| can access |S3| and |DDB| in the region :code:`us-west-2`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/iam/iam-ruby-example-create-role.rb
   :lines: 13-44
   :dedent: 0
   :language: ruby
