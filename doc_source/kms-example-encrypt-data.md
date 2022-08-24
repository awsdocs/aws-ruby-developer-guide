# Encrypting Data in AWS KMS<a name="kms-example-encrypt-data"></a>

The following example uses the AWS SDK for Ruby[encrypt method](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/KMS/Client.html#encrypt-instance_method), which implements the [Encrypt operation](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html), to encrypt the string “1234567890”\. The example displays a readable version of the resulting encrypted blob\.

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

# ARN of the customer master key (CMK).
#
# Replace the fictitious key ARN with a valid key ID

keyId = 'arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab'

text = '1234567890'

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.encrypt({
  key_id: keyId,
  plaintext: text,
})

puts 'Blob:'
puts resp.ciphertext_blob.unpack('H*')
```

Choose `Copy` to save the code locally\. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/ruby/example_code/kms/encrypt_data.rb) on GitHub\.
