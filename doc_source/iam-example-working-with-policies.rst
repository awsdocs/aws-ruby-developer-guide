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

An |IAM| policy is a document that specifies one or more permissions. For more information about IAM policies, see :IAM-ug:`Overview of IAM Policies <access_policies>`.

In this example, you use the |sdk-ruby| with |IAM| to:

#. Create a policy, using :aws-ruby-iam-client-method:`create_policy`.
#. Get information about the policy, using :aws-ruby-iam-client-method:`get_policy`.
#. Attach the policy to a role, using :aws-ruby-iam-client-method:`attach_role_policy`.
#. List policies attached to the role, using :aws-ruby-iam-client-method:`list_attached_role_policies`.
#. Detach the policy from the role, using :aws-ruby-iam-client-method:`detach_role_policy`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You will also need to create the role (`my-role`) specified in the script. You can do this in the |IAM| console.

*******
Example
*******

.. literalinclude:: ./example_code/iam/iam-ruby-example-manage-policies.rb
  :dedent: 0
  :language: ruby
