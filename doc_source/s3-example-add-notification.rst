.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-add-notification:

#################################################################
Triggering a Notification When an Item is Added to an |S3| Bucket
#################################################################

.. meta::
    :description:
        Trigger a notification when items in an Amazon S3 bucket change using this AWS
        SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon S3

You can trigger a notification when there is a change in the objects in a bucket. These changes
include:

* When an object is added to the bucket

* When an object is removed from the bucket

* When an object stored with Reduced Redundancy is lost

You can configure the service to send a notification to:

* An |SNS| topic

* An |SQS| queue

* A |LAMlong| function

To create a bucket notification, use the following procedure.

1. :ref:`Grant Amazon S3 permission to publish an item to a queue or topic, or invoke a Lambda function
   <aws-ruby-sdk-s3-example-grant-s3-permission>`.

2. :ref:`Set the bucket's Notification Configuration to point to the queue, topic, or function
   <aws-ruby-sdk-s3-example-set-notification>`.

After you do these steps, your application can respond to the information. For example,
the |LAM| topic
:LAM-dg:`Programming Model <programming-model-v2>` describes how to use the various
programming languages that |LAM| supports.

.. _aws-ruby-sdk-s3-example-grant-s3-permission:

Enabling |S3| to Send a Notification
------------------------------------

Learn how to configure an |SNS| topic or |SQS| queue, or create a |LAM| function so that
|S3| can send a notification to them.

* :ref:`aws-ruby-sdk-sns-example-enable-resource`

* :ref:`aws-ruby-sdk-sqs-example-enable-resource`

* :ref:`lambda-ruby-example-configure-function-for-notification`

.. _aws-ruby-sdk-s3-example-set-notification:

Creating an |S3| Bucket Notification
------------------------------------

This example enables the |S3| bucket :code-ruby:`my-bucket` to send a notification to the
following when an item is added to the bucket:

* The |SNS| topic with the ARN :code-ruby:`my-topic-arn`

* The |SQS| queue with the ARN :code-ruby:`my-queue-arn`

* The |LAM| function with the ARN :code-ruby:`my-function-arn`

.. literalinclude:: ./example_code/s3/s3-ruby-example-add-notification.rb
   :dedent: 0
   :language: ruby
