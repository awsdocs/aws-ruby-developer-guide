.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-create-index:

########################################
Creating an Index for an |DDBlong| Table
########################################

.. meta::
    :description:
        Create an index for an Amazon DynamoDB table using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example adds a new index, :code-ruby:`air-mileage-index`, to the :code-ruby:`Users`
table in the :code-ruby:`us-west-2` region.  Once the status of the index is :code-ruby:`ACTIVE`,
you can search for items in the table based on the value of their :code-ruby:`airmiles`.

.. literalinclude:: ./dynamodb/dynamodb-ruby-example-add-index.rb
   :lines: 13-47
   :dedent: 0
   :language: ruby
