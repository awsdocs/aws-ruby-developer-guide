.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-client-kms-key:

#########################################################
Encrypting an Amazon S3 Bucket Object with an AWS KMS Key
#########################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket objects with a client-side AWS KMS key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the object :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_object_csekms.rb*.

1. Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

2. Get the AWS KMS key from the command line,
where :code:`key` is an AWS KMS key ID as created in the :doc:`kms-example-create-key` example.

3. Set the bucket and object name and get the contents of the object from the file as a string.

4. Create a |KMS| and |S3| encryption client, call :code:`put_object` to upload the object to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_cskms_encrypt_item.rb>`_
on GitHub.
