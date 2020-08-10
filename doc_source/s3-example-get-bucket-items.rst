.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-get-bucket-items:

###########################################
Getting Information about |S3| Bucket Items
###########################################

.. meta::
    :description:
        Get Amazon S3 bucket item information using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

A presigned URL gives you access to the object identified in the URL, if the creator of the
presigned URL has permissions to access that object. You can use a presigned URL to allow a user to
click a link and see an item without having to make the item public.

The following example lists the names and presigned URLs of the first 50 items of the bucket
:code-ruby:`my-bucket` in the :code:`us-west-2` region.  If a limit is not specified, |S3| lists up
to 1,000 items.

.. literalinclude:: ./example_code/s3/s3-ruby-example-list-bucket-items.rb
   :dedent: 0
   :language: ruby
