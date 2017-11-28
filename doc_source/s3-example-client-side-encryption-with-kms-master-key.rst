.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-client-kms-key:

#########################################################
Encrypting an |S3| Bucket Item with a Client-Side KMS Key
#########################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side KMS key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_cseaes.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the bucket name, item filename, and key ID.
See :doc:`kms-example-create-key` for information on creating a KMS key.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 15-17
   :dedent: 0
   :language: ruby

Read the contents of the file as a string.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 20
   :dedent: 0
   :language: ruby

Create a |KMS| and |S3| encryption client, call :code:`put_object` to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 23-38
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_cskms_encrypt_item.rb>`_
on GitHub.
