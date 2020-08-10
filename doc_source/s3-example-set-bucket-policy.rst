.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-set-bucket-policy:

########################################
Creating an |S3| Bucket Policy with Ruby
########################################

.. meta::
    :description:
        Create an Amazon S3 bucket policy using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

This example demonstrates how to use the |sdk-ruby| to:

#. Create a bucket in |S3long| (|S3|).
#. Define a bucket policy.
#. Add the policy to the bucket.
#. Change the policy.
#. Remove the policy from the bucket.
#. Delete the bucket.

For the complete code for this example, see :ref:`aws-ruby-sdk-s3-example-bucket-policy-code`.

.. _aws-ruby-sdk-s3-example-bucket-policy-prereqs:

Prerequisites
=============

To set up and run this example, you must first:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.

Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example.

This example assumes you have set the credentials in the AWS credentials profile file or in the :code:`AWS_ACCESS_KEY_ID` and
:code:`AWS_SECRET_ACCESS_KEY` environment variables on your local system.

.. _aws-ruby-sdk-s3-example-bucket-policy-config:

Configure the SDK
=================

To configure the SDK for this example, add a :code:`require` statement so you can use the classes and methods
provided by the |sdk-ruby| for |S3|. Then create an :ruby-sdk-api:`Aws::S3::Client <Aws/S3/Client.html>` object in the AWS Region where you want to
create the bucket.

.. _aws-ruby-sdk-s3-example-bucket-policy-create-bucket:

Create a Bucket
===============

Call the :ruby-sdk-api:`create_bucket <Aws/S3/Client.html#create_bucket-instance_method>` method, specifying the bucket's name. This code
uses a variable named :code:`bucket` to represent the bucket's name. Substitute :code:`example-bucket-name` for your
bucket's name.

.. note:: Bucket names must be unique across |S3| |mdash| not just unique to your AWS account.

If you already have a bucket you want to use, you don't have to call :code:`create_bucket`.

.. _aws-ruby-sdk-s3-example-bucket-policy-define-policy:

Define a Bucket Policy
======================

Declare a Ruby hash that represents the policy. Then call the :code:`to_json` method on the
hash to convert it to a JSON object. This code uses a variable named :code:`policy` that contains the policy definition. This policy
allows the specified user to have full control over the :code:`example-bucket-name` (represented by :code:`#{bucket}`).
Substitute :code:`arn:aws:iam::111122223333:user/Alice` with the |ARNlong| (ARN) of the |IAMlong| (|IAM|) user you want to use.

.. code-block:: ruby

 policy = {
  "Version" => "2012-10-17",
  "Statement" => [
    {
      "Effect" => "Allow",
      "Principal" => {
        "AWS" => [
          "arn:aws:iam::111122223333:user/Alice"
        ]
      },
      "Action" => "s3:*",
      "Resource" => [
        "arn:aws:s3:::#{bucket}"
      ]
    }
  ]
 }.to_json

For examples of the types of policies you can define, see :S3-dg:`Bucket Policy Examples <example-bucket-policies>` in the |S3-dg|.

.. _aws-ruby-sdk-s3-example-bucket-policy-add-policy:

Add the Policy to the Bucket
============================

Call the :ruby-sdk-api:`put_bucket_policy <Aws/S3/Client.html#put_bucket_policy-instance_method>`
method, specifying the name of the bucket and the policy definition.

.. code-block:: ruby

 s3.put_bucket_policy(
  bucket: bucket,
  policy: policy
 )

.. _aws-ruby-sdk-s3-example-bucket-policy-change-policy:

Change the Policy
=================

You can call the :code:`put_bucket_policy` method again with a complete replacement policy. However, you can
also make incremental updates to an existing policy, which can reduce the amount of code you need to write. To do this, retrieve
the current policy by calling the :ruby-sdk-api:`get_bucket_policy <Aws/S3/Client.html#get_bucket_policy-instance_method>` method.
Next, parse the JSON object that is returned into a Ruby hash. Then make your incremental changes to the policy. For example,
this code changes the ARN of the |IAM| entity. After you make your changes, call the :code:`put_bucket_policy` method again.
Be sure to call the :code:`to_json` method on the hash to convert it back to a JSON object before applying the changed policy to the bucket.

.. code-block:: ruby

 policy_string = s3.get_bucket_policy(bucket: bucket).policy.read
 policy_json = JSON.parse(policy_string)

 policy_json["Statement"][0]["Principal"]["AWS"] = "arn:aws:iam::111122223333:root"

 s3.put_bucket_policy(
  bucket: bucket,
  policy: policy_json.to_json
 )

.. _aws-ruby-sdk-s3-example-bucket-policy-clean-up:

Clean Up
========

To remove the policy from the bucket, call the :ruby-sdk-api:`delete_bucket_policy <Aws/S3/Client.html#delete_bucket_policy-instance_method>`
method, specifying the name of the bucket.

To delete the bucket, call the
:ruby-sdk-api:`delete_bucket <Aws/S3/Client.html#delete_bucket-instance_method>` method, specifying the name of the bucket.

.. code-block:: ruby

 s3.delete_bucket_policy(bucket: bucket)
 s3.delete_bucket(bucket: bucket)

.. _aws-ruby-sdk-s3-example-bucket-policy-code:

Complete Example
================

Here is the complete code for this example.

.. literalinclude:: ./example_code/s3/s3-ruby-example-bucket-policy.rb
   :dedent: 0
   :language: ruby
