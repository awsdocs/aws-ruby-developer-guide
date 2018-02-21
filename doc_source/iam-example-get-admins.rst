.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-get-admins:

##########################################
Listing |IAM| Users who are Administrators
##########################################

.. meta::
    :description:
        Get a list of the IAM users with administrator privileges with this AWS
        SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

The following example uses the
:ruby-sdk-api:`get_account_authorization_details <Aws/IAM/Client.html#get_account_authorization_details-instance_method>`,
method to get the list of users for the current account.

Choose :code:`Copy` to save the code locally.

Create the file *get_admins.rb*.

Add the required |IAM| gem and the **os** gem, and use the latter to use the
bundled certificate if you are running on Microsoft Windows.

.. note:: Version 2 of the |sdk-ruby| didn't have service-specific gems.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 13-18
   :dedent: 0
   :language: ruby

Create a method to determine whether the user has a policy with administrator
privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 20-30
   :dedent: 0
   :language: ruby

Create a method to determine whether the user has an attached policy with administrator
privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 32-42
   :dedent: 0
   :language: ruby

Create a method to determine whether a group to which the user belongs
has a policy with administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 44-56
   :dedent: 0
   :language: ruby

Create a method to determine whether a group to which the user belongs
has an attached policy with administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 58-70
   :dedent: 0
   :language: ruby

Create a method to determine whether a group to which the user belongs
has administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 72-90
   :dedent: 0
   :language: ruby

Create a method to determine whether the user has administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 92-109
   :dedent: 0
   :language: ruby

Create a method to loop through a list of users and return
how many of those users have administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 111-123
   :dedent: 0
   :language: ruby

The main routine starts here.
Create an IAM client and variables to store the number of users,
number of users who have adminstrator privileges,
and the string that identifies a policy that supplies adminstrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 126-130
   :dedent: 0
   :language: ruby

Call :code:`get_account_authorization_details` to get the details of the account
and get the users for the account from :code:`user_detail_list`.
Keep track of how many users we get,
call :code:`get_admin_count` to get the number of those users who have
administrator privileges,
and keep track of the number of those.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 132-139
   :dedent: 0
   :language: ruby

If the first call to :code:`get_account_authorization_details` did not get
all of the details, call it again and repeat the process of determining
how many have administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 141-156
   :dedent: 0
   :language: ruby

Finally, display how many users have administrator privileges.

.. literalinclude:: ./example_code/iam/iam_ruby_example_show_admins.rb
   :lines: 158-159
   :dedent: 0
   :language: ruby

See the `complete example
<https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/iam/iam_ruby_example_show_admins.rb>`_
on GitHub.
