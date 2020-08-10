.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. Example at https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/s3/s3_ruby_bucket_website.rb

.. _aws-ruby-sdk-s3-example-bucket-website:

#####################################
Using a |S3| Bucket to Host a Website
#####################################

.. meta::
    :description:
        Use an Amazon S3 bucket to host a website using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

This example demonstrates how to use the |sdk-ruby| to:

#. Create an |S3| bucket.
#. Get the bucket website's configuration.
#. Add objects to the bucket.
#. Set the bucket website's configuration.
#. Access the bucket website's documents.
#. Delete the bucket website.
#. Delete the bucket.

For information about bucket website hosting, see :S3-dg:`Configure a Bucket for Website Hosting <HowDoIWebsiteConfiguration>` in the |S3-dg|.

For the complete code for this example, see :ref:`aws-ruby-sdk-s3-example-bucket-website-code`.

.. _aws-ruby-sdk-s3-example-bucket-website-prereqs:

Prerequisites
=============

To set up and run this example, you must first:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.

Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example.

This example assumes you have set the credentials in the AWS credentials profile file or in the
:envvar:`AWS_ACCESS_KEY_ID` and :envvar:`AWS_SECRET_ACCESS_KEY` environment variables on your local system.

.. _aws-ruby-sdk-s3-example-bucket-website-config:

Configure the SDK
=================

For this example, add a :code:`require` statement so that you can use the classes and methods
provided by the |sdk-ruby| for |S3|. Then create an :ruby-sdk-api:`Aws::S3::Client <Aws/S3/Client.html>` object in the AWS Region where you want to
create the bucket and the specified AWS profile. This code creates the :code:`Aws::S3::Client` object
in the :code:`us-east-2` region.

An additional variable is also declared for the bucket used in this example. To help ensure the bucket name is unique across all AWS accounts, an
additional :code:`require` statement is added, and the :code:`SecureRandom` module's
:code:`uuid` method is called to generate a unique identifier. This identifier is inserted into the
name of the bucket to be created later in the example.

.. _aws-ruby-sdk-s3-example-bucket-website-create-bucket:

Create a Bucket
===============

Call the :ruby-sdk-api:`create_bucket <Aws/S3/Client.html#create_bucket-instance_method>` method, supplying the name of the bucket to create.

.. code-block:: Ruby

  s3 = Aws::S3::Client.new(region: "us-west-2")

.. _aws-ruby-sdk-s3-example-bucket-website-get-config:

Get a Bucket Website's Configuration
====================================

Call the :ruby-sdk-api:`get_bucket_website <Aws/S3/Client.html#get_bucket_website-instance_method>` method, supplying the name of the bucket.
By default, a bucket is not configured as a website. To confirm this behavior, call the
:code:`get_bucket_website` method. This returns an error, because there is no website configuration for the bucket.

.. _aws-ruby-sdk-s3-example-bucket-website-add-object:

Add an Object to a Bucket
=========================

Call the :ruby-sdk-api:`put_object <Aws/S3/Client.html#put_object-instance_method>` method, supplying the name of the bucket and object,
the object's contents, and the object's access permissions set. This example adds two
webpages to the bucket.

.. _aws-ruby-sdk-s3-example-bucket-website-set-config:

Set a Bucket Website's Configuration
====================================

Call the :ruby-sdk-api:`put_bucket_website <Aws/S3/Client.html#put_bucket_website-instance_method>` method, supplying the name of the bucket and
the website configuration. For the website configuration, use an :ruby-sdk-api:`Aws::S3::Types::WebsiteConfiguration <Aws/S3/Types/WebsiteConfiguration.html>` hash, supplying the website's
index and error webpages.

.. _aws-ruby-sdk-s3-example-bucket-website-get-docs:

Access a Bucket Website's Documents
===================================

Call the Ruby :code:`Net::HTTP.get` method, supplying the address to the document in the bucket website.

.. _aws-ruby-sdk-s3-example-bucket-website-delete:

Delete a Bucket Website
=======================

Call the :ruby-sdk-api:`delete_bucket_website <Aws/S3/Client.html#delete_bucket_website-instance_method>` method, supplying the name of the bucket.

.. _aws-ruby-sdk-s3-example-bucket-website-delete-bucket:

Delete a Bucket
===============

Call the :ruby-sdk-api:`bucket <Aws/S3/Resource.html#bucket-instance_method>` method of an :ruby-sdk-api:`Aws::S3::Resource <Aws/S3/Resource.html>` object, supplying the name of the bucket.
This returns an :ruby-sdk-api:`Aws::S3::Bucket <Aws/S3/Bucket.html>` object. Then call the :code:`Aws::S3::Bucket` object's
:ruby-sdk-api:`delete <Aws/S3/Bucket.html#delete!-instance_method>` method.

.. _aws-ruby-sdk-s3-example-bucket-website-code:

Complete Example
================

Here is the complete code for this example.

.. literalinclude:: ./example_code/s3/s3_ruby_bucket_website.rb
   :dedent: 0
   :language: ruby
