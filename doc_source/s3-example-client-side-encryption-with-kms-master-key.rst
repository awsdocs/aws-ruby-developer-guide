.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-kms-master-key:

###########################################################
Encrypting an |S3| Bucket Item with a Client-Side |KMS| Key
###########################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side KMS key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`encrypt <Aws/KMS/Client.html#encrypt-instance_method>` method
to encrypt an item with a |KMS| key and the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_csekms.rb*.

Added the required |S3| gem.
Note how in V2 the |sdk-ruby| did not have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the region, bucket name, item name, and key value.
See the :doc:`kms-example-create-key` example for information on creating a |KMS| key.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 15-18
   :dedent: 0
   :language: ruby

Open the file, get it's contents, encrypt it with **encrypt**,
and get the ciphered file contents.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 21-33
   :dedent: 0
   :language: ruby


Create an |S3| client, call **put_object** to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_cskms_encrypt_item.rb
   :lines: 35-43
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_cskms_encrypt_item.rb>`_
on GitHub.
