# Using the AWS SDK for Ruby REPL Tool<a name="repl"></a>

Developers can use `aws-v3.rb` \(formerly `aws.rb`\), the interactive command line read\-evaluate\-print loop \(REPL\) console tool that is part of the `aws-sdk` gem\.

Although `aws-v3.rb` does work with the Interactive Ruby Shell \(`irb`\), we recommend that you install `pry`, which provides a more powerful REPL environment\.

Use the following command to install `pry`\.

```
gem install pry
```

To use `aws-v3.rb`, you invoke it in a console window using one of the following two command lines\.

```
aws-v3.rb
aws-v3.rb -v
```

The second command line invokes the REPL with extensive HTTP wire logging, which provides information about the communication between the AWS SDK for Ruby and AWS\. Use this command line with caution, however, because it also adds overhead that can make your code run slower\.

The REPL defines a helper object for every service class\. Downcase the service module name to get the name of the helper object\. For example, the names of the Amazon S3 and Amazon EC2 helper objects are `s3` and `ec2`, respectively\.