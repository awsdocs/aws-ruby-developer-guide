.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-encryption

######################
Client-Side Encryption
######################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items on the client using these AWS SDK for Ruby code examples.
    :keywords: AWS SDK for Ruby code examples

To encrypt objects on the client, you perform the encryption yourself,
either using keys that you create or keys that AWS Key Management Service (AWS KMS) manages for you.

Learn about client-side encryption in |S3| at
`Protecting Data Using Client-Side Encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`_.

.. toctree::
   :maxdepth: 1

   s3-example-client-side-encryption-with-kms-master-key
   s3-example-client-side-decrypt-item-with-kms-master-key
   s3-example-create-public-private-key
   s3-example-client-side-encryption-with-public-key
   s3-example-client-side-decrypt-item-with-private-key
