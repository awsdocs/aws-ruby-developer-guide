.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-public-key:

############################################################
Encrypting an |S3| Bucket Item with a Client-Side Public Key
############################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side public key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class to encrypt an item with a public key and the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_csepk.rb*.

Add the required |S3|, Base64, and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_cspk_encrypt_item.rb
   :lines: 13-15
   :dedent: 0
   :language: ruby

Set the region, bucket name, item name, and name of the file containing the public key.
See :doc:`s3-example-create-public-private-key` for information about creating a public key.

.. literalinclude:: ./example_code/s3/s3_add_cspk_encrypt_item.rb
   :lines: 17-20
   :dedent: 0
   :language: ruby

Open the file, get its contents as a string, and encrypt that string
using the public key.

.. literalinclude:: ./example_code/s3/s3_add_cspk_encrypt_item.rb
   :lines: 23-29
   :dedent: 0
   :language: ruby

Create an |S3| client, call :code:`put_object` to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_cspk_encrypt_item.rb
   :lines: 32-41
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_cspk_encrypt_item.rb>`_
on GitHub.
