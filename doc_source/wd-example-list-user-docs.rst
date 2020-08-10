.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

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

The following example lists the documents for a user.
Choose :code:`Copy` to save the code locally, or see the link to the complete
example at the end of this topic.

1. Require the |sdk-ruby| module.

2. Create a helper method to get the root folder of a user.

3. Create a |WD| client.

4. Get the root folder for that user.

5. Call :code:`describe_folder_contents` to get the contents of the folder
in ascending order.

6. Display the name, size (in bytes), last modified date, document ID and version
ID for each document in the user's root folder.

.. literalinclude:: ./example_code/workdocs/wd_list_user_docs.rb
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/workdocs/wd_list_user_docs.rb>`_
on GitHub.
