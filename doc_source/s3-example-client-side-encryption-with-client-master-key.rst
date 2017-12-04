.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-client-master-key:

############################################################
Encrypting an |S3| Bucket Item with a Client-Side Master Key
############################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side master key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_cseaes.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the bucket name, item filename, and AES key filename.
We'll show you how to create an AES key in a bit.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 15-17
   :dedent: 0
   :language: ruby

Open the file and get its contents as a string.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 20
   :dedent: 0
   :language: ruby

Get the KMS key from the file *aes_key.bin*.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 23
   :dedent: 0
   :language: ruby

Create an |S3| encryption client, call :code:`put_object` to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 26-35
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_csaes_encrypt_item.rb>`_
on GitHub.

The following example creates a 256-bit AES key and saves it as *aes_key.bin*

.. literalinclude:: ./example_code/s3/s3_create_AES_key.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_create_AES_key.rb>`_
on GitHub.
