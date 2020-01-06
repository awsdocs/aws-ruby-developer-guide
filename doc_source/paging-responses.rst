.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-paging-response-data:

####################
Paging Response Data
####################

.. meta::
    :description:
        Learn how to use paged responses to limit data returned for a response using the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby

Some AWS calls provide paged responses to limit the amount of data returned with each response. A
page of data represents up to 1,000 items.

.. _aws-ruby-sdk-paged-response-enumerable:

Paged Responses Are Enumerable
==============================

The simplest way to handle paged response data is to use the built-in enumerator in the response
object, as shown in the following example.

.. code-block:: ruby

    s3 = Aws::S3::Client.new

    s3.list_objects(bucket:'aws-sdk').each do |response|
      puts response.contents.map(&:key)
    end

This yields one response object per API call made, and enumerates objects in the named bucket.
The SDK retrieves additional pages of data to complete the request.

.. _aws-ruby-sdk-handling-paged-response-handling:

Handling Paged Responses Manually
=================================

To handle paging yourself, use the response's :code:`next_page?` method to verify there are more
pages to retrieve, or use the :code:`last_page?` method to verify there are no more pages to
retrieve.

If there are more pages, use the :code:`next_page` (notice there is no :code:`?`) method to retrieve
the next page of results, as shown in the following example.

.. code-block:: ruby

    s3 = Aws::S3::Client.new

    # Get the first page of data
    response = s3.list_objects(bucket:'aws-sdk')

    # Get additional pages
    while response.next_page? do
      response = response.next_page
      # Use the response data here...
    end

.. note:: If you call the :code:`next_page` method and there are no more pages to retrieve, the SDK raises an
    `Aws::PageableResponse::LastPageError
    <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/PageableResponse/LastPageError.html>`_ exception.

.. _aws-ruby-sdk-paged-data-classes:

Paged Data Classes
==================

Paged data in the |sdk-ruby| is handled by the `Aws::PageableResponse
<http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/PageableResponse.html>`_ class, which is included
with `Seahorse::Client::Response
<http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Seahorse/Client/Response.html>`_ to provide access to
paged data.
