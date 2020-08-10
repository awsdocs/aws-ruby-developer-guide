.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-get-table-item:

###############################################################
Getting Information about a Specific Item in an |DDBlong| Table
###############################################################

.. meta::
    :description:
        Get information about a specific item in an Amazon DynamoDB table using this AWS SDK for Ruby
        code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example displays the first and last name of an item with an :code-ruby:`ID` of
**123456** in the :code-ruby:`Users` table in the :code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-list-item-123456-users-table.rb
   :dedent: 0
   :language: ruby
