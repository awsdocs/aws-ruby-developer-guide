.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-repl:

##############################
Using the |sdk-ruby| REPL Tool
##############################

.. meta::
    :description:
        Build Ruby applications on top of APIs that use the cost-effective, scalable, and reliable
        AWS infrastructure services with the |sdk-ruby|.
    :keywords: AWS SDK for ruby, aws.rb, aws-v3.rb, aws-sdk-core gem, ruby code examples

Developers can use :code:`aws-v3.rb` (formerly :code:`aws.rb`), the interactive command line
read-evaluate-print loop (REPL) console tool that is part of the :code:`aws-sdk` gem.

Although :code:`aws-v3.rb` does work with the Interactive Ruby Shell (:code:`irb`), we recommend that
you install :code:`pry`, which provides a more powerful REPL environment.

Use the following command to install :code:`pry`.

.. code-block:: none

    gem install pry

To use :code:`aws-v3.rb`, you invoke it in a console window using one of the following two command
lines.

.. code-block:: none

    aws-v3.rb
    aws-v3.rb -v

The second command line invokes the REPL with extensive HTTP wire logging, which provides
information about the communication between the |sdk-ruby| and AWS. Use this command line with
caution, however, because it also adds overhead that can make your code run slower.

The REPL defines a helper object for every service class. Downcase the service module name to get
the name of the helper object. For example, the names of the |S3| and |EC2| helper objects are
:code:`s3` and :code:`ec2`, respectively.
