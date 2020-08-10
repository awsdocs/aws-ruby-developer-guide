.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-does-bucket-exist:

#########################################
Determining Whether an |S3| Bucket Exists
#########################################

.. meta::
    :description:
        Find out if an Amazon S3 bucket exists using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code example. Amazon S3

There are two cases in which you would want to determine whether a bucket already exists. You
perform these tests in lieu of receiving an exception if the condition fails:

* You want to determine whether a bucket with a specific name already exists among all buckets, even
  ones to which you do not have access.  This test helps prevent you from trying to create a bucket
  with the name of an existing bucket, which causes an exception.

* You want to perform an operation, such as add an item to a bucket, only on a bucket to which you
  have access.

The following example sets :code-ruby:`bucket_exists` to :code:`true` if a bucket with the name
:code-ruby:`my-bucket` already exists.  The :code:`region:` parameter to :code:`Resource` has no
effect on the result.

.. literalinclude:: ./example_code/s3/s3-ruby-example-bucket-exists.rb
   :dedent: 0
   :language: ruby

The following example sets ``bucket_exists`` to ``true`` if the bucket with the
name ``my-bucket`` exists and you have access to the bucket.
In this case, the ``region`` parameter to ``Client`` has an effect on the result.

.. literalinclude:: ./example_code/s3/s3-ruby-example-head-bucket.rb
   :dedent: 0
   :language: ruby
