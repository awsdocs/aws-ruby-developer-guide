# Running a Lambda Function<a name="lambda-ruby-example-run-function"></a>

The following example runs the Lambda function named `MyGetitemsFunction` in the `us-west-2` region\. This function returns a list of items from a database\. The input JSON looks like the following\.

```
{
   "SortBy": "name|time",
   "SortOrder": "ascending|descending",
   "Number": 50
}
```

where:
+  `SortBy` is the criteria for sorting the results\. Our examples uses `time`, which means the returned items are sorted in the order in which they were added to the database\.
+  `SortOrder` is the order of sorting\. Our example uses `descending`, which means the most\-recent item is last in the list\.
+  `Number` is the maximum number of items to retrieve \(the default is 50\)\. Our example uses `10`, which means get the 10 most\-recent items\.

The output JSON looks like the following, where:
+  `STATUS-CODE` is an HTTP status code, `200` means the call was successful\.
+  `RESULT` is the result of the call, either `success` or `failure`\.
+  `ERROR` is an error message if `result` is `failure`, otherwise an empty string
+  `DATA` is an array of returned results if `result` is `success`, otherwise nil\.

```
{
   "statusCode": "STATUS-CODE",
   "body": {
      "result": "RESULT",
      "error": "ERROR",
      "data": "DATA"
   }
}
```

The first step is to load the modules we use:
+  `aws-sdk` loads the AWS SDK for Ruby module we use to invoke the function\.
+  `json` loads the JSON module we use to marshall and unmarshall the request and response payloads\.
+  `os` loads the OS module we use to ensure we can run our Ruby application on Microsoft Windows\. If you are on a different operating system, you can remove those lines\.
+ We then create the client we use to invoke the function\.
+ Next we create the hash for the request arguments and call `MyGetItemsFunction`\.
+ Finally we parse the response, and if are successful, we print out the items\.

```
# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

require 'aws-sdk-lambda'  # v2: require 'aws-sdk'
require 'json'

# To run on Windows:
require 'os'
if OS.windows?
  Aws.use_bundled_cert!
end

client = Aws::Lambda::Client.new(region: 'us-west-2')

# Get the 10 most recent items
req_payload = {:SortBy => 'time', :SortOrder => 'descending', :NumberToGet => 10}
payload = JSON.generate(req_payload)

resp = client.invoke({
                         function_name: 'MyGetItemsFunction',
                         invocation_type: 'RequestResponse',
                         log_type: 'None',
                         payload: payload
                       })

resp_payload = JSON.parse(resp.payload.string) # , symbolize_names: true)

# If the status code is 200, the call succeeded
if resp_payload["statusCode"] == 200
  # If the result is success, we got our items
  if resp_payload["body"]["result"] == "success"
    # Print out items
    resp_payload["body"]["data"].each do |item|
      puts item
    end
  end
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/lambda/aws-ruby-sdk-lambda-example-run-function.rb) on GitHub\.