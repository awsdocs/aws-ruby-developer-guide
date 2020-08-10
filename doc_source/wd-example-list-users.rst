.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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

The following example lists the names, email addresses,
and root folders of all users in the organization.
Choose :code:`Copy` to save the code locally, or see the link to the complete
example at the end of this topic.

1. Require the |sdk-ruby| module and create a |WD| client.

2. Call :code:`describe_users` with your organization ID, and get all of the user
names in ascending order.

3. Display the information about the users.

.. literalinclude:: ./example_code/workdocs/wd_list_users.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/workdocs/wd_list_users.rb>`_
on GitHub.
