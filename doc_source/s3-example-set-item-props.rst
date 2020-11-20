.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-set-item-props:

#################################################
Changing the Properties for an |S3| Bucket Object
#################################################

.. meta::
    :description:
        Change Amazon S3 bucket object properties using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples

The following code example copies an object from one |S3| bucket to another. It also sets a predetermined access control list (ACL) and an |S3| storage class on the copied object.

.. literalinclude:: ./example_code/s3/s3-ruby-example-set-item-props.rb
   :dedent: 0
   :language: ruby
