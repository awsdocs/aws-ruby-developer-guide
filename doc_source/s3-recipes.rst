.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-recipes:

############
|S3| Recipes
############

This section provides some recipes you can use to access |S3long| (|S3|) using the |sdk-ruby|. For
more information about |S3|, see the `Amazon S3 documentation <http://aws.amazon.com/documentation/s3/>`_.

This section contains the following recipes:

* :ref:`aws-ruby-sdk-s3-recipe-get-buckets`

* :ref:`aws-ruby-sdk-s3-recipe-get-buckets-in-region`

* :ref:`aws-ruby-sdk-s3-recipe-create-buckets`

* :ref:`aws-ruby-sdk-s3-recipe-does-bucket-exist`

* :ref:`aws-ruby-sdk-s3-recipe-get-bucket-items`

* :ref:`aws-ruby-sdk-s3-recipe-upload-bucket-item`

* :ref:`aws-ruby-sdk-s3-recipe-upload-bucket-item-with-metadata`

* :ref:`aws-ruby-sdk-s3-recipe-get-bucket-item`

* :ref:`aws-ruby-sdk-s3-recipe-set-item-props`

* :ref:`aws-ruby-sdk-s3-recipe-add-notification`

* :ref:`aws-ruby-sdk-s3-recipe-create-policy-template`

.. _aws-ruby-sdk-s3-recipe-get-buckets:

Getting Information About All Buckets
=====================================

The following example lists the names of up to 50 of your S3 buckets.
Copy the code and save it as :file:`buckets.rb`.
Note that although the Resource object is created in the region :code:`us-west-2`,
|S3| returns buckets to which you have access, regardless of the region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-show-50-buckets.rb
   :lines: 13-20
   :dedent: 0
   :language: ruby

.. note:: You might think that by specifying a region,
   the :code:`buckets` method would only return buckets in that region.
   That is not the case. If you read the documentation,
   it states that the :code:`buckets` method calls the :code:`Client#list_buckets` method,
   which itself states "Returns a list of all buckets owned by the authenticated sender of the request".
   In the next recipe we will show you how to filter this list to get only the buckets in a specific region.

.. _aws-ruby-sdk-s3-recipe-get-buckets-in-region:

Getting Information About All Buckets in a Region
=================================================

The following example lists the names of the first 50 buckets for the bucket in the region :code:`us-west-2`.
If a limit is not specified, |S3| lists all of the buckets in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-show-buckets-in-region.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby

.. note:: One more tidbit.
   If the bucket is not in the region in which you instantiated your :code-ruby:`Resource` object,
   the SDK emits a warning message when you call :code-ruby:`get_bucket_location`.
   You can suppress this message by redirecting STDERR.

   On Windows, append :code:`2> nul` to the command.

   On Linux or iOS, append :code:`2> /dev/null` to the command.

.. _aws-ruby-sdk-s3-recipe-create-buckets:

Creating a Bucket
=================

The following example creates a bucket with the name :code-ruby:`my-bucket` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-create-bucket.rb
   :lines: 13-16
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-does-bucket-exist:

Determining Whether a Bucket Exists
===================================

There are two use cases for determining whether a bucket exists. You perform these tests in lieu of
receiving an exception if the condition fails.

* You want to determine whether a bucket with that name exists among all buckets,
  even ones to which you do not have access.
  This test helps prevent you from attempting to create a bucket with the name of an existing bucket,
  which causes an exception.

* You want to perform an operation,
  such as add an item to a bucket, only on a bucket to which you have access.

The following example sets :code-ruby:`bucket_exists` to **true** if a a bucket with the name :code-ruby:`my-bucket` exists.
Note that the region: parameter to **Resource** has no effect on the result.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-bucket-exists.rb
   :lines: 13-16
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-get-bucket-items:

Getting Information About Bucket Items
======================================

A presigned URL gives you access to the object identified in the URL, provided that the creator of
the presigned URL has permissions to access that object. You can use a presigned URL to allow a user
to click on a link and see an item without having to make the item public.

The following example lists the names and presigned URLs of the first 50 items of the bucket :code-ruby:`my-bucket` in the region :code:`us-west-2`.
If a limit is not specified, |S3| lists up to 1000 items.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-list-bucket-items.rb
   :lines: 13-23
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-upload-bucket-item:

Uploading an Item to a Bucket
=============================

The following example uploads the item (file) :file:`C:\file.txt` to the bucket :code-ruby:`my-bucket` in the region :code:`us-west-2`.
Because :file:`C:\file.txt` is the fully-qualified name of the file, the name of the item is set to the name of the file.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-upload-item.rb
   :lines: 13-27
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-upload-bucket-item-with-metadata:

Uploading an Item With Metadata to a Bucket
===========================================

The following example uploads the item (file) :file:`C:\file.txt` with the metadata key-value pair :code-ruby:`answer` and :code-ruby:`42`
to the bucket :code-ruby:`my-bucket` in the region :code:`us-west-2`.
Because :file:`C:\file.txt` is the fully-qualified name of the file, the name of the item is set to the name of the file.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-upload-item-with-metadata.rb
   :lines: 13-30
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-get-bucket-item:

Downloading an Object from a Bucket into a File
===============================================

The following example gets the contents of the item :code-ruby:`my-item` from the bucket :code-ruby:`my-bucket` in the region :code:`us-west-2`,
and saves it to the file :file:`my-item.txt` in the directory :file:`./my-code`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-get-item.rb
   :lines: 13-21
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-set-item-props:

Changing the Properties for a Bucket Item
=========================================

The following example adds public read-only access, sets server-side encryption to AES-256,
and sets the storage class to reduced redundancy for the item :code-ruby:`my-item` in the bucket :code-ruby:`my-bucket` in the region :code:`us-west-2`.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-set-item-props.rb
   :lines: 13-36
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-add-notification:

Triggering a Notification when an Item is Added to a Bucket
===========================================================

You can trigger a notification when there is a change in the objects in a bucket. These changes
include:

* An object is added to the bucket

* An object is removed from the bucket

* An object stored with Reduced Redundancy has been lost

You can configure the service to send a notification to:

* An |SNS| topic

* An |SQS| queue

* A |LAM| function

To create a bucket notification:

1. :ref:`Grant S3 permission to publish an item to a queue or topic, or invoke a Lambda function
   <aws-ruby-sdk-s3-recipe-grant-s3-permission>`

2. :ref:`Set the bucket's Notification Configuration to point to the queue, topic, or function
   <aws-ruby-sdk-s3-recipe-set-notification>`

Once you have performed these steps your application can respond to the information. For example,
the |LAM| topic `Programming Model </programming-model-v2.html>`_ describes how to use the various
programming languages that |LAM| supports.

.. _aws-ruby-sdk-s3-recipe-grant-s3-permission:

Enabling |S3| to Send a Notification
------------------------------------

Learn how to configure an |SNS| topic or |SQS| queue, or create a |LAM| function so that |S3| can send
a notification to them.

* :ref:`aws-ruby-sdk-sns-recipe-enable-resource`

* :ref:`aws-ruby-sdk-sqs-recipe-enable-resource`

* :ref:`lambda-ruby-example-configure-function-for-notification`

.. _aws-ruby-sdk-s3-recipe-set-notification:

Creating an |S3| Bucket Notification
------------------------------------

The following example enables the |S3| bucket :code-ruby:`my-bucket` to send a notification to the following when an item is added to the bucket:

* The |SNS| topic with the ARN :code-ruby:`my-topic-arn`

* The |SQS| queue with the ARN :code-ruby:`my-queue-arn`

* The |LAM| function with the ARN :code-ruby:`my-function-arn`

.. literalinclude:: ../build_dependencies/1/ruby/example_code/s3/s3-ruby-example-add-notification.rb
   :lines: 13-58
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-s3-recipe-create-policy-template:

Creating a Bucket LifeCycle Rule Configuration Template
=======================================================

If you have (or plan to create) a non-trivial number of objects and want to specify when to move
them to long-term storage or delete them, you can save yourself a lot of time by creating a template
for the lifecycle rules and apply that template to your buckets. This section describes how you can
create such a template and apply it to all of your buckets.

The process takes the following steps:

1. Manually modify the lifecycle settings on an existing bucket.

2. Save the rules.

3. Apply the rules to your other buckets.

Given the following rule:

.. image:: images/DefaultRule.png
    :scale: 65

Run the following code to produce a JSON representation of that rule. Save the output as
:file:`default.json`.

.. code-block:: ruby

    require 'aws-sdk'

    s3 = Aws::S3::Client.new(region: 'us-west-2')
    resp = s3.get_bucket_lifecycle_configuration(bucket: 'default')

    resp.rules.each do |rule|
      rule.to_hash.to_json
    end

The output should look something like the following:

.. code-block:: json

    [{"expiration":{"date":null,"days":425},"id":"default","prefix":"","status":"Enabled","transitions":[{"date":null,"days":30,"storage_class":"STANDARD_IA"},{"date":null,"days":60,"storage_class":"GLACIER"}],"noncurrent_version_transitions":[],"noncurrent_version_expiration":null}]

Now that you have the JSON for a life-cycle rule, you can apply it to any other bucket using the
following example,which takes the rule from :file:`default.json` and applies it to the bucket
:code-ruby:`other_bucket`:

.. code-block:: ruby

    require 'aws-sdk'
    require 'json'

    class Aws::S3::Types::LifecycleExpiration
      def to_map
        map = Hash.new
        self.members.each { |m| map[m] = self[m] }
        map
      end

      def to_json(*a)
        to_map.to_json(*a)
      end
    end

    class Aws::S3::Types::Transition
      def to_map
        map = Hash.new
        self.members.each { |m| map[m] = self[m] }
        map
      end

      def to_json(*a)
        to_map.to_json(*a)
      end
    end

    class Aws::S3::Types::LifecycleRule
      def to_map
        map = Hash.new
        self.members.each { |m| map[m] = self[m] }
        map
      end

      def to_json(*a)
        to_map.to_json(*a)
      end
    end

    # Suck in contents as a string
    value = File.open('default.json', "rb").read
    json_data = JSON.parse(value, opts={symbolize_names: true})

    s3 = Aws::S3::Client.new(region: 'us-west-2')
    s3.put_bucket_lifecycle_configuration(:bucket => 'other_bucket', :lifecycle_configuration => {:rules => json_data})
