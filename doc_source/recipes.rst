.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-recipes:

##################
|sdk-ruby| Recipes
##################

This section provides the following recipes, which you can use to access AWS services using the
|sdk-ruby|.

:ref:`aws-ruby-sdk-cw-recipes`

    Demonstrates how to use the |sdk-ruby| with |CW| to:

    * Get information about all alarms

    * Create an alarm

:ref:`aws-ruby-sdk-dynamo-recipes`

    Demonstrates how to use the |sdk-ruby| with |DDB| to: 
     
    * Get information about all tables

    * Create a table

    * Add an item to a table

    * Get information about all table items

    * Get information about a specific table item

    * Update a table to include a new field

    * Create an index

:ref:`aws-ruby-sdk-ec2-recipes`

    Demonstrates how use to the |sdk-ruby| with |EC2| to:
         
    * Create a Virtual Private Cloud

    * Create an Internet Gateway

    * Create a Public Subnet

    * Create a Route Table

    * Create a Security Group

    * Create a Key-Pair

    * Get information about all instances

    * Get information about all instances with a specific tag value

    * Get information about a specific instance

    * Create an instances

    * Start, stop, and reboot an instance

    * Terminate an instance

:ref:`aws-ruby-sdk-eb-recipes`

    Demonstrates how to use the |sdk-ruby| with |AEB| to:
     
    * Get information about all applications

    * Get information about a specific application

    * Update a Ruby on Rails application

:ref:`aws-ruby-sdk-iam-recipes`

    Demonstrates how to use the |sdk-ruby| with |IAM| to:
     
    * Get information about all users

    * Add a new user

    * Create a user's access keys

    * Add a managed policy to a user

    * Create a role

:ref:`aws-ruby-sdk-lambda-recipes`

    Demonstrates how to use the |sdk-ruby| with |LAM| to:
     
    * Get information about all functions

    * Create a function

    * Configure a function to receive notifications

:ref:`aws-ruby-sdk-rds-recipes`

    Demonstrates how to use the |sdk-ruby| with |RDS| to:
     
    * Get information about all instances

    * Get information about all snapshots

    * Get information about all cluster and their snapshots

    * Get information about all security groups

    * Get information about all subnet groups

    * Get information about all parameter groups

    * Create an instance snapshot

    * Create a cluster snapshot

:ref:`aws-ruby-sdk-s3-recipes`

    Demonstrates how to use the |sdk-ruby| with |S3| to:
     
    * Get information about all buckets

    * Get information about all buckets in a region

    * Create a bucket

    * Determine whether a bucket exists or is accessible

    * Get information about all bucket items

    * Add an item to a bucket

    * Add an item with metadata to a bucket

    * Retrieve an item from a bucket

    * Change the properties of a bucket item

    * Trigger a notification when an item is added to a bucket

    * Create a bucket lifecycle template

:ref:`aws-ruby-sdk-sns-recipes`

    Demonstrates how to use the |sdk-ruby| with |SNS| to:
     
    * Get information about all topics

    * Create a topic

    * Get information about all of the subscribers to a topic

    * Add new subscriber to a topic

    * Send a message to all topic subscribers

:ref:`aws-ruby-sdk-sqs-recipes`

    Demonstrates how to use the |sdk-ruby| with |SQS| to:
     
    * Get information about all queues

    * Create a queue

    * Send messages through a queue

    * Get the messages in a queue

    * Poll the messages in a queue

    * Redirect dead letters in a queue

    * Delete a queue

.. include:: cw-recipes.rst

.. include:: dynamo-recipes.rst

.. include:: ec2-recipes.rst

.. include:: eb-recipes.rst

.. include:: iam-recipes.rst

.. include:: lambda-recipes.rst

.. include:: rds-recipes.rst

.. include:: s3-recipes.rst

.. include:: sns-recipes.rst

.. include:: sqs-recipes.rst


