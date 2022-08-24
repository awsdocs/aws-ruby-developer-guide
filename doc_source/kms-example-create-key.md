# Creating a CMK in AWS KMS<a name="kms-example-create-key"></a>

The following example uses the AWS SDK for Ruby[create\_key](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/KMS/Client.html#create_key-instance_method) method, which implements the [CreateKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateKey.html) operation to create a customer master key \(CMK\)\. Because the example only encrypts a small amount of data, a CMK is fine for our purposes\. For larger amounts of data, use the CMK to encrypt a data encryption key \(DEK\)\.

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

require 'aws-sdk-kms'  # v2: require 'aws-sdk'

# Create a customer master key (CMK).
# As long we are only encrypting small amounts of data (4 KiB or less) directly,
# a CMK is fine for our purposes.
# For larger amounts of data,
# use the CMK to encrypt a data encryption key (DEK).

client = Aws::KMS::Client.new

resp = client.create_key({
  tags: [
    {
      tag_key: 'CreatedBy',
      tag_value: 'ExampleUser'
    },
  ],
})

puts resp.key_metadata.key_id
```

Choose `Copy` to save the code locally\. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/ruby/example_code/kms/create_key.rb) on GitHub\.
