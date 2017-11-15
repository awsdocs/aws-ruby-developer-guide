.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-server-side-encryption:

############################################
Encrypting an |S3| Bucket Item on the Server
############################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items on the server using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region
with server-side encryption set to 256-bit AES.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_sse.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the bucket and item name.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 15-16
   :dedent: 0
   :language: ruby

Get the contents of the file as a string.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 19
   :dedent: 0
   :language: ruby

Create an |S3| client and call :code:`put_object` to upload the item to the bucket.
Notice that the :code:`server_side_encryption` property is set to :code:`AES256`,
indicating that |S3| encrypts the item using a 256-bit AES cipher.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 22-30
   :dedent: 0
   :language: ruby

Display a success message to the user.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 32
   :dedent: 0
   :language: ruby

You can also specify server-side KMS encryption by changing:

.. code-block:: ruby

   server_side_encryption: 'AES256',

To:

.. code-block:: ruby

   server_side_encryption: 'aws:kms',
   ssekms_key_id: KEY,

Where *KEY* is a KMS key ID as created in the :doc:`kms-example-create-key` example.

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_sses3_encrypt_item.rb>`_
on GitHub.
