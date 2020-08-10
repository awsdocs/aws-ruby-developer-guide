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

1. Create the file *decrypt_object_csepk.rb*.

2. Add the required |S3| and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

3. Get the pass phrase from the command line.

4. Set the bucket name, object name, and name of the private key file.

5. Create an RSA key from the contents of the key file and passphrase.

6. Create an |S3| encryption client, call :code:`get_object`, get the contents of the object as text
and print out the object's contents.

.. literalinclude:: ./example_code/s3/s3-ruby-example-get-cspk-item.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3-ruby-example-get-cspk-item.rb>`_
on GitHub.
