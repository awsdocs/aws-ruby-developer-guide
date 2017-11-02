.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-enforce-server-side-encryption:

##################################################################
Requiring Server-Side |S3| Managed Key to Upload |S3| Bucket Items
##################################################################

.. meta::
    :description:
        Require server-side encryption to upload Amazon S3 bucket using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_bucket_policy <Aws/S3/Client.html#put_bucket_policy-instance_method>` method
to require that items uploaded to an |S3| bucket have
AES-256 encryption.
Attempts to upload an item without AES-256 encryption enabled on the item,
raise an :code:` Aws::S3::Errors::AccessDenied` exception.

Choose :code:`Copy` to save the code locally.

Create the file *add_sses3_policy.rb*.

Added the required |S3| gem.
Note how in V2 the |sdk-ruby| did not have service-specific gems.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Set the region and bucket name.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :lines: 15-16
   :dedent: 0
   :language: ruby

Create an |S3| policy that requires server-side 256-bit AES cipher on items
uploaded to the bucket.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :lines: 24-53
   :dedent: 0
   :language: ruby

To require server-side KMS, change:

.. code-block:: ruby

   's3:x-amz-server-side-encryption': 'AES256'

To:

.. code-block:: ruby

   's3:x-amz-server-side-encryption': 'KMS'

Create the |S3| client, apply the policy to the bucket, and print a success message.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :lines: 56-64
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/s3/s3_add_bucket_sses3_encryption_policy.rb>`_
on GitHub.
