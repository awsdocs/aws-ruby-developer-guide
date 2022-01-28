# Amazon EC2 Tips and Tricks<a name="ec2-tips"></a>

This section provides some tips to help you use the AWS SDK for Ruby with Amazon Elastic Compute Cloud \(Amazon EC2\) services\. For more information about Amazon EC2, see the [Amazon EC2 Getting Started Guide](https://docs.aws.amazon.com/AWSEC2/latest/GettingStartedGuide/)\.

## Switching Elastic IPs<a name="aws-ruby-sdk-ec2-tip-switch-elastic-ips"></a>

The following example associates the Elastic IP address with the instance represented by `i-12345678`\.

```
ec2 = Aws::EC2::Client.new

resp = ec2.allocate_address
ec2.associate_address(instance_id:"i-12345678", allocation_id: resp.allocation_id)
```