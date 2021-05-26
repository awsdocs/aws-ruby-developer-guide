# Creating a Lambda Function<a name="lambda-ruby-example-create-function"></a>

The following example creates the Lambda function named `my-notification-function` in the `us-west-2` region using these values:
+ Role ARN: `my-resource-arn`\. In most cases, you need to attach only the `AWSLambdaExecute` managed policy to the policy for this role\.
+ Function entry point: `my-package.my-class` 
+ Runtime: `java8` 
+ Zip file: `my-zip-file.zip` 
+ Bucket: `my-notification-bucket` 
+ Key: `my-zip-file` 

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

client = Aws::Lambda::Client.new(region: 'us-west-2')

args = {}
args[:role] = 'my-resource-arn'
args[:function_name] = 'my-notification-function'
args[:handler] = 'my-package.my-class'

# Also accepts nodejs, nodejs4.3, and python2.7
args[:runtime] = 'java8'

code = {}
code[:zip_file] = 'my-zip-file.zip'
code[:s3_bucket] = 'my-notification-bucket'
code[:s3_key] = 'my-zip-file'

args[:code] = code

client.create_function(args)
```