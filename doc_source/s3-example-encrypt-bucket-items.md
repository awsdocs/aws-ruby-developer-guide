# Encrypting Amazon S3 Bucket Items<a name="s3-example-encrypt-bucket-items"></a>

Amazon S3 supports encrypting Amazon S3 bucket objects on both the client and the server\. To encrypt objects on the client, you perform the encryption yourself, either using keys that you create or keys that \(AWS KMS\) manages for you\.

To encrypt objects on the server, you have more options\.
+ You can have Amazon S3 automatically encrypt objects as you upload them to a bucket\. Once you configure a bucket with this option, every object that you upload–from that point on–is encrypted\.
+ You can have Amazon S3 encrypt an object when you upload it to a bucket\. The disadvantage with this approach is that you can still upload objects that are not encrypted\.
+ You can have Amazon S3 encrypt an object when you upload it to a bucket\. The disadvantage with this approach is that you can still upload objects that are not encrypted\.

The following examples describe these options, from the simplest example of specifying that all objects uploaded to a bucket are automatically encrypted, to the most complex example of using asymmetric public and private keys on the client\. Don’t worry, we’ll explain these concepts as we go\. Learn about encryption in Amazon S3 at [Protecting Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html)\.

**Topics**
+ [Server\-Side Encryption](s3-example-server-encryption.md)
+ [Client\-Side Encryption](s3-example-client-encryption.md)