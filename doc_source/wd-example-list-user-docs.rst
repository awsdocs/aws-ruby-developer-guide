.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _wd-example-list-user-docs:

#################
Listing User Docs
#################

The following example lists the documents for the user whose name is specified
on the command line.
Choose :code:`Copy` to save the code locally, or see the link to the complete
example at the end of this topic.

Require the |sdk-ruby| module.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :lines: 13
   :dedent: 0
   :language: ruby

Create a helper method to get the root folder of a user.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :lines: 15-30
   :dedent: 0
   :language: ruby

Create a |WD| client.

.. literalinclude:: ./example_code/workdocs/wd_list_users.rb
   :lines: 32
   :dedent: 0
   :language: ruby

Get the root folder for that user.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :lines: 34-40
   :dedent: 0
   :language: ruby

Call :code:`describe_folder_contents` to get the contents of the folder
in ascending order.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :lines: 47-51
   :dedent: 0
   :language: ruby

Display the name, size (in bytes), last modified date, document ID and version
ID for each document in the user's root folder.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :lines: 53-62
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/workdocs/wd_list_user_docs.rb>`_
on GitHub.
