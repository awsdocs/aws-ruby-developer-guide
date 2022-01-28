# Authorize SDK Metrics to Collect and Send Metrics in the AWS SDK for Ruby<a name="authorize-metrics"></a>

To collect metrics from AWS SDKs using AWS SDK Metrics for Enterprise Support, Enterprise customers must create an IAM Role that gives CloudWatch agent permission to gather data from their Amazon EC2 instance or production environment\.

Use the following code sample or the AWS Console to create an IAM Policy and Role for an CloudWatch agent to access SDK Metrics in your environment\.

Learn more about using SDK Metrics with AWS SDK for Ruby in [Set up SDK Metrics in the AWS SDK for Ruby](setup-metrics.md)\.

## Set Up Access Permissions Using the AWS SDK for Ruby<a name="setup-access-permissions-sdk"></a>

Create an IAM role for the instance that has permission for Amazon EC2 Systems Manager and SDK Metrics\.

First, create a policy using `CreatePolicy`\. Then create a role using `CreateRole`\. Finally, attach the policy you created to your new role with `AttachRolePolicy`\.

```
require 'aws-sdk-iam' # v2: require 'aws-sdk'

role_name = 'AmazonCSM'

client = Aws::IAM::Client.new(region: 'us-west-2')

csm_policy = {
    'Version': '2012-10-17',
    'Statement': [
        {
            'Effect': 'Allow',
            'Action': [
                'sdkmetrics:*'
            ],
            'Resource': '*'
        },
        {
            'Effect': 'Allow',
            'Action': [
                'ssm:GetParameter'
            ],
            'Resource': 'arn:aws:ssm:*:*:parameter/AmazonCSM*'
        }
    ]
}

# Create policy
resp = client.create_policy({
                                policy_name: role_name,
                                policy_document: csm_policy.to_json,
                            })

policy_arn = resp.policy.arn

puts 'Created policy with ARN: ' + policy_arn

policy_doc = {
    Version: '2012-10-17',
    Statement: [
        {
            Effect: 'Allow',
            Principal: {
                Service: 'ec2.amazonaws.com'
            },
            Action: 'sts:AssumeRole'
        },]
}

# Create role
client.create_role(
    {
        role_name: role_name,
        description: 'An instance role that has permission for AWS Systems Manager and SDK Metric Monitoring.',
        assume_role_policy_document: policy_doc.to_json,
    })

puts 'Created role ' + role_name

# Attach policy to role
client.attach_role_policy(
    {
        policy_arn: policy_arn,
        role_name: role_name,
    })

puts 'Attached policy ' + role_name + 'policy to role: ' + role_name
```

## Set Up Access Permissions by Using the IAM Console<a name="setup-access-permissions-console"></a>

Alternatively, you can use the IAM console to create a role\.

1. Go to the IAM console, and create a role to use Amazon EC2\.

1. In the navigation pane, choose **Roles**\.

1. Choose **Create Role**\.

1. Choose **AWS Service**, and then **EC2**\.

1. Choose **Next: Permissions**\.

1. Under **Attach permissions policies**, choose **create policy**\.

1. For **Service**, choose **Systems Manager**\. For **Actions**, expand **Read**, and choose `GetParameters`\. For resources, specify your CloudWatch agent\.

1. Add additional permission\.

1. Select **Choose a service**, and then **Enter service manually**\. For **Service**, enter `sdkmetrics`\. Select all `sdkmetrics` actions and all resources, and then choose **Review Policy**\.

1. Name the **Role** `AmazonSDKMetrics`, and add a description\.

1. Choose **Create Role**\.