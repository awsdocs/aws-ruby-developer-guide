.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-object-with-private-key:

########################################################
Decrypting an Amazon S3 Bucket Object with a Private Key
########################################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket objects with client-side private keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`get_object <Aws/S3/Client.html#get_object-instance_method>` method
to get the object :code-ruby:`my_item` from the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region. Then it
decrypts the contents with the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class.

Choose :code:`Copy` to save the code locally.

Create the file *decrypt_object_csepk.rb*.

Add the required |S3| and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :lines: 13-14
   :dedent: 0
   :language: ruby

Get the pass phrase from the command line.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :lines: 16-21
   :dedent: 0
   :language: ruby

Set the bucket name, object name, and name of the private key file.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :lines: 23-25
   :dedent: 0
   :language: ruby

Create an RSA key from the contents of the key file and passphrase.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :lines: 28-29
   :dedent: 2
   :language: ruby

Create an |S3| encryption client, call :code:`get_object`, get the contents of the object as text
and print out the object's contents.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :lines: 32,34,36
   :dedent: 2
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3-ruby-example-get-cspk-item.rb>`_
on GitHub.
