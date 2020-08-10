.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-get-buckets-in-region:

######################################################
Getting Information about All |S3| Buckets in a Region
######################################################

.. meta::
    :description:
        Get Amazon S3 bucket information for a specific region using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example lists the names of the first 50 buckets for the :code:`us-west-2` region.
If you don't specify a limit, |S3| lists all buckets in :code:`us-west-2`.

.. literalinclude:: ./example_code/s3/s3-ruby-example-show-buckets-in-region.rb
   :dedent: 0
   :language: ruby

.. note:: If a bucket is not in the region in which you instantiated your :code-ruby:`Resource`
   object, the SDK emits a warning message when you call :code-ruby:`get_bucket_location`. You can
   suppress this message by redirecting STDERR.

   On Windows, append :code:`2> nul` to the command.

   On Linux or iOS, append :code:`2> /dev/null` to the command.
