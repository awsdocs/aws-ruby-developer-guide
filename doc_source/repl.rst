.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-repl:

#########################
Using the |sdk-ruby| REPL
#########################

This section is for developers who want to use :code:`aws.rb`, the interactive command-line
read-evaluate-print loop (REPL) console tool that is part of the :code:`aws-sdk-core` gem.

Although :code:`aws.rb` works with the Interactive Ruby Shell (:code:`irb`), we recommend that you
install :code:`pry`, which provides a more powerful REPL environment.

Use the following command to install :code:`pry`:

.. code-block:: none

    gem install pry

To use :code:`aws.rb`, invoke it in a console window. You can use one of the following two command
lines.

.. code-block:: none

    aws.rb
    aws.rb -v

The second command line invokes the REPL with extensive HTTP wire logging, which provides
information about the communication between the |sdk-ruby| and AWS. It also adds overhead and thus
slows down the running of your code, so use it with caution.

The REPL defines a helper object for every service class. Downcase the service module name to get
the name of the helper object. For example, the names of the |S3| and |EC2| helper objects are
:code:`s3` and :code:`ec2`, respectively.
