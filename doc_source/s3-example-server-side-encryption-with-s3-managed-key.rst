.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-server-side-encryption-with-s3-managed-key:

##################################################################
Encrypting an |S3| Bucket Item with a Server-Side |S3| Managed Key
##################################################################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items with an S3 managed key using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region
with server-side encryption set to AES-256.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_sses3.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./s3/s3_add_sses3_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the region, bucket name, and item name.

.. literalinclude:: ./s3/s3_add_sses3_encrypt_item.rb
   :lines: 15-17
   :dedent: 0
   :language: ruby

Open the file and get just the file name to use as the bucket key.

.. literalinclude:: ./s3/s3_add_sses3_encrypt_item.rb
   :lines: 20-23
   :dedent: 0
   :language: ruby

Create an |S3| client and call :code:`put_object` to upload the item to the bucket.
Notice that the :code:`server_side_encryption` property is set to :code:`AES256`,
indicating that |S3| encrypts the item using a 256-bit AES cipher.

.. literalinclude:: ./s3/s3_add_sses3_encrypt_item.rb
   :lines: 26-34
   :dedent: 0
   :language: ruby

Finally, close the file and display a success message to the user.

.. literalinclude:: ./s3/s3_add_sses3_encrypt_item.rb
   :lines: 37-39
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_sses3_encrypt_item.rb>`_
on GitHub.
