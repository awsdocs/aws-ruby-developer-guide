.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-delete-table-item:

################################
Deleting an |DDBlong| Table Item
################################

.. meta::
    :description:
        Delete an Amazon DynamoDB table item using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, DynamoDB

The following example deletes item with the :code:`year` **2015** and
:code-ruby:`title`  **The Big New Movie**
from the :code-ruby:`Movies` table in the :code-ruby:`us-west-2` region.

.. literalinclude:: ./dynamodb/dynamodb_ruby_example_delete_movies_item.rb
   :lines: 13-32
   :dedent: 0
   :language: ruby

See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/dynamodb/dynamodb_ruby_example_delete_movies_item.rb>`_
on GitHub.
