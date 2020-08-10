.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-example-managing-instances:

########################
Managing |EC2| Instances
########################

.. meta::
   :description: Learn how to manage Amazon EC2 instances using this AWS SDK for Ruby code example.
   :keywords: AWS SDK for Ruby code examples, Amazon EC2


In this example, you use the |sdk-ruby| with |EC2| to:

#. Stop an existing |EC2| instance by using :aws-ruby-ec2-client-method:`stop_instances`.
#. Restart the instance by using :aws-ruby-ec2-client-method:`start_instances`.
#. Reboot the instance by using :aws-ruby-ec2-client-method:`reboot_instances`.
#. Enable detailed monitoring for the instance by using :aws-ruby-ec2-client-method:`monitor_instances`.
#. Get information about available instances by using :aws-ruby-ec2-client-method:`describe_instances`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

You also need to replace `INSTANCE-ID` in the code with the instance ID of an existing EC2 instance.

*******
Example
*******

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-manage-instances.rb
   :dedent: 0
   :language: ruby
