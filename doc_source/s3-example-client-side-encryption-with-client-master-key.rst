.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-client-side-encryption-with-client-master-key:

#############################################
Client-Side Encryption with an AES Master Key
#############################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with a client-side master key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

1. Create the file *encrypt_item_cseaes.rb*.

2. Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

3. Get the key from the command-line.

4. Set the bucket name and object filename.

5. Open the file and get its contents as a string.

6. Create an |S3| encryption client, call :code:`put_object` to upload the item to the bucket,
and display a success message.

.. literalinclude:: ./example_code/s3/s3_add_csaes_encrypt_item.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_csaes_encrypt_item.rb>`_
on GitHub.

The following example creates a 256-bit AES key and displays the value as a string.

.. literalinclude:: ./example_code/s3/s3_create_AES_key.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_create_AES_key.rb>`_,
which includes the code you need to decode the encoded value,
on GitHub.
