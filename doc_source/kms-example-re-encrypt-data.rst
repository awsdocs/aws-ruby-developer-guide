.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-kms-example-re-encrypt-data:

##################################
Re-encrypting a Data Blob in |KMS|
##################################

.. meta::
    :description:
        Re-encrypt a data blob in AWS KMS using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code example, KMS

The following example uses the |sdk-ruby|
`re_encrypt <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/KMS/Client.html#re_encrypt-instance_method>`_ method,
which implements the
`ReEncrypt <http://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html>`_ operation,
to decrypt encrypted data and then immediately re-encrypt data under a new customer master key (CMK).
The operations are performed entirely on the server side within |KMS|,
so they never expose your plaintext outside of |KMS|.
The example displays a readable version of the resulting re-encrypted blob.

.. literalinclude:: ./example_code/kms/aws-ruby-sdk-kms-example-re-encrypt-data.rb
   :dedent: 0
   :language: ruby

Choose :code:`Copy` to save the code locally.
See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/kms/aws-ruby-sdk-kms-example-re-encrypt-data.rb>`_
on GitHub.
