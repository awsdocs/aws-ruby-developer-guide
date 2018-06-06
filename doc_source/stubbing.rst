.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-stubbing:

####################################
Stubbing Client Responses and Errors
####################################

.. meta::
    :description:
        Learn how to stub client responses and client errors in an AWS SDK for Ruby application.
    :keywords: AWS SDK for Ruby

Learn how to stub client responses and client errors in an |sdk-ruby| 
application.

.. _aws-ruby-sdk-stubbing-clients:

Stubbing Client Responses
=========================

When you stub a response, the |sdk-ruby| disables network traffic and the client returns stubbed
(or fake) data. If you don't supply stubbed data, the client returns:

* Lists as empty arrays

* Maps as empty hashes

* Numeric values as zero

* Dates as :code:`now`

The following example returns stubbed names for the list of |S3| buckets.

.. code-block:: ruby

    require 'aws-sdk'

    s3 = Aws::S3::Client.new(stub_responses: true)

    bucket_data = s3.stub_data(:list_buckets, :buckets => [{name:'aws-sdk'}, {name:'aws-sdk2'}])
    s3.stub_responses(:list_buckets, bucket_data)
    bucket_names = s3.list_buckets.buckets.map(&:name)

    # List each bucket by name
    bucket_names.each do |name|
      puts name
    end

Running this code displays the following.

.. code-block:: none

    aws-sdk
    aws-sdk2

.. note:: After you supply any stubbed data, the default values no longer apply for any remaining instance
    attributes. This means that in the previous example, the remaining instance attribute,
    :code:`creation_date`, is not :code:`now` but :code:`nil`.

The |sdk-ruby| validates your stubbed data. If you pass in data of the wrong type, it raises an :code:`ArgumentError` exception. For example, if
instead of the previous assignment to :code:`bucket_data`, you used the following:

.. code-block:: ruby

    bucket_data = s3.stub_data(:list_buckets, buckets:['aws-sdk', 'aws-sdk2'])

The |sdk-ruby| raises two :code:`ArgumentError` exceptions.

.. code-block:: none

    expected params[:buckets][0] to be a hash
    expected params[:buckets][1] to be a hash

.. _aws-ruby-sdk-stubbing-errors:

Stubbing Client Errors
======================

You can also stub errors that the |sdk-ruby| raises for specific methods. The following example displays
:code:`Caught Timeout::Error error calling head_bucket on aws-sdk`.

.. code-block:: ruby

    require 'aws-sdk'

    s3 = Aws::S3::Client.new(stub_responses: true)
    s3.stub_responses(:head_bucket, Timeout::Error)

    begin
      s3.head_bucket({bucket: 'aws-sdk'})
    rescue Exception => ex
      puts "Caught #{ex.class} error calling 'head_bucket' on 'aws-sdk'"
    end
