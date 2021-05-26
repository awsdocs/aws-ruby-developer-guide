# Listing AWS CodeBuild Project Builds<a name="cb-example-list-builds"></a>

The following example displays information about your AWS CodeBuild project builds\. This information includes the name of the project, when the build started, and how long each phase of the build took, in seconds\.

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

require 'aws-sdk-codebuild'  # v2: require 'aws-sdk'

client = Aws::CodeBuild::Client.new(region: 'us-west-2')

build_list = client.list_builds({sort_order: 'ASCENDING', })

builds = client.batch_get_builds({ids: build_list.ids})

builds.builds.each do |build|
  puts 'Project:    ' + build.project_name
  puts 'Phase:      ' + build.current_phase
  puts 'Status:     ' + build.build_status
end
```

Choose `Copy` to save the code locally\. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/codebuild/aws-ruby-sdk-codebuild-example-list-builds.rb) on GitHub\.