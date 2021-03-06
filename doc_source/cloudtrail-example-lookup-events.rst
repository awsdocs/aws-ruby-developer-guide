.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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


.. literalinclude:: ./example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb
   :dedent: 0
   :language: ruby


See the `complete example <https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb>`_
on GitHub.
