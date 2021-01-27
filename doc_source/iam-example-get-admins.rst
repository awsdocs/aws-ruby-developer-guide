.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-get-admins:

##########################################
Listing |IAM| Users who are Administrators
##########################################

.. meta::
    :description:
        Get a list of the IAM users with administrator privileges with this AWS
        SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following code example determines of the users available to you in |IAMlong| (|IAM|), 
how many of them are associated with a policy that provides administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :dedent: 0
   :language: ruby