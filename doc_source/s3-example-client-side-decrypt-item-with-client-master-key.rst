.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-item-with-client-master-key:

#############################################
Client-Side Decryption with an AES Master Key
#############################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket items with client-side master keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following code example gets the contents of an encrypted object in an |S3| bucket.

.. literalinclude:: ./example_code/s3/s3_get_csaes_decrypt_item.rb
   :dedent: 0
   :language: ruby

