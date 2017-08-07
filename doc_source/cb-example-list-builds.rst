.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-cb-example-list-builds:

###########################
Listing your Project Builds
###########################

The following example displays information about your |ACBlong| project builds,
including the name of the project, when the build started, and how long each
phase of the build took, in seconds.
Click the :code:`Copy` button and save it as :file:`cb_list_builds.rb`.

.. literalinclude:: ./example_code/codebuild/aws-ruby-sdk-codebuild-example-list-builds.rb
   :lines: 13-66
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/codebuild/aws-ruby-sdk-codebuild-example-list-builds.rb>`_
on GitHub.
