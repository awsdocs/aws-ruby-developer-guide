.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-enforce-server-side-encryption:

#####################################################################
Requiring Encryption on the Server to Upload Amazon S3 Bucket Objects
#####################################################################

.. meta::
    :description:
        Require server-side encryption to upload Amazon S3 bucket using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following example uses the
:ruby-sdk-api:`put_bucket_policy <Aws/S3/Client.html#put_bucket_policy-instance_method>` method
to require that objects uploaded to an |S3| bucket have |S3| encrypt the object with an AWS KMS key.
Attempts to upload an object without specifying that |S3| encrypt the object with an AWS KMS key
raise an :code:`Aws::S3::Errors::AccessDenied` exception.

Avoid using this configuration option if you use default server-side encryption as described in
:doc:`s3-example-default-server-side-encryption` as they could conflict and result in unexpected
results.

Choose :code:`Copy` to save the code locally.

1. Create the file *add_sses3_policy.rb*.

2. Add the required |S3| gem and set the bucket name.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

3. Create an |S3| policy that requires server-side KMS encryption on objects
uploaded to the bucket.

4. Create the |S3| client, apply the policy to the bucket, and print a success message.

.. literalinclude:: ./example_code/s3/s3_add_bucket_sses3_encryption_policy.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_add_bucket_sses3_encryption_policy.rb>`_
on GitHub.
