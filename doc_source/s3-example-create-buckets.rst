.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-create-buckets:

#################################
Creating and Using an |S3| Bucket
#################################

.. meta::
    :description:
        Learn to create and use Amazon S3 buckets through this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

This example demonstrates how to use the |sdk-ruby| to:

#. Display a list of buckets in |S3|.
#. Create a bucket.
#. Upload an object (a file) to the bucket.
#. Copy files to the bucket.
#. Delete files from the bucket.

For the complete code for this example, see :ref:`aws-ruby-sdk-s3-example-create-buckets-code`.

.. _aws-ruby-sdk-s3-example-create-buckets-prereqs:

Prerequisites
=============

To set up and run this example, you must first:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.

Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example.

This example assumes you have set the credentials in the AWS credentials profile file and named the file
:code:`david`.

.. _aws-ruby-sdk-s3-example-create-buckets-config:

Configure the SDK
=================

For this example, add :code:`require` statements so that you can use the classes and methods
provided by the |sdk-ruby| for |S3| and work with JSON-formatted data. Then create an :ruby-sdk-api:`Aws::S3::Client
<Aws/S3/Client.html>` object in the AWS Region where you want to
create the bucket and the specified AWS profile. This code creates the :code:`Aws::S3::Client` object
in the :code:`us-east-1` region.
Additional variables are also declared for the two buckets used in this example.

.. _aws-ruby-sdk-s3-example-create-buckets-list:

Get a List of Buckets
=====================

Call the :ruby-sdk-api:`list_buckets <Aws/S3/Client.html#list_buckets-instance_method>` method. This returns an instance of the
:ruby-sdk-api:`Aws::S3::Types::ListBucketsOutput <Aws/S3/Types/ListBucketsOutput.html>` class, which represents the list of buckets.
Then use the :code:`buckets` attribute of the :code:`ListBucketsOutput` class to access the buckets' properties, such as :code:`name` for each bucket's name.

.. _aws-ruby-sdk-s3-example-create-buckets-create:

Create a Bucket
===============

Call the :ruby-sdk-api:`create_bucket <Aws/S3/Client.html#create_bucket-instance_method>` method, specifying the bucket's name.

.. note:: Bucket names must be unique across |S3| |mdash| not just unique to your AWS account.

.. _aws-ruby-sdk-s3-example-create-buckets-upload:

Upload an Object (a File) to a Bucket
=====================================

Call the :ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method, specifying settings such as the bucket's name and the name of the file to create.
For the file's contents, you can specify an instance of a Ruby :code:`File` class or, in this example, a string representing the file's data.

To confirm whether the file was uploaded successfully, call the :ruby-sdk-api:`list_objects_v2 <Aws/S3/Client.html#list_objects_v2-instance_method>` method. This returns an instance
of the :ruby-sdk-api:`Aws::S3::Types::ListObjectsV2Output <Aws/S3/Types/ListObjectsV2Output.html>` class, which represents the bucket's objects. Then use the :code:`contents` method of the
:code:`ListObjectsV2Output` class to access the objects' properties, such as :code:`key` for each object's name.

.. _aws-ruby-sdk-s3-example-create-buckets-copy:

Copy Files between Buckets
==========================

Call the :ruby-sdk-api:`copy_object <Aws/S3/Client.html#copy_object-instance_method>` method, specifying the name of the target bucket to receive the object (:code:`bucket`),
the names of the source bucket and object to copy over (:code:`copy_source`), and the name of the new object that is copied over into the target bucket (:code:`key`).

In this example, the name of the bucket containing the objects to copy over is :code:`#{my_bucket}`, which is the bucket named :code:`david-cloud`. After the copy operation,
:code:`test_file` in the :code:`david-cloud` bucket is renamed :code:`file2` in the :code:`doc-sample-bucket` bucket, and :code:`test_file1` in the :code:`david-cloud` bucket is renamed
:code:`file3` in the :code:`doc-sample-bucket` bucket.

.. _aws-ruby-sdk-s3-example-create-buckets-delete:

Delete Files from a Bucket
==========================

Call the :ruby-sdk-api:`delete_objects <Aws/S3/Client.html#delete_objects-instance_method>` method. For the :code:`delete` argument, use an instance of the
:ruby-sdk-api:`Aws::S3::Types::Delete <Aws/S3/Types/Delete.html>` type to represent the objects to delete. In this example, :code:`objects` represents two files to delete.

To confirm whether the files were deleted successfully, call the :code:`list_objects_v2` method as before. This time, when you use the :code:`contents` method of the
class, the deleted file names (represented here by :code:`key`) should not be displayed.

.. _aws-ruby-sdk-s3-example-create-buckets-code:

Complete Example
================

Here is the complete code for this example.

.. literalinclude:: ./example_code/s3/s3_ruby_create_bucket.rb
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-example-create-buckets-alternatives:

Alternative Approaches
======================

The following example creates a bucket named :code-ruby:`my-bucket` in the :code:`us-west-2` region. This example uses an instance of the
:ruby-sdk-api:`Aws::S3::Resource <Aws/S3/Resource.html>` class instead of the :code:`Aws::S3::Client` class.

.. code-block:: Ruby

  require 'aws-sdk-s3'  # v2: require 'aws-sdk'

  s3 = Aws::S3::Resource.new(region: 'us-west-2')
  s3.create_bucket(bucket: 'my-bucket')
