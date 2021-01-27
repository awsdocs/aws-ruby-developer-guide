.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-working-with-policies:

#########################
Working with IAM Policies
#########################

.. meta::
    :description:
        Learn to work with IAM policies using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following code example demonstrates how to:

#. Create a policy in |IAMlong| (|IAM|).
#. Attach the policy to a role.
#. List the policies that are attached to the role.
#. Detach the policy from the role.

.. literalinclude:: ./example_code/iam/iam-ruby-example-manage-policies.rb
  :dedent: 0
  :language: ruby
