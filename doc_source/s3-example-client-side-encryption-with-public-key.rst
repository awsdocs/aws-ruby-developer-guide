.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-public-key:

#######################################################
Encrypting an Amazon S3 Bucket Object with a Public Key
#######################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket buckets with a client-side public key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class to encrypt an object with a public key and the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the object :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_object_csepk.rb*.

Add the required |S3| and OpenSSL gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./s3/s3-ruby-example-add-cspk-item.rb
   :lines: 13-14
   :dedent: 0
   :language: ruby

Set the bucket name, object name, and name of the file containing the public key.
See :doc:`s3-example-create-public-private-key` for information about creating a public key.

.. literalinclude:: ./s3/s3-ruby-example-add-cspk-item.rb
   :lines: 16-18
   :dedent: 0
   :language: ruby

Get the file contents as a string; get the public key from the file
and create a new RSA key to encrypt the bucket object.

.. literalinclude:: ./s3/s3-ruby-example-add-cspk-item.rb
   :lines: 21,22,24
   :dedent: 0
   :language: ruby

Create an |S3| encryption client and call :code:`put_object` to upload the object to the bucket.
Finally, display a message to the user about the results.

.. literalinclude:: ./s3/s3-ruby-example-add-cspk-item.rb
   :lines: 28-37
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3-ruby-example-add-cspk-item.rb>`_
on GitHub.
