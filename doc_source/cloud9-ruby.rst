.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _cloud9-ruby:

###################################
Using |AC9long| with the |sdk-ruby|
###################################

.. meta::
    :description:
        Describes how to use AWS Cloud9 with the AWS SDK for Ruby.

You can use |AC9long| with the |sdk-ruby| to write and run your Ruby code using just a browser. |AC9| includes tools such as a
code editor and terminal. Because the |AC9| IDE is cloud based, you can work on your projects from your office, home,
or anywhere using an internet-connected machine. For general information about |AC9|, see the |AC9-ug|.

Follow these instructions to set up |AC9| with the |sdk-ruby|:

* :ref:`cloud9-ruby-account`
* :ref:`cloud9-ruby-environment`
* :ref:`cloud9-ruby-sdk`
* :ref:`cloud9-ruby-examples`
* :ref:`cloud9-ruby-run`

.. _cloud9-ruby-account:

Step 1: Set up Your AWS Account to Use |AC9|
============================================

Start to use |AC9| by signing in to the |AC9| console as an |IAMlong| (|IAM|) entity (for example, an |IAM| user) in your AWS account who
has access permissions for |AC9|.

To set up an |IAM| entity in your AWS account to access |AC9|, and to sign in to the |AC9| console, see
`Team Setup for AWS Cloud9 <https://docs.aws.amazon.com/cloud9/latest/user-guide/setup.html>`_ in the |AC9-ug|.

.. _cloud9-ruby-environment:

Step 2: Set up Your |AC9| Development Environment
=================================================

After you sign in to the |AC9| console, use the console to create an |AC9| development environment. 
After you create the environment, |AC9| opens the IDE for that environment.

See `Creating an Environment in AWS Cloud9 <https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html>`_ in the |AC9-ug| for details.

.. note:: As you create your environment in the console for the first time, we recommend that you choose the option to :guilabel:`Create a new instance for environment (EC2)`.
   This option tells |AC9| to create an environment, launch an |EC2| instance, and then connect the new instance to the new environment. This is the fastest way
   to begin using |AC9|.

.. _cloud9-ruby-sdk:

Step 3: Set up the |sdk-ruby|
=============================

After |AC9| opens the IDE for your development environment, use the IDE to set up the |sdk-ruby| in your environment, as follows.

#. If the terminal isn't already open in the IDE, open it. On the menu bar in the IDE, choose :guilabel:`Window, New Terminal`.
#. Run the following command to install the |sdk-ruby|.

   .. code-block:: sh

      sudo gem install aws-sdk

If the IDE can't find RubyGems, run the following command to install it. (This command assumes you 
chose the option to :guilabel:`Create a new instance for environment (EC2)`, earlier in this topic.)

.. code-block:: sh

   sudo yum -y install gem

If the IDE can't find Ruby, run the following command to install it. (This command assumes you 
chose the option to :guilabel:`Create a new instance for environment (EC2)`, earlier in this topic.)

.. code-block:: sh

   sudo yum -y install ruby

.. _cloud9-ruby-examples:

Step 4: Download Example Code
=============================

Use the terminal you opened in the previous step to download example code for the |sdk-ruby| into the |AC9| development environment.

To do this, run the following command. This command downloads a copy of all of the code examples 
used in the official AWS SDK documentation into your environment's root directory.

.. code-block:: sh

   git clone https://github.com/awsdocs/aws-doc-sdk-examples.git

To find code examples for the |sdk-ruby|, use the :guilabel:`Environment` window to open the
:file:`ENVIRONMENT_NAME/aws-doc-sdk-examples/ruby` directory,
where :file:`ENVIRONMENT_NAME` is the name of your development environment.

To learn how to work with these and other code examples, see :doc:`examples`.

.. _cloud9-ruby-run:

Step 5: Run Example Code
========================

To run code in your |AC9| development environment, see
`Run Your Code <https://docs.aws.amazon.com/cloud9/latest/user-guide/build-run-debug.html#build-run-debug-run>`_ in the |AC9-ug|.
