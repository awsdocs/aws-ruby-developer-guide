.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-load-table-items-from-json:

######################################################
Loading Items from a JSON File into an |DDBlong| Table
######################################################

.. meta::
    :description:
        Add the items in a JSON file to an Amazon DynamoDB table using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following code example adds items from a JSON file to a table.

.. literalinclude:: ./example_code/dynamodb/dynamodb_ruby_example_load_movies.rb
   :dedent: 0
   :language: ruby

The following JSON file example defines two of these items.

.. literalinclude:: ./example_code/dynamodb/movie_data.json
   :dedent: 0
   :language: json
