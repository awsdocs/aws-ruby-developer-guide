.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-create-role:

######################
Creating an |IAM| Role
######################

.. meta::
    :description:
        Create an IAM role using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following example creates the role :code:`my_groovy_role` so that |EC2| can access |S3| and |DDBlong| in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/iam/iam-ruby-example-create-role.rb
   :dedent: 0
   :language: ruby
