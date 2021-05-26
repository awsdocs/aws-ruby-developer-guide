# Listing CloudTrail Trail Events<a name="cloudtrail-example-lookup-events"></a>

This example uses the [lookup\_events](https://docs.aws.amazon.com/sdkforruby/api/Aws/CloudTrail/Client.html#lookup_events-instance_method) method to list the CloudTrail trail events in the `us-west-2` region\.

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

def show_event(event)
  puts 'Event name:   ' + event.event_name
  puts 'Event ID:     ' + event.event_id
  puts "Event time:   #{event.event_time}"
  puts 'User name:    ' + event.username

  puts 'Resources:'

  event.resources.each do |r|
    puts '  Name:       ' + r.resource_name
    puts '  Type:       ' + r.resource_type
    puts ''
  end
end

# Create client in us-west-2
client = Aws::CloudTrail::Client.new(region: 'us-west-2')

resp = client.lookup_events()

puts
puts "Found #{resp.events.count} events in us-west-2:"
puts

resp.events.each do |e|
  show_event(e)
end
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/cloudtrail/aws-ruby-sdk-cloudtrail-example-lookup-events.rb) on GitHub\.