# Deleting a CloudTrail Trail<a name="cloudtrail-example-delete-trail"></a>

This example uses the [delete\_trail](https://docs.aws.amazon.com/sdkforruby/api/Aws/CloudTrail/Client.html#delete_trail-instance_method) method to delete a CloudTrail trail in the `us-west-2` region\. It requires one input, the name of the trail\.

Choose `Copy` to save the code locally\.

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

require 'aws-sdk-cloudtrail'  # v2: require 'aws-sdk'

if ARGV.length != 1
  puts 'You must supply the name of the trail to delete'
  exit 1
end

name = ARGV[0]

# Create client in us-west-2
client = Aws::CloudTrail::Client.new(region: 'us-west-2')

begin
  client.delete_trail({
    name: name, # required
  })

  puts 'Successfully deleted CloudTrail ' + name + ' in us-west-2'
rescue StandardError => err
  puts 'Got error trying to delete trail ' + name + ':'
  puts err
  exit 1
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-delete-trail.rb) on GitHub\.