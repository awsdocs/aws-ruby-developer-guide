.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-tips:

#####################
|EC2| Tips and Tricks
#####################

.. meta::
    :description:
        Learn tips and tricks for using Amazon EC2 with the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby, Amazon EC2

This section provides some tips to help you use the |sdk-ruby| with |EC2long| (|EC2|) services. For
more information about |EC2|, see the |EC2-gsg|_.

.. _aws-ruby-sdk-ec2-tip-switch-elastic-ips:

Switching Elastic IPs
=====================

The following example associates the Elastic IP address with the instance represented by
:code-ruby:`i-12345678`.

.. code-block:: ruby

    ec2 = Aws::EC2::Client.new

    resp = ec2.allocate_address
    ec2.associate_address(instance_id:"i-12345678", allocation_id: resp.allocation_id)
