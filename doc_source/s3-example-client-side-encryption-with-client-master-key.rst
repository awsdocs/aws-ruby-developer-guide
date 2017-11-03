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
`Cipher <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/Cipher.html>`_
class to encrypt an item with a 256-bit AES key, and the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_cseaes.rb*.

Add the required |S3| and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 13-14
   :dedent: 0
   :language: ruby

Set the region, bucket name, item name, and key value.
See the :doc:`kms-example-create-key` example for information about creating an |KMS| key.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 16-19
   :dedent: 0
   :language: ruby

Create the cipher, random initialization vector, and key. Then display the value
of the initialization vector, as you need that value to decrypt the item.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 22-33
   :dedent: 0
   :language: ruby

Open the file, get its contents, and encrypt it.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 36-41
   :dedent: 0
   :language: ruby

Create an |S3| client, call :code:`put_object` to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :lines: 44-53
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_csaes_encrypt_item.rb>`_
on GitHub.
