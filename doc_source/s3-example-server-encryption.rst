.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-server-encryption

######################
Server-Side Encryption
######################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items on the server using these AWS SDK for Ruby code examples.
    :keywords: AWS SDK for Ruby code examples

To encrypt objects on the server, you have the following options.

* You can have Amazon S3 automatically encrypt objects as you upload
  them to a bucket. Once you configure a bucket with this option,
  every object that you upload--from that point on--is encrypted.

* You can have Amazon S3 encrypt an object when you upload it to a bucket.
  The disadvantage with this approach is that you can still upload objects that
  are not encrypted.

* You can have Amazon S3 reject objects that are not encrypted when you attempt
  to upload them to a bucket.

Learn about service-side encryption in |S3| at
`Protecting Data Using Server-Side Encryption <https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html>`_.

.. toctree::
   :maxdepth: 1

   s3-example-default-server-side-encryption
   s3-example-server-side-encryption
   s3-example-enforce-server-side-encryption
   s3-example-server-side-encryption-with-user-managed-key
