.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-bucket-cors:

###################################
Configuring an |S3| Bucket for CORS
###################################

.. meta::
    :description:
        Configure an Amazon S3 bucket for CORS using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

This example demonstrates how to use the |sdk-ruby| to:

#. Configure Cross-Origin Resource Sharing (CORS) settings for an |S3| bucket.
#. Get the CORS settings for a bucket.

For more information about CORS support in |S3|, see :S3-dg:`Cross-Origin Resource Sharing (CORS) <cors>` in the |S3-dg|.

For the complete code for this example, see :ref:`aws-ruby-sdk-s3-example-bucket-cors-code`.

.. _aws-ruby-sdk-s3-example-bucket-cors-prereqs:

Prerequisites
=============

To set up and run this example, you must first:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.
#. Create an |S3| bucket or identify an existing bucket in your AWS account.

Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example.

This example assumes:

* You have set the credentials in the AWS credentials profile file and the profile is named :code:`david`.
* Your bucket is named :code:`doc-sample-bucket`.

.. _aws-ruby-sdk-s3-example-bucket-cors-config:

Configure the SDK
=================

For this example, add a :code:`require` statement so that you can use the classes and methods
provided by the |sdk-ruby| for |S3|. Then create an :ruby-sdk-api:`Aws::S3::Client <Aws/S3/Client.html>` object in the AWS Region where you want to
create the bucket and the specified AWS profile.

.. _aws-ruby-sdk-s3-example-bucket-cors-configure:

Configure CORS for a Bucket
===========================

Call the :ruby-sdk-api:`put_bucket_cors <Aws/S3/Client.html#put_bucket_cors-instance_method>` method, providing the name of the bucket and the CORS configuration settings.

For the CORS configuration settings, declare an :ruby-sdk-api:`Aws::S3::Types::CORSConfiguration <Aws/S3/Types/CORSConfiguration.html>` hash. Specify things such as the HTTP methods
that the specified origins are allowed to execute (:code:`allowed_methods`), the origins you want customers to be able to access the bucket from (:code:`allowed_origins`), and
the headers in the response you want customers to be able to access from their applications (for example, from a JavaScript :code:`XMLHttpRequest` object, shown here in :code:`expose_headers`).

.. code-block:: Ruby

 s3.put_bucket_cors(
  bucket: bucket,
  cors_configuration: cors_configuration
 )

For the HTTP methods that the specified origins are allowed to execute, you could specify them inline or, as shown here, you could get them from the user at the command line.

.. code-block:: Ruby

 allowed_methods = []
 ARGV.each do |arg|
 case arg.upcase
 when "POST"
    allowed_methods << "POST"
  when "GET"
    allowed_methods << "GET"
  when "PUT"
    allowed_methods << "PUT"
  when "PATCH"
    allowed_methods << "PATCH"
  when "DELETE"
    allowed_methods << "DELETE"
  when "HEAD"
    allowed_methods << "HEAD"
  else
    puts "#{arg} is not a valid HTTP method"
  end
 end

For example, assuming the code file is named :code:`doc_sample_code_s3_bucket_cors.rb`, and you want to allow the specified origins to execute only GET and POST methods, here is how the user could
run the code from the command line.

.. code-block:: ruby

   ruby doc_sample_code_s3_bucket_cors.rb get post

.. _aws-ruby-sdk-s3-example-bucket-cors-settings:

Get the CORS Settings for a Bucket
==================================

Call the :ruby-sdk-api:`get_bucket_cors <Aws/S3/Client.html#get_bucket_cors-instance_method>` method, providing the name of the bucket. The :code:`get_bucket_cors` method returns an
:ruby-sdk-api:`Aws::S3::Types::GetBucketCorsOutput <Aws/S3/Types/GetBucketCorsOutput.html>` object. This object's :code:`cors_rules` attribute returns an array of
:ruby-sdk-api:`Aws::S3::Types::CORSRule <Aws/S3/Types/CORSRule.html>` objects, which represent the bucket's CORS settings.

.. _aws-ruby-sdk-s3-example-bucket-cors-code:

Complete Example
================

Here is the complete code for this example.

.. literalinclude:: ./example_code/s3/s3_ruby_bucket_cors.rb
   :dedent: 0
   :language: ruby
