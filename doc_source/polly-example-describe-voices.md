# Getting a List of Voices<a name="polly-example-describe-voices"></a>

This example uses the [describe\_voices](https://docs.aws.amazon.com/sdkforruby/api/Aws/Polly/Client.html#describe_voices-instance_method) method to get the list of US English voices in the `us-west-2` region\.

Choose `Copy` to save the code locally\.

Create the file *polly\_describe\_voices\.rb*\.

Add the required gem\.

**Note**  
Version 2 of the AWS SDK for Ruby didn’t have service\-specific gems\.

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

require 'aws-sdk-polly'  # In v2: require 'aws-sdk'

begin
  # Create an Amazon Polly client using
  # credentials from the shared credentials file ~/.aws/credentials
  # and the configuration (region) from the shared configuration file ~/.aws/config
  polly = Aws::Polly::Client.new
  
  # Get US English voices
  resp = polly.describe_voices(language_code: 'en-US')

  resp.voices.each do |v|
    puts v.name
    puts '  ' + v.gender
    puts
  end
rescue StandardError => ex
  puts 'Could not get voices'
  puts 'Error message:'
  puts ex.message
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/polly/polly_describe_voices.rb) on GitHub\.