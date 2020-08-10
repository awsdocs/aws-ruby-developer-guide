.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _lambda-ruby-example-run-function:

########################
Running a |LAM| Function
########################

.. meta::
    :description:
        Run an AWS Lambda function using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Lambda

The following example runs the |LAM| function named :code:`MyGetitemsFunction` in the :code:`us-west-2`
region.
This function returns a list of items from a database. The input JSON looks like the following.

.. code-block:: json

   {
      "SortBy": "name|time",
      "SortOrder": "ascending|descending",
      "Number": 50
   }

where:

* :code:`SortBy` is the criteria for sorting the results. Our examples uses :code:`time`,
  which means the returned items are sorted in the order in which they were added to the database.

* :code:`SortOrder` is the order of sorting. Our example uses :code:`descending`,
  which means the most-recent item is last in the list.

* :code:`Number` is the maximum number of items to retrieve (the default is 50).
  Our example uses :code:`10`, which means get the 10 most-recent items.

The output JSON looks like the following,
where:

* :code:`STATUS-CODE` is an HTTP status code, :code:`200` means the call was successful.
* :code:`RESULT` is the result of the call, either :code:`success` or :code:`failure`.
* :code:`ERROR` is an error message if :code:`result` is :code:`failure`, otherwise an empty string
* :code:`DATA` is an array of returned results if :code:`result` is :code:`success`, otherwise nil.

.. code-block:: json

   {
      "statusCode": "STATUS-CODE",
      "body": {
         "result": "RESULT",
         "error": "ERROR",
         "data": "DATA"
      }
   }

The first step is to load the modules we use:

* :code:`aws-sdk` loads the AWS SDK for Ruby module we use to invoke the |lam| function.

* :code:`json` loads the JSON module we use to marshall and unmarshall the request and response payloads.

* :code:`os` loads the OS module we use to ensure we can run our Ruby application on Microsoft Windows.
  If you are on a different operating system, you can remove those lines.

* We then create the |lam| client we use to invoke the |lam| function.

* Next we create the hash for the request arguments and call :code:`MyGetItemsFunction`.

* Finally we parse the response, and if are successful, we print out the items.

.. literalinclude:: ./example_code/lambda/aws-ruby-sdk-lambda-example-run-function.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/lambda/aws-ruby-sdk-lambda-example-run-function.rb>`_
on GitHub.
