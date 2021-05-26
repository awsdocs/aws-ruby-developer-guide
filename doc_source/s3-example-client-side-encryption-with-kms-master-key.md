# Encrypting an Amazon S3 Bucket Object with an AWS KMS Key<a name="s3-example-client-side-encryption-with-kms-master-key"></a>

The following code example uploads an encrypted object to an Amazon S3 bucket\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX - License - Identifier: Apache - 2.0

require 'aws-sdk-s3'

# Uploads an encrypted object to an Amazon S3 bucket.
#
# Prerequisites:
#
# - An Amazon S3 bucket.
# - An encrypted object to upload to the bucket.
#
# @param s3_encryption_client [Aws::S3::EncryptionV2::Client]
#   An initialized Amazon S3 V2 encryption client.
# @param bucket_name [String] The name of the bucket.
# @param object_key [String] The name of the object to upload.
# @param object_content [String] The content of the object to upload.
# @return [Boolean] true if the object was encrypted and uploaded;
#   otherwise, false.
# @example
#   s3_encryption_client = Aws::S3::EncryptionV2::Client.new(
#     region: 'us-east-1',
#     kms_key_id: '9041e78c-7a20-4db3-929e-828abEXAMPLE',
#     key_wrap_schema: :kms_context,
#     content_encryption_schema: :aes_gcm_no_padding,
#     security_profile: :v2
#   )
#   if encrypted_object_uploaded?(
#     s3_encryption_client,
#     'doc-example-bucket',
#     'my-file.txt',
#     'This is the content of my-file.txt.'
#   )
#     puts 'Uploaded.'
#   else
#     puts 'Not uploaded.'
#   end
def encrypted_object_uploaded?(
  s3_encryption_client,
  bucket_name,
  object_key,
  object_content
)
  s3_encryption_client.put_object(
    bucket: bucket_name,
    key: object_key,
    body: object_content
  )
  return true
rescue StandardError => e
  puts "Error uploading object: #{e.message}"
  return false
end

# Full example call:
def run_me
  bucket_name = 'doc-example-bucket'
  object_key = 'my-file.txt'
  region = 'us-east-1'
  kms_key_id = '9041e78c-7a20-4db3-929e-828abEXAMPLE'
  object_content = File.read(object_key)

  # Note that in the following call:
  # - key_wrap_schema must be kms_context for AWS KMS.
  # - To allow reading and decrypting objects that are encrypted by the
  #   Amazon S3 V1 encryption client instead, use :v2_and_legacy instead of :v2.
  s3_encryption_client = Aws::S3::EncryptionV2::Client.new(
    region: region,
    kms_key_id: kms_key_id,
    key_wrap_schema: :kms_context,
    content_encryption_schema: :aes_gcm_no_padding,
    security_profile: :v2
  )

  if encrypted_object_uploaded?(
    s3_encryption_client,
    bucket_name,
    object_key,
    object_content
  )
    puts 'Uploaded.'
  else
    puts 'Not uploaded.'
  end
end

run_me if $PROGRAM_NAME == __FILE__
```