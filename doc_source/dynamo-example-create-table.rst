.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-create-table:

###########################
Creating an |DDBlong| Table
###########################

.. meta::
    :description:
        Create a DynamoDB table using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example creates the table :code-ruby:`Movies` with two required
attributes: :code-ruby:`year` and :code-ruby:`title` in the :code-ruby:`us-west-2` region.

The :code-ruby:`wait_until` call blocks you from using the table until
|DDB| has created it.
By default, the |DDB| client's :code-ruby:`wait_until` method checks every 20
seconds, up to a maximum of 500 seconds, to see if the table was created.

.. literalinclude:: ./example_code/dynamodb/dynamodb_ruby_example_create_movies_table.rb
   :dedent: 0
   :language: ruby

See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/dynamodb/dynamodb_ruby_example_create_movies_table.rb>`_
on GitHub.
