.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-client-master-key:

#############################################
Client-Side Encryption with an AES Master Key
#############################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side master key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following code example uploads an encrypted object to an |S3| bucket.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :dedent: 0
   :language: ruby

The following code example generates a random AES256-GCM key. Call this function if you do not already have an AES256-GCM key that you want to use to encrypt an object.

.. literalinclude:: ./example_code/s3/s3_create_AES_key.rb
   :dedent: 0
   :language: ruby
