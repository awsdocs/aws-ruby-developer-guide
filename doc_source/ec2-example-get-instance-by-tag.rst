.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-example-get-instance-by-tag:

#######################################################################
Getting Information about All |EC2| Instances with a Specific Tag Value
#######################################################################

.. meta::
    :description:
        Get information for all Amazon EC2 instances by tag value using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following example lists the ID and state (pending, running, shutting down, terminated, stopping, or stopped)
of an |EC2| instance with the tag :code:`Group` and tag value :code:`MyGroovyGroup` in the :code:`us-west-2` region.

.. note:: The tag name and value are case-sensitive.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-get-instance-info-by-tag.rb
   :dedent: 0
   :language: ruby
