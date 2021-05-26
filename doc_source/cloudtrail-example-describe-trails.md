# Listing the CloudTrail Trails<a name="cloudtrail-example-describe-trails"></a>

This example uses the [describe\_trails](https://docs.aws.amazon.com/sdkforruby/api/Aws/CloudTrail/Client.html#describe_trails-instance_method) method to list the names of the CloudTrail trails and the bucket in which CloudTrail stores information in the `us-west-2` region\.

Choose `Copy` to save the code locally\.

Create the file *describe\_trails\.rb* with the following code\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
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

# Create client in us-west-2
client = Aws::CloudTrail::Client.new(region: 'us-west-2')

resp = client.describe_trails({})

puts
puts "Found #{resp.trail_list.count} trail(s) in us-west-2:"
puts

resp.trail_list.each do |trail|
  puts 'Name:           ' + trail.name
  puts 'S3 bucket name: ' + trail.s3_bucket_name
  puts
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-describe-trails.rb) on GitHub\.