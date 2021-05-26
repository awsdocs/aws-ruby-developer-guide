# QuickStart Guide to Using the AWS SDK for Ruby<a name="quick-start-guide"></a>

This section shows you how to use the AWS SDK for Ruby to create a simple Ruby application that lists your Amazon S3 buckets\.
+ If you haven’t installed the SDK, see [Installing the AWS SDK for Ruby](setup-install.md)\.
+ If you haven’t configured the SDK, see [Configuring the AWS SDK for Ruby](setup-config.md)\.

## Write the Code<a name="aws-ruby-sdk-quick-start-code"></a>

The following example lists the names of up to 50 of your buckets\. Copy the code and save it as `buckets.rb`\. Note that although the **Resource** object is created in the `us-west-2` region, Amazon S3 returns buckets to which you have access, regardless of the region\.

```
require 'aws-sdk-s3'  # v2: require 'aws-sdk'

s3 = Aws::S3::Resource.new(region: 'us-west-2')

s3.buckets.limit(50).each do |b|
  puts "#{b.name}"
end
```

## Run the Code<a name="run-the-code"></a>

Enter the following command to execute `buckets.rb`\.

```
ruby buckets.rb
```

## Note for Windows Users<a name="aws-ruby-sdk-quick-start-windows"></a>

When you use SSL certificates on Windows and run your Ruby code, you will see an error similar to the following\.

```
C:\Ruby>ruby buckets.rb
C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect': SSL_connect returned=1 errno=0 state=SSLv3 read server certificate B: certificate verify failed (Seahorse::Client::NetworkingError)
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `block in connect'

         from C:/Ruby200-x64/lib/ruby/2.0.0/timeout.rb:66:in `timeout'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:921:in `connect'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:862:in `do_start'
         from C:/Ruby200-x64/lib/ruby/2.0.0/net/http.rb:857:in `start'
...
```

To fix this issue, add the following line to your Ruby source file, somewhere before your first AWS call\.

```
Aws.use_bundled_cert!
```

Note that if you are using just the `aws-sdk-s3` gem in your Ruby program, you’ll also need to add the `aws-sdk-core` gem to use the bundled certificate\.