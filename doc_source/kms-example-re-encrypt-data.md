# Re\-encrypting a Data Blob in AWS KMS<a name="kms-example-re-encrypt-data"></a>

The following example uses the AWS SDK for Ruby[re\_encrypt](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/KMS/Client.html#re_encrypt-instance_method) method, which implements the [ReEncrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_ReEncrypt.html) operation, to decrypt encrypted data and then immediately re\-encrypt data under a new customer master key \(CMK\)\. The operations are performed entirely on the server side within AWS KMS, so they never expose your plaintext outside of AWS KMS\. The example displays a readable version of the resulting re\-encrypted blob\.

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

# Human-readable version of the ciphertext of the data to reencrypt.

blob = '01020200785d68faeec386af1057904926253051eb2919d3c16078badf65b808b26dd057c101747cadf3593596e093d4ffbf22434a6d00000068306606092a864886f70d010706a0593057020100305206092a864886f70d010701301e060960864801650304012e3011040c9d629e573683972cdb7d94b30201108025b20b060591b02ca0deb0fbdfc2f86c8bfcb265947739851ad56f3adce91eba87c59691a9a1'
sourceCiphertextBlob = [blob].pack("H*")

# Replace the fictitious key ARN with a valid key ID

destinationKeyId = 'arn:aws:kms:us-west-2:111122223333:key/0987dcba-09fe-87dc-65ba-ab0987654321'

client = Aws::KMS::Client.new(region: 'us-west-2')

resp = client.re_encrypt({
  ciphertext_blob: sourceCiphertextBlob,
  destination_key_id: destinationKeyId
})

puts 'Blob:'
puts resp.ciphertext_blob.unpack('H*')
```

Choose `Copy` to save the code locally\. See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/kms/aws-ruby-sdk-kms-example-re-encrypt-data.rb) on GitHub\.