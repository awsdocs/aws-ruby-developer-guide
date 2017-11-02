.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-item-with-client-master-key:

##########################################################
Decrypting an |S3| Bucket Item with Client-Side Master Key
##########################################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket items with client-side master keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`get_object <Aws/S3/Client.html#get_object-instance_method>` method
to get the item :code-ruby:`my_item` from the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region,
and decrypts the contents with the
`Cipher <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/Cipher.html>`_
class.

Choose :code:`Copy` to save the code locally.

Create the file *decrypt_item_cseaes.rb*.

Added the required |S3| and OpenSSL gems.
Note how in V2 the |sdk-ruby| did not have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_get_csaes_decrypt_item.rb
   :lines: 13-14
   :dedent: 0
   :language: ruby

Set the region, bucket name, item name, key, and initialization vector.

.. literalinclude:: ./example_code/s3/s3_get_csaes_decrypt_item.rb
   :lines: 16-20
   :dedent: 0
   :language: ruby

Create an |S3| client, call **get_object**, and get the contents of the item as text.

.. literalinclude:: ./example_code/s3/s3_get_csaes_decrypt_item.rb
   :lines: 23-29
   :dedent: 0
   :language: ruby

Create an **AES256** object, decipher the contents of the item,
and display the decrtyped text.

.. literalinclude:: ./example_code/s3/s3_get_csaes_decrypt_item.rb
   :lines: 32-39
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_get_csaes_decrypt_item.rb>`_
on GitHub.
