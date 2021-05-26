# Creating a Snapshot of an Amazon RDS Instance<a name="rds-example-create-snapshot"></a>

The following example creates a snapshot for the Amazon RDS instance represented by *instance\_name* in the `us-west-2` region\.

**Note**  
If your instance is a member of a cluster, you can’t create a snapshot of the instance\. Instead, you must create a snapshot of the cluster \(see [Creating a Snapshot of an Amazon RDS Cluster](rds-example-create-cluster-snapshot.md#aws-ruby-sdk-rds-example-create-cluster-snapshot)\)\.

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

require 'aws-sdk-rds'  # v2: require 'aws-sdk'

rds = Aws::RDS::Resource.new(region: 'us-west-2')
      
instance = rds.db_instance(instance_name)
      
date =  Time.new
date_time =  date.year.to_s +  '-' +  date.month.to_s +  '-' +  date.day.to_s +  '-' +  date.hour.to_s +  '-' +  date.min.to_s

id = instance_name + '-' + date_time
      
instance.create_snapshot({db_snapshot_identifier: id})

puts "Created snapshot #{id}"
```