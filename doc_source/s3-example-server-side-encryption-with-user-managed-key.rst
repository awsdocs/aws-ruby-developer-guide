.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-server-side-encryption-with-user-managed-kms-key:

#########################################################
Encrypting an Amazon S3 Bucket Object with an AWS KMS Key
#########################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket objects with an AWS KMS key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the object :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region
with server-side AWS KMS encryption where you provide the key.
See :doc:`kms-example-create-key` for information on creating an AWS KMS key.

Amazon S3 uses, but does not store, the AWS KMS key that you provide.

1. Create the file *encrypt_object_sseck.rb*.

2. Add the required |S3| and **md5** gems.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

3. Get the key from the command-line.
If there is no command-line argument,
print an error message and quit.
Otherwise, create an MD5 hash of the key.
Amazon S3 uses the hash to ensure the integrity of the key.

4. Set the bucket and object names, and get the contents of the object from the file as a string.

5. Create an |S3| client and call :code:`put_object` to upload the object to the bucket.
Notice that the :code:`server_side_encryption` property is set to :code:`aws:kms`,
indicating that |S3| encrypts the object using the provided AWS KMS key.

6.Finally, display a success message to the user.

.. literalinclude:: ./example_code/s3/s3_add_sseck_encrypt_item.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_sseck_encrypt_item.rb>`_
on GitHub.
