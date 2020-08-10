.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-read-table-item:

#####################################
Reading an Item in an |DDBlong| Table
#####################################

.. meta::
    :description:
        Display information about an item in an Amazon DynamoDB tables using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example displays information about the item with the :code:`year` **2015** and
:code-ruby:`title`  **The Big New Movie** in the :code-ruby:`Movies` table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb_ruby_example_read_movies_item.rb
   :dedent: 0
   :language: ruby

See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/dynamodb/dynamodb_ruby_example_read_movies_item.rb>`_
on GitHub.
