.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-kms-example-encrypt-data:

###############
Encrypting Data
###############

The following example uses the |sdk-ruby|
`encrypt <http://docs.aws.amazon.com/sdkforruby/api/Aws/KMS/Client.html#encrypt-instance_method>`_ method,
which implements the
`Encrypt <http://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html>`_ operation,
to encrypt the string "1234567890".
The example displays a readable version of the resulting encrypted blob.

.. literalinclude:: ./example_code/kms/aws-ruby-sdk-kms-example-encrypt-data.rb
   :lines: 13-31
   :dedent: 0
   :language: ruby

Choose :code:`Copy` to save the code locally.
See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/kms/aws-ruby-sdk-kms-example-encrypt-data.rb>`_
on GitHub.
