.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-dynamo-example-create-table:

#################################################
Creating a Simple Table with a Single Primary Key
#################################################

The following example creates the table :code-ruby:`Users` with three attributes: :code-ruby:`ID`,
:code-ruby:`FirstName`, and :code-ruby:`LastName` in the :code-ruby:`us-west-2` region.

The :code-ruby:`wait_until` call blocks you from using the table until |DDB| has created it.  By
default, the |DDB| client's :code-ruby:`wait_until` method checks every 20 seconds, up to a maximum
of 500 seconds, to see if the table was created.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-create-users-table.rb
   :lines: 13-48
   :dedent: 0
   :language: ruby