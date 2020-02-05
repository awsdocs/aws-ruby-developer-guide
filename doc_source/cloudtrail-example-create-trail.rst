.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cloudtrail-example-create-trail:

#####################
Creating a |CT| Trail
#####################

.. meta::
    :description:
        Create an |CTlong| trail using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, CloudTrail

This example uses the
:ruby-sdk-api:`create_trail <Aws/CloudTrail/Client.html#create_trail-instance_method>` method
to create a |CT| trail
in the :code:`us-west-2` region.
It requires two inputs, the name of the trail and the name of the bucket
in which |CT| stores information.
If the bucket does not have the proper policy,
include the **-p** flag to attach the correct policy to the bucket.

Choose :code:`Copy` to save the code locally.

Create the file *create_trail.rb*.
Add the following statements to use the **CloudTrail**, **STS**, and **S3** gems of the |sdk-ruby|.

.. literalinclude:: ./cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb
   :lines: 13-15
   :dedent: 0
   :language: ruby

Create a function to add a policy to the bucket that gives |CT| permission to save data to the bucket.

.. literalinclude:: ./cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb
   :lines: 18-68
   :dedent: 0
   :language: ruby

Get the names of the trail and bucket,
and whether to attach the policy to the bucket.
If either the trail name or bucket name is missing,
display an error message and exit.

.. literalinclude:: ./cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb
   :lines: 71-97
   :dedent: 0
   :language: ruby

If the **-p** flag was specified, call **add_policy** to attach the policy to the bucket.

.. literalinclude:: ./cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb
   :lines: 99-101
   :dedent: 0
   :language: ruby

Create the |CT| client and call **create_trail** to create the trail.
If any errors occur, print the error and quit,
otherwise print a success message.

.. literalinclude:: ./cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb
   :lines: 104-117
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/cloudtrail/aws-ruby-sdk-cloudtrail-example-create-trail.rb>`_
on GitHub.
