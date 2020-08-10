.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _polly-example-describe-voices:

########################
Getting a List of Voices
########################

.. meta::
    :description:
        Get the list of voices that are available for use when requesting speech synthesis using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon Polly

This example uses the
:ruby-sdk-api:`describe_voices <Aws/Polly/Client.html#describe_voices-instance_method>`
method to get the list of US English voices in the :code:`us-west-2` region.

Choose :code:`Copy` to save the code locally.

Create the file *polly_describe_voices.rb*.

Add the required gem.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/polly/polly_describe_voices.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/polly/polly_describe_voices.rb>`_
on GitHub.
