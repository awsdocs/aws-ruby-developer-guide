.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-decrypt-object-with-kms-master-key:

#########################################################
Decrypting an Amazon S3 Bucket Object with an AWS KMS Key
#########################################################

.. meta::
    :description:
        Decrypt Amazon S3 bucket objects with client-side AWS KMS keys using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`get_object <Aws/S3/Client.html#get_object-instance_method>` method
to get the object :code-ruby:`my_item` from the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *decrypt_object_csekms.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./s3/s3_get_cskms_decrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Get the AWS KMS key from the command line,
Where :code:`key` is an AWS KMS key ID as created in the :doc:`kms-example-create-key` example
and must be the same value you used to encrypt the object.

.. literalinclude:: ./s3/s3_get_cskms_decrypt_item.rb
   :lines: 16-21
   :dedent: 0
   :language: ruby

Set the bucket name and object name.

.. literalinclude:: ./s3/s3_get_cskms_decrypt_item.rb
   :lines: 23-24
   :dedent: 0
   :language: ruby

Create a |KMS| and |S3| client.

.. literalinclude:: ./s3/s3_get_cskms_decrypt_item.rb
   :lines: 27, 30-33
   :dedent: 0
   :language: ruby

Call :code:`get_object` to get the object and display the result.

.. literalinclude:: ./s3/s3_get_cskms_decrypt_item.rb
   :lines: 36,38
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_get_cskms_decrypt_item.rb>`_
on GitHub.
