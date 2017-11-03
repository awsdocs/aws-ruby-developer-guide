.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-item-with-private-key:

#############################################################
Decrypting an |S3| Bucket Item with a Client-Side Private Key
#############################################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket items with client-side private keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`get_object <Aws/S3/Client.html#get_object-instance_method>` method
to get the item :code-ruby:`my_item` from the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region. Then it
decrypts the contents with the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class.

Choose :code:`Copy` to save the code locally.

Create the file *decrypt_item_csepk.rb*.

Add the required |S3|, Base64, and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_get_cspk_decrypt_item.rb
   :lines: 13-15
   :dedent: 0
   :language: ruby

Set the region, bucket name, item name, name of the private key file, and
pass phrase.

.. literalinclude:: ./example_code/s3/s3_get_cspk_decrypt_item.rb
   :lines: 17-21
   :dedent: 0
   :language: ruby

Create an |S3| client, call :code:`get_object`, and get the contents of the item as text.

.. literalinclude:: ./example_code/s3/s3_get_cspk_decrypt_item.rb
   :lines: 24-30
   :dedent: 0
   :language: ruby

Create an **RSA** object, decipher the contents of the item using the private key,
and display the resulting text.

.. literalinclude:: ./example_code/s3/s3_get_cspk_decrypt_item.rb
   :lines: 33-36
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_get_cspk_decrypt_item.rb>`_
on GitHub.
