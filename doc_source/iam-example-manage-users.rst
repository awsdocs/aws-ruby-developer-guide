.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-manage-users:

####################
Managing |IAM| Users
####################

.. meta::
    :description:
        Learn to manage IAM users with this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

An |IAM| user represents a person or service that interacts with AWS. For more information about |IAM| users, see :IAM-ug:`IAM Users <id_users>`.

In this example, you use the |sdk-ruby| with |IAM| to:

#. Get information about available AWS |IAM| users by using :aws-ruby-iam-client-method:`list_users`.
#. Create a user by using :aws-ruby-iam-client-method:`create_user`.
#. Update the user's name by using :aws-ruby-iam-client-method:`update_user`.
#. Delete the user by using :aws-ruby-iam-client-method:`delete_user`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

*******
Example
*******

.. literalinclude:: ./example_code/iam/iam-ruby-example-manage-users.rb
   :dedent: 0
   :language: ruby
