.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-example-get-instances:

#############################################
Getting Information about All |EC2| Instances
#############################################

.. meta::
    :description:
        Get EC2 instance information using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code example, Amazon EC2

The following example lists the IDs and states (pending, running, shutting down, terminated, stopping, or stopped)
for all of your |EC2| instances in the :code:`us-west-2` region.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-get-all-instance-info.rb
   :dedent: 0
   :language: ruby
