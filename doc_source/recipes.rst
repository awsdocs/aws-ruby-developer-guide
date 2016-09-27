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

<<<<<<< HEAD
This section provides the following recipes that you can use to access AWS services using the
=======
This section provides recipes you can use to access AWS services by using the
>>>>>>> aws-ruby-developer-guide-editsBA
|sdk-ruby|.

.. toctree::
    :titlesonly:
    :maxdepth: 1

   cw-recipes
   dynamo-recipes
   ec2-recipes
   eb-recipes
   iam-recipes
   lambda-recipes
   rds-recipes
   s3-recipes
   sns-recipes
   sqs-recipes

:ref:`aws-ruby-sdk-cw-recipes`

    * :ref:`aws-ruby-sdk-cw-recipe-show_alarms`

    * :ref:`aws-ruby-sdk-cw-recipe-create_alarm`


:ref:`aws-ruby-sdk-dynamo-recipes`
     
    * :ref:`aws-ruby-sdk-dynamo-recipe-get-tables`

	* :ref:`aws-ruby-sdk-dynamo-recipe-create-table`

	* :ref:`aws-ruby-sdk-dynamo-recipe-add-item-to-table`

	* :ref:`aws-ruby-sdk-dynamo-recipe-list-table-items`

	* :ref:`aws-ruby-sdk-dynamo-recipe-get-table-item`

	* :ref:`aws-ruby-sdk-dynamo-recipe-update-table`

	* :ref:`aws-ruby-sdk-dynamo-recipe-create-index`


:ref:`aws-ruby-sdk-ec2-recipes`
         
	* :ref:`aws-ruby-sdk-ec2-create-vpc`

	* :ref:`aws-ruby-sdk-ec2-attach-igw-vpc`

	* :ref:`aws-ruby-sdk-ec2-create-subnet`

	* :ref:`aws-ruby-sdk-ec2-create-route-table`

	* :ref:`aws-ruby-sdk-ec2-create-security-group`

	* :ref:`aws-ruby-sdk-ec2-create-key-pair`

	* :ref:`aws-ruby-sdk-ec2-recipe-get-instances`

	* :ref:`aws-ruby-sdk-ec2-recipe-get-instance-by-tag`

	* :ref:`aws-ruby-sdk-ec2-recipe-get-instance`

	* :ref:`aws-ruby-sdk-ec2-recipe-create-instance`

	* :ref:`aws-ruby-sdk-ec2-recipe-stop-instance`

	* :ref:`aws-ruby-sdk-ec2-recipe-start-instance`

	* :ref:`aws-ruby-sdk-ec2-recipe-reboot-instance`

	* :ref:`aws-ruby-sdk-ec2-recipe-terminate-instance`


:ref:`aws-ruby-sdk-eb-recipes`
     
	* :ref:`aws-ruby-sdk-eb-recipe-get-apps`

	* :ref:`aws-ruby-sdk-eb-recipe-get-app`

	* :ref:`aws-ruby-sdk-eb-recipe-update-ruby-on-rails-app`


:ref:`aws-ruby-sdk-iam-recipes`
     
	* :ref:`aws-ruby-sdk-iam-recipe-get-users`

	* :ref:`aws-ruby-sdk-iam-recipe-add-user`

	* :ref:`aws-ruby-sdk-iam-recipe-create-user-access-keys`

	* :ref:`aws-ruby-sdk-iam-recipe-add-managed-policy`

	* :ref:`aws-ruby-sdk-iam-recipe-create-role`


:ref:`aws-ruby-sdk-lambda-recipes`
     
	* :ref:`lambda-ruby-example-show-functions`

	* :ref:`lambda-ruby-example-create-function`

	* :ref:`lambda-ruby-example-configure-function-for-notification`


:ref:`aws-ruby-sdk-rds-recipes`
     
	* :ref:`aws-ruby-sdk-rds-recipe-get-instances`

	* :ref:`aws-ruby-sdk-rds-recipe-get-snapshots`

	* :ref:`aws-ruby-sdk-rds-recipe-get-cluster-snapshots`

	* :ref:`aws-ruby-sdk-rds-recipe-get-security_groups`

	* :ref:`aws-ruby-sdk-rds-recipe-get-subnet-groups`

	* :ref:`aws-ruby-sdk-rds-recipe-get-parameter_groups`

	* :ref:`aws-ruby-sdk-rds-recipe-create-snapshot`

	* :ref:`aws-ruby-sdk-rds-recipe-create-cluster-snapshot`


:ref:`aws-ruby-sdk-s3-recipes`
     
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


:ref:`aws-ruby-sdk-sns-recipes`
     
	* :ref:`aws-ruby-sdk-sns-recipe-show-topics`

	* :ref:`aws-ruby-sdk-sns-recipe-create-topic`

	* :ref:`aws-ruby-sdk-sns-recipe-show-subscriptions`

	* :ref:`aws-ruby-sdk-sns-recipe-create-subscription`

	* :ref:`aws-ruby-sdk-sns-recipe-send-message`

	* :ref:`aws-ruby-sdk-sns-recipe-enable-resource`


:ref:`aws-ruby-sdk-sqs-recipes`
     
	* :ref:`aws-ruby-sdk-sqs-recipe-show-queues`

	* :ref:`aws-ruby-sdk-sqs-recipe-create-queue`

	* :ref:`aws-ruby-sdk-sqs-recipe-send-messages`

	* :ref:`aws-ruby-sdk-sqs-recipe-get-messages`

	* :ref:`aws-ruby-sdk-sqs-recipe-get-messages-with-long-polling`

	* :ref:`aws-ruby-sdk-sqs-recipe-poll-messages`

	* :ref:`aws-ruby-sdk-sqs-recipe-redirect-deadletters`

	* :ref:`aws-ruby-sdk-sqs-recipe-delete_queue`

<<<<<<< HEAD
=======
	* :ref:`aws-ruby-sdk-sqs-recipe-enable-resource`
	
	
.. include:: cw-recipes.rst

.. include:: dynamo-recipes.rst

.. include:: ec2-recipes.rst

.. include:: eb-recipes.rst

.. include:: iam-recipes.rst

.. include:: lambda-recipes.rst

.. include:: rds-recipes.rst

.. include:: s3-recipes.rst

.. include:: sns-recipes.rst
>>>>>>> aws-ruby-developer-guide-editsBA



