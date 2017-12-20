.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-server-side-encryption:

######################
Server-Side Encryption
######################

.. meta::
    :description:
        Encrypt Amazon S3 bucket items on the server using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method
to add the item :code-ruby:`my_item` to the bucket
:code-ruby:`my_bucket` in the :code:`us-west-2` region
with server-side encryption set KMS.

Note that this differs from :doc:`s3-example-default-server-side-encryption`,
is in that case, the objects are encrypted without you having to explicitly perform the operation.

Choose :code:`Copy` to save the code locally.

Create the file *encrypt_item_sse.rb*.

Add the required |S3| gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Get the KMS key from the command line,
Where :code:`key` is a KMS key ID as created in the :doc:`kms-example-create-key` example.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 15-21
   :dedent: 0
   :language: ruby

Set the bucket and item name and get the object from the file as a string.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 23-24, 27
   :dedent: 0
   :language: ruby

Create an |S3| client and call :code:`put_object` to upload the item to the bucket.
Notice that the :code:`server_side_encryption` property is set to :code:`aws:kms`,
indicating that |S3| encrypts the item using KMS.
Finally, display a success message to the user.

.. literalinclude:: ./example_code/s3/s3_add_sses3_encrypt_item.rb
   :lines: 30-41
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_sses3_encrypt_item.rb>`_
on GitHub.
