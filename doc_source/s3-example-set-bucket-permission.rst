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

The following code example shows how to: 

#. Set the initial access level of an |S3| bucket to private.
#. Attempt to access and upload an object to the bucket, which should fail.
#. Set the access level to public-read.
#. Attempt to access and upload an object to the bucket, which should now succeed.
#. Set the access level back to private.
#. Attempt to access and upload an object to the bucket, which should now fail.

.. literalinclude:: ./example_code/s3/s3-ruby-example-access-permissions.rb
   :dedent: 0
   :language: ruby
