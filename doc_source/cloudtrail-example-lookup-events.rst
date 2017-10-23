.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cloudtrail-example-lookup-events:

#########################
Listing |CT| Trail Events
#########################

.. meta::
    :description:
        List the |CTlong| trails using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, CloudTrail

This example uses the
:ruby-sdk-api:`lookup_events <Aws/CloudTrail/Client.html#lookup_events-instance_method>` method
to list the |CT| trail events
in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *lookup_events.rb*.
Add the following statement to use the **CloudTrail** gem of the |sdk-ruby|.

.. literalinclude:: ./example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Create a function to display information about each event.

.. literalinclude:: ./example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb
   :lines: 15-28
   :dedent: 0
   :language: ruby

Create a |CT| client in :code:`us-west-2`,
call **lookup_events**,
and use the **show_event** function to display information about each event.

.. literalinclude:: ./example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb
   :lines: 31-41
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb>`_
on GitHub.
