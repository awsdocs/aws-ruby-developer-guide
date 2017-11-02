.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-create-public-private-key:

########################################################################
Creating Public and Private RSA Keys to Encrypt Client-Side Bucket Items
########################################################################

.. meta::
    :description:
        Create public and private keys upload client-side encrypted items to Amazon S3 buckets using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class to create a public/private RSA key pair that you can use to
encrypt items on the client before you upload them to an |S3| bucket.
You'll need these keys in the next two examples.

Choose :code:`Copy` to save the code locally.

Create the file *create_rsa_keys.rb*.

Added the required OpenSSL gem.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the pass phrase to seed the key and create the key.

.. literalinclude:: ./example_code/s3/create_rsa_keys.rb
   :lines: 15-16
   :dedent: 0
   :language: ruby

Save the public key as *public_key.pem* and the private
key as *private_secure_key.pem*.

.. literalinclude:: ./example_code/s3/create_rsa_keys.rb
   :lines: 19-28
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/create_rsa_keys.rb>`_
on GitHub.
