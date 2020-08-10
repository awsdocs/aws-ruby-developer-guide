.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-upload-bucket-item:

###################################
Uploading an Item to an |S3| Bucket
###################################

.. meta::
    :description:
        Upload Amazon S3 bucket items using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uploads the item (file) :file:`C:\file.txt` to the bucket
:code-ruby:`my-bucket` in the :code:`us-west-2` region.  Because :file:`C:\file.txt` is the fully
qualified name of the file, the name of the item is set to the name of the file.

.. literalinclude:: ./example_code/s3/s3-ruby-example-upload-item.rb
   :dedent: 0
   :language: ruby
