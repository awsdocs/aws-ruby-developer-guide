.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-s3-example-set-item-props:

#########################################
Changing the Properties for a Bucket Item
#########################################

The following example adds public read-only access, sets server-side encryption to AES-256, and sets
the storage class to Reduced Redundancy for the item :code-ruby:`my-item` in the bucket
:code-ruby:`my-bucket` in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/s3/s3-ruby-example-set-item-props.rb
   :lines: 13-36
   :dedent: 0
   :language: ruby