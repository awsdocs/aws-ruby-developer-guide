# Server\-Side Encryption<a name="s3-example-server-encryption"></a>

To encrypt objects on the server, you have the following options\.
+ You can have Amazon S3 automatically encrypt objects as you upload them to a bucket\. Once you configure a bucket with this option, every object that you upload–from that point on–is encrypted\.
+ You can have Amazon S3 encrypt an object when you upload it to a bucket\. The disadvantage with this approach is that you can still upload objects that are not encrypted\.
+ You can have Amazon S3 reject objects that are not encrypted when you attempt to upload them to a bucket\.

Learn about service\-side encryption in Amazon S3 at [Protecting Data Using Server\-Side Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/serv-side-encryption.html)\.

**Topics**
+ [Setting Default Server\-Side Encryption for an Amazon S3 Bucket](s3-example-default-server-side-encryption.md)
+ [Encrypting an Amazon S3 Bucket Object on the Server](s3-example-server-side-encryption.md)
+ [Requiring Encryption on the Server to Upload Amazon S3 Bucket Objects](s3-example-enforce-server-side-encryption.md)
+ [Encrypting an Amazon S3 Bucket Object with an AWS KMS Key](s3-example-server-side-encryption-with-user-managed-key.md)