.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-quick-start-guide:

########################################
QuickStart Guide to Using the |sdk-ruby|
########################################

.. meta::
    :description:
        Build Ruby applications on top of APIs that use the cost-effective, scalable, and reliable
        AWS infrastructure services with the |sdk-ruby|.
    :keywords: AWS SDK for ruby, aws.rb, aws-sdk-core gem, ruby code examples

This section shows you how to use the |sdk-ruby| to create a simple Ruby application that lists your
|S3| buckets.

* If you haven't installed the SDK, see :doc:`setup-install`.

* If you haven't configured the SDK, see :doc:`setup-config`.

.. _aws-ruby-sdk-quick-start-code:

Write the Code
==============

The following example lists the names of up to 50 of your buckets. Copy the code and save it as
:file:`buckets.rb`. Note that although the **Resource** object is created in the
:code:`us-west-2` region, |S3| returns buckets to which you have access, regardless of the
region.

.. code-block:: ruby

   require 'aws-sdk-s3'  # v2: require 'aws-sdk'

   s3 = Aws::S3::Resource.new(region: 'us-west-2')

   s3.buckets.limit(50).each do |b|
     puts "#{b.name}"
   end

Run the Code
============

Enter the following command to execute :code:`buckets.rb`.

.. code-block:: sh

   ruby buckets.rb

.. _aws-ruby-sdk-quick-start-windows:

Note for Windows Users
======================

When you use SSL certificates on Windows and run your Ruby code, you will see an error similar to
the following.

.. code-block:: none

   C:\Ruby>ruby buckets.rb
   C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect': SSL_connect returned=1 errno=0 state=SSLv3 read server certificate B: certificate verify failed (Seahorse::Client::NetworkingError)
            from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `block in connect'

            from C:/Ruby200-x64/lib/ruby/2.0.0/timeout.rb:66:in `timeout'
            from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect'
            from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:862:in `do_start'
            from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:857:in `start'
   ...

To fix this issue, add the following line to your Ruby source file, somewhere before your first AWS
call.

.. code-block:: ruby

   Aws.use_bundled_cert!

Note that if you are using just the :code:`aws-sdk-s3` gem in your Ruby
program,
you'll also need to add the :code:`aws-sdk-core` gem to use the bundled
certificate.
