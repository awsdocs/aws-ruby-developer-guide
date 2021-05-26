# Creating a LifeCycle Rule Configuration Template for an Amazon S3 Bucket<a name="s3-example-create-policy-template"></a>

If you have \(or plan to create\) a non\-trivial number of objects and want to specify when to move them to long\-term storage or delete them, you can save a lot of time by creating a template for the lifecycle rules and applying that template to all of your Amazon S3 buckets\.

The process includes these steps:

1. Manually modify the lifecycle settings on an existing bucket\.

1. Save the rules\.

1. Apply the rules to your other buckets\.

Start with the following rule:

![\[Image NOT FOUND\]](http://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/images/DefaultRule.png)

Run the following code to produce a JSON representation of that rule\. Save the output as `default.json`\.

```
require 'aws-sdk'

s3 = Aws::S3::Client.new(region: 'us-west-2')
resp = s3.get_bucket_lifecycle_configuration(bucket: 'default')

resp.rules.each do |rule|
  rule.to_hash.to_json
end
```

The output should look like the following\.

```
[{"expiration":{"date":null,"days":425},"id":"default","prefix":"","status":"Enabled","transitions":[{"date":null,"days":30,"storage_class":"STANDARD_IA"},{"date":null,"days":60,"storage_class":"GLACIER"}],"noncurrent_version_transitions":[],"noncurrent_version_expiration":null}]
```

Now that you have the JSON for a lifecycle rule, you can apply it to any other bucket using the following example\. The example takes the rule from `default.json` and applies it to the bucket `other_bucket`\.

```
require 'aws-sdk'
require 'json'

class Aws::S3::Types::LifecycleExpiration
  def to_map
    map = Hash.new
    self.members.each { |m| map[m] = self[m] }
    map
  end

  def to_json(*a)
    to_map.to_json(*a)
  end
end

class Aws::S3::Types::Transition
  def to_map
    map = Hash.new
    self.members.each { |m| map[m] = self[m] }
    map
  end

  def to_json(*a)
    to_map.to_json(*a)
  end
end

class Aws::S3::Types::LifecycleRule
  def to_map
    map = Hash.new
    self.members.each { |m| map[m] = self[m] }
    map
  end

  def to_json(*a)
    to_map.to_json(*a)
  end
end

# Pull in contents as a string
value = File.open('default.json', "rb").read
json_data = JSON.parse(value, opts={symbolize_names: true})

s3 = Aws::S3::Client.new(region: 'us-west-2')
s3.put_bucket_lifecycle_configuration(:bucket => 'other_bucket', :lifecycle_configuration => {:rules => json_data})
```

**Note**  
Best Practice  
We recommend that you enable the [AbortIncompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTBucketPUTlifecycle.html) lifecycle rule on your Amazon S3 buckets\.  
This rule directs Amazon S3 to abort multipart uploads that don’t complete within a specified number of days after being initiated\. When the set time limit is exceeded, Amazon S3 aborts the upload and then deletes the incomplete upload data\.  
For more information, see [Lifecycle Configuration for a Bucket with Versioning](https://docs.aws.amazon.com/AmazonS3/latest/UG/lifecycle-configuration-bucket-with-versioning.html) in the \.