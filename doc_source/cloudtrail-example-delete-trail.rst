.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cloudtrail-example-delete-trail:

#####################
Deleting a |CT| Trail
#####################

.. meta::
    :description:
        Delete an |CTlong| trail using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, CloudTrail

This example uses the
:ruby-sdk-api:`delete_trail <Aws/CloudTrail/Client.html#delete_trail-instance_method>` method
to delete a |CT| trail
in the :code:`us-west-2` region.
It requires one input, the name of the trail.

Choose :code:`Copy` to save the code locally.

.. literalinclude:: ./example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-delete-trail.rb
   :dedent: 0
   :language: ruby

See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-delete-trail.rb>`_
on GitHub.
