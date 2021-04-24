.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-object-with-kms-master-key:

#########################################################
Decrypting an Amazon S3 Bucket Object with an AWS KMS Key
#########################################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket objects with client-side AWS KMS keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following code example gets the contents of an encrypted object in an |S3| bucket.

.. literalinclude:: ./example_code/s3/s3_get_cskms_decrypt_item.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_get_cskms_decrypt_item.rb>`_
on GitHub.
