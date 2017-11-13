.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-encrypt-bucket-items

############################
Encrypting |S3| Bucket Items
############################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items using these AWS SDK for Ruby code examples.
    :keywords: AWS SDK for Ruby code examples

The :doc:`s3-example-set-item-props` example added a number of properties, including server-side encryption,
to a bucket item. The following examples demonstrate how to encrypt and decrypt
bucket items using both server-side encryption as shown in that example, and
client-side encryption.
For more information about encryption in |S3|, see
`Protecting Data Using Encryption <http://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html>`_.

.. toctree::
   :maxdepth: 1

   s3-example-default-server-side-encryption
   s3-example-server-side-encryption
   s3-example-enforce-server-side-encryption
   s3-example-client-side-encryption-with-kms-master-key
   s3-example-client-side-decrypt-item-with-kms-master-key
   s3-example-client-side-encryption-with-client-master-key
   s3-example-client-side-decrypt-item-with-client-master-key
   s3-example-create-public-private-key
   s3-example-client-side-encryption-with-public-key
   s3-example-client-side-decrypt-item-with-private-key
