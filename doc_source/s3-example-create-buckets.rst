.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-create-buckets:

#################################
Creating and Using an |S3| Bucket
#################################

.. meta::
    :description:
        Learn to create and use Amazon S3 buckets through this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

The following code example:

#. Lists available buckets in |S3| for the specified AWS Region.
#. Creates two buckets.
#. Uploads an object to one of the buckets.
#. Copies the uploaded object to the other bucket.
#. Deletes the object from the first bucket.

.. literalinclude:: ./example_code/s3/s3_ruby_create_bucket.rb
   :dedent: 0
   :language: ruby
