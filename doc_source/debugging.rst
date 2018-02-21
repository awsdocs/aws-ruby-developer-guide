.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-debugging-tip-wire-tracing:

###########################################################
Debugging Tip: Getting Wire Trace Information from a Client
###########################################################

.. meta::
    :description:
        Debugging information for getting client wire trace information using the AWS SDK for Ruby
    :keywords: AWS SDK for Ruby

You can get wire trace information from an AWS client when you create it by setting the :code:`http_wire_trace` option. This information helps differentiate client changes, service issues, and user errors. The following example creates an |S3| client with wire tracing enabled.

.. code-block:: ruby

    s3 = Aws::S3::Client.new(http_wire_trace: true)

Given the following code and the argument :code:`bucket_name`, the output displays a message that says whether
a bucket with that name exists.

.. code-block:: ruby

    require 'aws-sdk'

    s3 = Aws::S3::Resource.new(client: Aws::S3::Client.new(http_wire_trace: true))

    if s3.bucket(ARGV[0]).exists?
      puts "Bucket #{ARGV[0]} exists"
    else
      puts "Bucket #{ARGV[0]} does not exist"
    end

If the bucket exists, the output looks something like the following, where *ACCESS_KEY* is the value
of your access key. (Returns were added to the :code:`HEAD` line for readability.)

.. code-block:: sh

    opening connection to bucket_name.s3-us-west-1.amazonaws.com:443...
    opened
    starting SSL for bucket_name.s3-us-west-1.amazonaws.com:443...
    SSL established
    <- "HEAD / HTTP/1.1\r\n
       Content-Type: \r\n
       Accept-Encoding: \r\n
       User-Agent: aws-sdk-ruby2/2.2.7 ruby/2.1.7 x64-mingw32\r\n
       X-Amz-Date: 20160121T191751Z\r\n
       Host: bucket_name.s3-us-west-1.amazonaws.com\r\n
       X-Amz-Content-Sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855\r\n
       Authorization: AWS4-HMAC-SHA256 Credential=ACCESS_KEY/20160121/us-west-1/s3/aws4_request,
                      SignedHeaders=host;x-amz-content-sha256;x-amz-date,
                      Signature=2ca8301c5e829700940d3cc3bca2a3e8d79d177f2c046c34a1a285770db63820\r\n
       Content-Length: 0\r\n
       Accept: */*\r\n
       \r\n"
    -> "HTTP/1.1 301 Moved Permanently\r\n"
    -> "x-amz-bucket-region: us-west-2\r\n"
    -> "x-amz-request-id: F3C75F33EF0792C4\r\n"
    -> "x-amz-id-2: N6BzRLx8b68NmF50g1IxLzT+E4uWPuAIRe7Pl4XKl5STT4tfNO7gBsO8qrrAnG4CbVpU0iIRXmk=\r\n"
    -> "Content-Type: application/xml\r\n"
    -> "Transfer-Encoding: chunked\r\n"
    -> "Date: Thu, 21 Jan 2016 19:17:54 GMT\r\n"
    -> "Server: AmazonS3\r\n"
    -> "\r\n"
    Conn keep-alive
    Bucket bucket_name exists
