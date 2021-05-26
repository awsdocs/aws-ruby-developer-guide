# Determining Whether an Amazon S3 Bucket Exists<a name="s3-example-does-bucket-exist"></a>

The following code example checks whether the specified bucket exists in Amazon S3 and is accessible to you\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX - License - Identifier: Apache - 2.0

require 'aws-sdk-s3'

# Checks to see whether an Amazon Simple Storage Service
#   (Amazon S3) bucket exists.
#
# @param s3_client [Aws::S3::Client] An initialized S3 client.
# @param bucket_name [String] The name of the bucket.
# @return [Boolean] true if the bucket exists; otherwise, false.
# @example
#   exit 1 unless bucket_exists?(
#     Aws::S3::Client.new(region: 'us-east-1'),
#     'doc-example-bucket'
#   )
def bucket_exists?(s3_client, bucket_name)
  response = s3_client.list_buckets
  response.buckets.each do |bucket|
    return true if bucket.name == bucket_name
  end
  return false
rescue StandardError => e
  puts "Error listing buckets: #{e.message}"
  return false
end

# Full example call:
def run_me
  bucket_name = 'doc-example-bucket'
  region = 'us-east-1'
  s3_client = Aws::S3::Client.new(region: region)

  if bucket_exists?(s3_client, bucket_name)
    puts 'Bucket exists.'
  else
    puts 'Bucket does not exist or is not accessible to you.'
  end
end

run_me if $PROGRAM_NAME == __FILE__
```

The following code example checks whether the specified bucket exists in Amazon S3 and you have permission to access it\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

require 'aws-sdk-s3'

# Determines whether an Amazon Simple Storage Service (Amazon S3)
#   bucket exists and you have permission to access it.
#
# Prerequisites:
#
# - An S3 bucket.
#
# @param
# @param
# @return [Boolean] true if the bucket exists and you have permission to
#   access it; otherwise, false.
# @example
#   exit 1 unless bucket_exists_and_accessible?(
#     Aws::S3::Client.new(region: 'us-east-1'),
#     'doc-example-bucket'
#   )
def bucket_exists_and_accessible?(s3_client, bucket_name)
  s3_client.head_bucket(bucket: bucket_name)
  return true
rescue StandardError
  return false
end

# Full example call:
def run_me
  bucket_name = 'doc-example-bucket'
  region = 'us-east-1'
  s3_client = Aws::S3::Client.new(region: region)

  if bucket_exists_and_accessible?(s3_client, bucket_name)
    puts "Bucket '#{bucket_name}' exists and is accessible to you."
  else
    puts "Bucket '#{bucket_name}' does not exist " \
      'or is not accessible to you.'
  end
end

run_me if $PROGRAM_NAME == __FILE__
```