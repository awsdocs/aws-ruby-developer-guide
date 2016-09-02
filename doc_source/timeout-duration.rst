.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-timeout-duration:

####################################
Specifying a Client Timeout Duration
####################################

The following example creates a new |S3|, client in the region :code:`us-west-2`, and specifies to
wait 5 seconds between two retries on every client operation. By default the SDK performs up to
three retries, with 15 seconds between retries, for a total of up to four attempts. Therefore an
operation could take 60 seconds to time out, so the example could take 15 seconds to timeout.

.. code-block:: ruby

    s3 = Aws::S3::Client.new(region: 'us-west-2', retry_limit: 2, http_open_timeout: 5)
