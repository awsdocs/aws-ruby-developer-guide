# Getting a List of Lexicons<a name="polly-example-list-lexicons"></a>

This example uses the [list\_lexicons](https://docs.aws.amazon.com/sdkforruby/api/Aws/Polly/Client.html#list_lexicons-instance_method) method to get the list of lexicons in the `us-west-2` region\.

Choose `Copy` to save the code locally\.

Create the file *polly\_list\_lexicons\.rb*\.

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

  resp = polly.list_lexicons

  resp.lexicons.each do |l|
    puts l.name
    puts '  Alphabet:' + l.attributes.alphabet
    puts '  Language:' + l.attributes.language
    puts
  end
rescue StandardError => ex
  puts 'Could not get lexicons'
  puts 'Error message:'
  puts ex.message
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/polly/polly_list_lexicons.rb) on GitHub\.