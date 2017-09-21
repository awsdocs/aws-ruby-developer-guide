.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _wd-example-list-users:

#############
Listing Users
#############

The following example lists the names of all users, or lists additional details
about a user if a user name is specified on the command line.
Choose :code:`Copy` to save the code locally, or see the link to the complete
example at the end of this topic.

Require the |sdk-ruby| module and create a |WD| client.

.. literalinclude:: ./example_code/workdocs/wd_list_users.rb
   :lines: 13-15
   :dedent: 0
   :language: ruby

Call :code:`describe_users` with your organization ID, and get all of the user
names in ascending order.

.. literalinclude:: ./example_code/workdocs/wd_list_users.rb
   :lines: 17-25
   :dedent: 0
   :language: ruby

Display the information about the users.

.. literalinclude:: ./example_code/workdocs/wd_list_users.rb
   :lines: 27-33
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/workdocs/wd_list_users.rb>`_
on GitHub.
