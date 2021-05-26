# Specifying a Client Timeout Duration<a name="timeout-duration"></a>

By default, the AWS SDK for Ruby performs up to three retries, with 15 seconds between retries, for a total of up to four attempts\. Therefore, an operation could take up to 60 seconds to time out\.

The following example creates an Amazon S3 client in the region `us-west-2`, and specifies to wait five seconds between two retries on every client operation\. Therefore, Amazon S3 client operations could take up to 15 seconds to time out\.

```
 s3 = Aws::S3::Client.new(
   region: region,
   retry_limit: 2,
   retry_backoff: lambda { |c| sleep(5) }
)
```