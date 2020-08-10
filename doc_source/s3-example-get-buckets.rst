.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-get-buckets:

##########################################
Getting Information about All |S3| Buckets
##########################################

.. meta::
    :description:
        Get Amazon S3 bucket information using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

The following example lists the names of up to 50 of your |S3| buckets.  Copy the code and save it
as :file:`buckets.rb`. Notice that although the :code:`Resource` object is created in the
:code:`us-west-2` region, |S3| returns buckets to which you have access, regardless of the region
they are in.

.. literalinclude:: ./example_code/s3/s3-ruby-example-show-50-buckets.rb
   :dedent: 0
   :language: ruby

.. note:: When you specify a region, the :code:`buckets` method calls the
   :code:`Client#list_buckets` method, which returns a list of all buckets owned by the
   authenticated sender of the request.  See :ref:`aws-ruby-sdk-s3-example-get-buckets-in-region` to
   learn how to filter this list to get the buckets only in a specific region.
