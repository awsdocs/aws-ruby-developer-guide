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

The following code example checks whether the specified bucket exists in |S3| and is accessible to you.

.. literalinclude:: ./example_code/s3/s3-ruby-example-bucket-exists.rb
   :dedent: 0
   :language: ruby

The following code example checks whether the specified bucket exists in |S3| and you have permission to access it.

.. literalinclude:: ./example_code/s3/s3-ruby-example-head-bucket.rb
   :dedent: 0
   :language: ruby
