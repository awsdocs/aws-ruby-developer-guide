.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _lambda-ruby-example-create-function:

#########################
Creating a |LAM| Function
#########################

.. meta::
    :description:
        Create an AWS Lambda function using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Lambda

The following example creates the |LAM| function named :code:`my-notification-function` in the :code:`us-west-2`
region using these values:

* Role ARN: :code:`my-resource-arn`. In most cases, you need to attach only the :code:`AWSLambdaExecute` managed policy to the policy for this role.

* Function entry point: :code:`my-package.my-class`

* Runtime: :code:`java8`

* Zip file: :code:`my-zip-file.zip`

* Bucket: :code:`my-notification-bucket`

* Key: :code:`my-zip-file`

.. literalinclude:: ./lambda/aws-ruby-sdk-lambda-example-create-function.rb
   :lines: 13-32
   :dedent: 0
   :language: ruby
