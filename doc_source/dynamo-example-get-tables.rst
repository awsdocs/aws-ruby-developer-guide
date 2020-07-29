.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-get-tables:

##############################################
Getting Information about All |DDBlong| Tables
##############################################

.. meta::
    :description:
        Get Amazon DynamoDB table information using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example lists the names and number of items in each table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./dynamodb/dynamodb-ruby-example-show-tables-names-and-item-count.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby
