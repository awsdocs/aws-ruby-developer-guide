.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-default-server-side-encryption:

##############################################################
Setting Default Server-Side Encryption for an Amazon S3 Bucket
##############################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items by default using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_bucket_encryption <Aws/S3/Client.html#put_bucket_encryption-instance_method>`
method to enable KMS server-side encryption on any items added to
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

The only exception is if the user configures their request to explicitly
use server-side encryption. In that case, the specified encryption takes precedence.

Choose :code:`Copy` to save the code locally.

1. Create the file *add_default_sse_encryption.rb*.

2. Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

3. Get the KMS key from the command line,
Where :code:`key` is a KMS key ID as created in the :doc:`kms-example-create-key` example.

4. Create an |S3| client and call :code:`put_bucket_encryption` to add
default encryption to the bucket.

.. literalinclude:: ./example_code/s3/s3_add_default_sse_encryption.rb
   :dedent: 0
   :language: ruby



See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_default_sse_encryption.rb>`_
on GitHub.
