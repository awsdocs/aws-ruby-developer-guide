.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-set-bucket-permission:

##################################################
Managing |S3| Bucket and Object Access Permissions
##################################################

.. meta::
    :description:
        Manage access permissions for Amazon S3 buckets and objects using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

This example demonstrates how to use the |sdk-ruby| to:

#. Set a predefined grant (also known as a :dfn:`canned ACL`) for a bucket in |S3|.
#. Add an object to the bucket.
#. Set a canned ACL for an object in the bucket.
#. Get the bucket's current ACL.

For the complete code for this example, see :ref:`aws-ruby-sdk-s3-example-set-bucket-permission-code`.

.. _aws-ruby-sdk-s3-example-set-bucket-permission-prereqs:

Prerequisites
=============

To set up and run this example, you must first:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.

Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example.

This example assumes you have set the credentials in the AWS credentials profile file or in the :code:`AWS_ACCESS_KEY_ID` and
:code:`AWS_SECRET_ACCESS_KEY` environment variables on your local system.

.. _aws-ruby-sdk-s3-example-set-bucket-permission-config:

Configure the SDK
=================

For this example, add a :code:`require` statement so that you can use the classes and methods
provided by the |sdk-ruby| for |S3|. Then create an :ruby-sdk-api:`Aws::S3::Client <Aws/S3/Client.html>` object in the AWS Region where you want to
create the bucket. This code creates the :code:`Aws::S3::Client` object in the :code:`us-west-2` region. This code also declares a variable representing the bucket.

.. code-block:: ruby

 require 'aws-sdk-s3'  # v2: require 'aws-sdk'

 # Create a S3 client
 client = Aws::S3::Client.new(region: 'us-west-2')

.. _aws-ruby-sdk-s3-example-set-bucket-permission-bucket-acl:

Set a Canned ACL for a Bucket
=============================

Call the :ruby-sdk-api:`put_bucket_acl <Aws/S3/Client.html#put_bucket_acl-instance_method>` method, specifying the names of the canned ACL and the bucket. This code
sets the :code:`public-read` canned ACL on the bucket, which enables full control for the bucket's owner and read-only access for everyone else.

.. code-block:: ruby

 client.put_bucket_acl({
  acl: "public-read",
  bucket: bucket,
 })

For more information about canned ACLs, see **Canned ACL** in :S3-dg:`Access Control List (ACL)
Overview <acl-overview>` in the |S3-dg|.

To confirm this setting, call the Ruby :code:`Net::HTTP.get` method to attempt to get the bucket's content.

.. code-block:: ruby

 bucket_path = "http://#{bucket}.s3-us-west-2.amazonaws.com/"
 resp = Net::HTTP.get(URI(bucket_path))
 puts "Content of unsigned request to #{bucket_path}:\n\n#{resp}\n\n"

.. _aws-ruby-sdk-s3-example-set-bucket-permission-upload-object:

Upload an Object to a Bucket
============================

Call the :ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method, specifying
the names of the bucket and object and the object's content.
This code declares a variable representing the object.

.. code-block:: ruby

 object_key = "my-key"
 # Put an object in the public bucket
 client.put_object({
   bucket: bucket,
   key: object_key,
   body: 'Hello World',
 })

.. _aws-ruby-sdk-s3-example-set-bucket-permission-object-acl:

Set a Canned ACL for an Object
==============================

By default, you can't get the contents of the object in the bucket. To
confirm this behavior, call the Ruby :code:`Net::HTTP.get` method to attempt to get the object's content.

.. code-block:: ruby

 object_path = "http://#{bucket}.s3-us-west-2.amazonaws.com/#{object_key}"
 resp = Net::HTTP.get(URI(object_path))
 puts "Content of unsigned request to #{object_path}:\n\n#{resp}\n\n"

To change this behavior, call the :ruby-sdk-api:`put_object_acl <Aws/S3/Client.html#put_object_acl-instance_method>` method, specifying the names of the canned ACL, bucket, and object. This code
sets the :code:`public-read` canned ACL on the object, which enables full control for the object's owner
and read-only access for everyone else. After the call, try to get the object's content again.

.. code-block:: ruby

 client.put_object_acl({
  acl: "public-read",
  bucket: bucket,
  key: object_key,
 })
 object_path = "http://#{bucket}.s3-us-west-2.amazonaws.com/#{object_key}"
 puts "Now I can access object (#{object_key}) :\n#{Net::HTTP.get(URI(object_path))}\n\n"

.. _aws-ruby-sdk-s3-example-set-bucket-permission-get-bucket-acl:

Get a Bucket's Current ACL
==========================

Call the :ruby-sdk-api:`get_bucket_acl <Aws/S3/Client.html#get_bucket_acl-instance_method>` method, specifying the name of the bucket. The :code:`get_bucket_acl` method returns an
instance of the :ruby-sdk-api:`Aws::S3::Types::GetBucketAclOutput <Aws/S3/Types/GetBucketAclOutput.html>` class. Use the :code:`grants` attribute of the
:code:`GetBucketAclOutput` class to list the bucket's current ACL.

.. code-block:: ruby

 resp = client.get_bucket_acl(bucket: bucket)
 puts resp.grants

.. _aws-ruby-sdk-s3-example-set-bucket-permission-code:

Complete Example
================

Here is the complete code for this example.

.. literalinclude:: ./example_code/s3/s3-ruby-example-access-permissions.rb
   :dedent: 0
   :language: ruby
