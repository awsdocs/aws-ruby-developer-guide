.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-manage-access-keys:

########################
Managing IAM Access Keys
########################

.. meta::
    :description:
        Learn to manage IAM access keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

Users need their own access keys to make programmatic calls to AWS from the |sdk-ruby|. To fill this need,
you can create, modify, view, or rotate access keys (access key IDs and secret access keys) for |IAM|
users. By default, when you create an access key, its status is Active. This means the user can use the
access key for API calls. For more information about access keys, see :IAM-ug:`Managing Access Keys for IAM Users <id_credentials_access-keys>`.

In this example, you use the |sdk-ruby| with |IAM| to:

#. List AWS IAM user access keys, using :aws-ruby-iam-client-method:`list_access_keys`.
#. Create an access key, using :aws-ruby-iam-client-method:`create_access_key`.
#. Determine when access keys were last used, using :aws-ruby-iam-client-method:`get_access_key_last_used`.
#. Deactivate access keys, using :aws-ruby-iam-client-method:`update_access_key`.
#. Delete the access key, using :aws-ruby-iam-client-method:`delete_access_key`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You will also need to create the user (`my-user`) specified in the script. You can create a new IAM user in the IAM console or programmatically, as shown at :ref:`aws-ruby-sdk-iam-example-add-user`.

*******
Example
*******

.. literalinclude:: ./example_code/iam/iam-ruby-example-access-keys.rb
   :dedent: 0
   :language: ruby
