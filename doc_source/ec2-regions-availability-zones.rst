.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-regions-availability-zones:

##################################################################
Getting Information about Regions and Availability Zones for |EC2|
##################################################################

.. meta::
   :description: Get information about AWS Regions and Availability Zones for Amazon EC2 using this code example for the AWS SDK for Ruby.
   :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following examples show you how to use the |sdk-ruby| together with |EC2| to:

* Get information about available |EC2| regions and their endpoints.
* Get information about available |EC2| Availability Zones.

For more information about |EC2| regions and Availability Zones, see :EC2-ug:`Regions and Availability Zones <using-regions-availability-zones>` in the |EC2-ug|.

For additional code that you can use to run these examples, see the :ref:`aws-ruby-sdk-ec2-regions-availability-zones-code`.

.. _aws-ruby-sdk-ec2-regions-availability-zones-regions-endpoints:

Get Information about Regions and Endpoints
===========================================

To get information about available regions, call the :ruby-sdk-api:`describe_regions
<Aws/EC2/Client.html#describe_regions-instance_method>` method.

.. code-block:: Ruby

  describe_regions_result = ec2.describe_regions()

In this code, :code:`ec2` is a variable representing an :ruby-sdk-api:`Aws::EC2::Client <Aws/EC2/Client.html>` object. For more information,
see the :ref:`aws-ruby-sdk-ec2-regions-availability-zones-code`.

To get the region names and endpoints:

#. Get an :ruby-sdk-api:`Aws::EC2::Types::DescribeRegionsResult <Aws/EC2/Types/DescribeRegionsResult.html>` object,
   which is returned by the :code:`describe_regions` method and represented in this code by the :code:`describe_regions_result` variable.
#. Use the :code:`DescribeRegionsResult` object's :ruby-sdk-api:`regions <Aws/EC2/Types/DescribeRegionsResult.html#regions-instance_method>` attribute to get
   an array of :ruby-sdk-api:`Aws::EC2::Types::Region <Aws/EC2/Types/Region.html>` objects representing the regions.
#. Get each region's name and endpoint by using the :code:`Region` object's :ruby-sdk-api:`region_name <Aws/EC2/Types/Region.html#region_name-instance_method>` and
   :ruby-sdk-api:`endpoint <Aws/EC2/Types/Region.html#endpoint-instance_method>` attributes.

.. code-block:: Ruby

   describe_regions_result.regions.each do |region|
     puts "#{region.region_name} (#{region.endpoint})"
   end

.. _aws-ruby-sdk-ec2-regions-availability-zones-availability-zones:

Get Information about Availability Zones
========================================

To get information about Availability Zones, call the :ruby-sdk-api:`describe_availability_zones
<Aws/EC2/Client.html#describe_availability_zones-instance_method>` method.

.. code-block:: Ruby

  describe_availability_zones_result = ec2.describe_availability_zones()

The :ruby-sdk-api:`Aws::EC2::Types::DescribeAvailabilityZonesResult <Aws/EC2/Types/DescribeAvailabilityZonesResult.html>` object contains an array of
:ruby-sdk-api:`Aws::EC2::Types::AvailabilityZone <Aws/EC2/Types/AvailabilityZone.html>` objects representing the Availability Zones.
The :code:`DescribeAvailabilityZonesResult` object is returned by the :code:`describe_availability_zones`
method and represented in this code by the :code:`describe_availability_zones_result` variable.

In this code, :code:`ec2` is a variable representing an :ruby-sdk-api:`Aws::EC2::Client <Aws/EC2/Client.html>` object. For more information,
see the :ref:`aws-ruby-sdk-ec2-regions-availability-zones-code`.

To get the name and state of each Availability Zone, use the :code:`AvailabilityZone` object's
:ruby-sdk-api:`zone_name <Aws/EC2/Types/AvailabilityZone.html#zone_name-instance_method>` and
:ruby-sdk-api:`state <Aws/EC2/Types/AvailabilityZone.html#state-instance_method>` attributes.

.. code-block:: Ruby

 describe_availability_zones_result.availability_zones.each do |zone|
 puts "#{zone.zone_name} is #{zone.state}"
 if zone.messages.count > 0
   zone.messages.each do |message|
     puts "  #{message.message}"
   end
 end
 end

To get any messages about Availability Zones:

#. Use the :code:`AvailabilityZone` object's :ruby-sdk-api:`messages <Aws/EC2/Types/AvailabilityZone.html#messages-instance_method>` attribute, which
   returns an :ruby-sdk-api:`Aws::EC2::Types::AvailabilityZoneMessage <Aws/EC2/Types/AvailabilityZoneMessage.html>` array.
#. If there is at least one message in the array, use each :code:`AvailabilityZoneMessage` object's
   :ruby-sdk-api:`message <Aws/EC2/Types/AvailabilityZoneMessage.html#message-instance_method>` attribute to get the message.

.. _aws-ruby-sdk-ec2-regions-availability-zones-code:

Complete Example
================

The following code, which you can adapt and run, combines the preceding examples into a single example.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-regions-availability-zones.rb
   :dedent: 0
   :language: ruby

To run this code:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.
   Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example. This example assumes you
   have set the credentials in the AWS credentials profile file or in the :envvar:`AWS_ACCESS_KEY_ID` and :envvar:`AWS_SECRET_ACCESS_KEY` environment variables on your local system.
