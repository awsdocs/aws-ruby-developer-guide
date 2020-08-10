.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-account-aliases:

############################
Managing IAM Account Aliases
############################

.. meta::
    :description:
        Learn to manage IAM account aliases using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

If you want the URL for your sign-in page to contain your company name or other friendly identifier instead
of your AWS account ID, you can create an |IAM| account alias for your AWS account ID.
If you create an |IAM| account alias, your sign-in page URL changes to incorporate the alias. For more
information about |IAM| account aliases, see :IAM-ug:`Your AWS Account ID and Its Alias <console_account-alias>`.

In this example, you use the |sdk-ruby| with |IAM| to:

#. List AWS account aliases, using :aws-ruby-iam-client-method:`list_account_aliases`.
#. Create an account alias, using :aws-ruby-iam-client-method:`create_account_alias`.
#. Delete the account alias, using :aws-ruby-iam-client-method:`delete_account_alias`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

In the example code, change the `my-account-alias` string to something that will be unique across all Amazon Web Services products.

*******
Example
*******

.. literalinclude:: ./example_code/iam/iam-ruby-example-account-alias.rb
   :dedent: 0
   :language: ruby
