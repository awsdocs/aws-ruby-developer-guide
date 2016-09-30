.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

#################
|DDBlong| Recipes
#################

You can use the following recipes to access |DDBlong| services by using the |sdk-ruby|. For more
information about |DDB|, see the `Amazon DynamoDB documentation
<http://aws.amazon.com/documentation/dynamodb>`_. Specifically, see `Ruby and DynamoDB
<http://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/GettingStarted.Ruby.html>`_ to
learn how to:

* Create a table and load sample data in JSON format.

* Perform create, read, update, and delete operations on the table.

* Run simple queries.

The topic also provides a link to a downloadable version of |DDB|, which includes an interactive web
interface so you can experiment with |DDB| offline.

**Recipes**

* :ref:`aws-ruby-sdk-dynamo-recipe-get-tables`

* :ref:`aws-ruby-sdk-dynamo-recipe-create-table`

* :ref:`aws-ruby-sdk-dynamo-recipe-add-item-to-table`

* :ref:`aws-ruby-sdk-dynamo-recipe-list-table-items`

* :ref:`aws-ruby-sdk-dynamo-recipe-get-table-item`

* :ref:`aws-ruby-sdk-dynamo-recipe-update-table`

* :ref:`aws-ruby-sdk-dynamo-recipe-create-index`

.. _aws-ruby-sdk-dynamo-recipe-get-tables:

Getting Information about All Tables
====================================

The following example lists the names and number of items in each table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-show-tables-names-and-item-count.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-create-table:

Creating a Simple Table with a Single Primary Key
=================================================

The following example creates the table :code-ruby:`Users` with three attributes: :code-ruby:`ID`,
:code-ruby:`FirstName`, and :code-ruby:`LastName` in the :code-ruby:`us-west-2` region.

The :code-ruby:`wait_until` call blocks you from using the table until |DDB| has created it.  By
default, the |DDB| client's :code-ruby:`wait_until` method checks every 20 seconds, up to a maximum
of 500 seconds, to see if the table was created.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-create-users-table.rb
   :lines: 13-48
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-add-item-to-table:

Adding an Item to a Table
=========================

The following example adds an item with the :code:`ID` value of **123456**, :code-ruby:`FirstName`
value of **John**, and :code-ruby:`LastName` value of **Doe** to the :code-ruby:`Users` table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-add-item-users-table.rb
   :lines: 13-25
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-list-table-items:

Getting Information about the Items in a Table
==============================================

The following example lists up to 50 items from the :code-ruby:`Users` table in the
:code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-list-50-users-table-items.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-get-table-item:

Getting Information about a Specific Item in a Table
====================================================

The following example displays the first and last name of an item with an :code-ruby:`ID` of
**123456** in the :code-ruby:`Users` table in the :code-ruby:`us-west-2` region.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-list-item-123456-users-table.rb
   :lines: 13-27
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-update-table:

Updating a Table
================

The following example updates all the items in the :code-ruby:`Users` table in the :code-ruby:`us-west-2`
region to include a new field, :code-ruby:`airmiles`, and sets the value to **10000**.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-update-users-table.rb
   :lines: 13-33
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-dynamo-recipe-create-index:

Creating an Index
=================

The following example adds a new index, :code-ruby:`air-mileage-index`, to the :code-ruby:`Users`
table in the :code-ruby:`us-west-2` region.  Once the status of the index is :code-ruby:`ACTIVE`,
you can search for items in the table based on the value of their :code-ruby:`airmiles`.

.. literalinclude:: ./example_code/dynamodb/dynamodb-ruby-example-add-index.rb
   :lines: 13-47
   :dedent: 0
   :language: ruby
