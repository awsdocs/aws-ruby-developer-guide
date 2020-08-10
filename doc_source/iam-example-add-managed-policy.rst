.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-add-managed-policy:

########################################
Adding a Managed Policy to an |IAM| User
########################################

.. meta::
    :description:
        Learn to add a managed poligy to an IAM user with this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following example adds the managed policy :code:`AmazonS3FullAccess` to the |IAM| user :code:`my_groovy_user` in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/iam/iam-ruby-example-add-managed-policy.rb
   :dedent: 0
   :language: ruby
