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

The following code example demonstrates how to:

#. List access keys for a user in |IAMlong| (|IAM|).
#. Create an access key for a user.
#. Determine when a user's access keys were last used.
#. Deactivate an access key for a user.
#. Delete an access key for a user.

.. literalinclude:: ./example_code/iam/iam-ruby-example-access-keys.rb
   :dedent: 0
   :language: ruby
