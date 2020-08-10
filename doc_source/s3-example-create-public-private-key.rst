.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-create-public-private-key:

###########################################
Creating Public and Private Asymmetric Keys
###########################################

.. meta::
    :description:
        Create public and private keys to upload and download encrypted objects to
        Amazon S3 buckets using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
`PKey <http://ruby-doc.org/stdlib-2.0.0/libdoc/openssl/rdoc/OpenSSL/PKey.html>`_
class to create a public and private keys.
Use the public key to encrypt objects on the client before you upload them to an
|S3| bucket.
Use the private key and pass phrase to decrypt objects on the client after you
download them from an |S3| bucket.
The
:doc:`s3-example-client-side-encryption-with-public-key` and
:doc:`s3-example-client-side-decrypt-item-with-private-key` examples
use public and private keys, respectively.

Choose :code:`Copy` to save the code locally.

.. literalinclude:: ./example_code/s3/create_rsa_keys.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/create_rsa_keys.rb>`_
on GitHub.
