.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-add-item-to-table:

####################################
Adding an Item to an |DDBlong| Table
####################################

.. meta::
    :description:
        Add items to Amazony DynamoDB tables using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example adds an item with the :code:`ID` value of **123456**, :code-ruby:`FirstName`
value of **John**, and :code-ruby:`LastName` value of **Doe** to the :code-ruby:`Users` table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-add-item-users-table.rb
   :dedent: 0
   :language: ruby
