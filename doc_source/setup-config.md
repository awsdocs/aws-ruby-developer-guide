# Configuring the AWS SDK for Ruby<a name="setup-config"></a>

Learn how to configure the AWS SDK for Ruby\. To use the SDK, you must set either AWS credentials or create an AWS STS access token, and set the AWS Region you want to use\.

## Get your AWS access keys<a name="aws-ruby-sdk-getting-credentials"></a>

Access keys consist of an *access key ID* and *secret access key*, which are used to sign programmatic requests that you make to AWS\. If you don’t have access keys, you can create them by using the [Management Console](https://console.aws.amazon.com/)\. We recommend that you use IAM access keys instead of AWS root account access keys\. IAM lets you securely control access to AWS services and resources in your AWS account\.

**Note**  
To create access keys, you must have permissions to perform the required IAM actions\. For more information, see [Granting IAM User Permission to Manage Password Policy and Credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_delegate-permissions.html) in the IAM User Guide\.

### To get your access key ID and secret access key<a name="get-access-id"></a>

1. Open the [IAM console](https://console.aws.amazon.com/iam/home)\.

1. On the navigation menu, choose **Users**\.

1. Choose your IAM user name \(not the check box\)\.

1. Open the **Security credentials** tab, and then choose **Create access key**\.

1. To see the new access key, choose **Show**\. Your credentials resemble the following:
   + Access key ID: `AKIAIOSFODNN7EXAMPLE` 
   + Secret access key: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` 

1. To download the key pair, choose **Download \.csv file**\. Store the keys

in a secure location\.

**Important**  
Keep the keys confidential to protect your AWS account, and never email them\. Do not share them outside your organization, even if an inquiry appears to come from AWS or Amazon\.com\. *No one who legitimately represents Amazon will ever ask you for your secret key\.* 

 **Related topics** 
+  [What Is IAM?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) in the IAM User Guide\.
+  [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) in the AWS General Reference\.

## Setting AWS Credentials<a name="aws-ruby-sdk-setting-credentials"></a>

Before you can use the AWS SDK for Ruby to make a call to an AWS service, you must set the AWS access credentials that the SDK will use to verify your access to AWS services and resources\.

The AWS SDK for Ruby searches for credentials in the following order:

1.  [Setting Credentials Using Environment Variables](#aws-ruby-sdk-credentials-environment) 

1.  [Setting Shared Credentials](#aws-ruby-sdk-credentials-shared) 

1.  [Setting Credentials Using IAM](#aws-ruby-sdk-credentials-iam) 

You can override these settings in your code\. The precedence is:

1.  [Setting Credentials in a Client Object](#aws-ruby-sdk-credentials-client) 

1.  [Setting Credentials Using `Aws.config`](#aws-ruby-sdk-credentials-aws-config) 

The following sections describe the various ways you can set credentials, starting with the most flexible approach\. For more information about AWS credentials and recommended approaches for credential management, see [AWS Security Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html) in the AWS General Reference\.

Note that the shared configuration is loaded only a single time, and credentials are provided statically at client creation time\. Shared credentials do not refresh\.

### Setting Shared Credentials<a name="aws-ruby-sdk-credentials-shared"></a>

Set shared credentials in the AWS credentials profile file on your local system\.

On Unix\-based systems, such as Linux or OS X, this file is located in the following location\.

```
~/.aws/credentials
```

On Windows, this file is located in the following location\.

```
%HOMEPATH%\.aws\credentials
```

This file must have the following format, where `default` is the name of the default configuration profile given to these credentials, `your_access_key_id` is the value of your access key, and `your_secret_access_key` is the value of your secret access key\.

```
[default]
aws_access_key_id = your_access_key_id
aws_secret_access_key = your_secret_access_key
```

### Setting Credentials Using Environment Variables<a name="aws-ruby-sdk-credentials-environment"></a>

Set the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` environment variables\.

Use the `export` command to set these variables on Unix\-based systems, such as Linux or OS X\. The following example sets the value of your access key to `your_access_key_id` and the value of your secret access key to `your_secret_access_key`\.

```
export AWS_ACCESS_KEY_ID=your_access_key_id
export AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

To set these variables on Windows, use the `set` command, as shown in the following example\.

```
set AWS_ACCESS_KEY_ID=your_access_key_id
set AWS_SECRET_ACCESS_KEY=your_secret_access_key
```

### Setting Credentials Using `Aws.config`<a name="aws-ruby-sdk-credentials-aws-config"></a>

Set the credentials in your code by updating the values in the `Aws.config` hash\.

The following example sets the value of your access key to `your_access_key_id` and the value of your secret access key to `your_secret_access_key`\. Any client or resource you create subsequently will use these credentials\.

```
Aws.config.update({
   credentials: Aws::Credentials.new('your_access_key_id', 'your_secret_access_key')
})
```

### Changing your Credentials Location<a name="aws-ruby-sdk-credentials-move"></a>

You can also use **`Aws.config`** to store your credentials in a non\-standard location\.

The following example updates your configuration to store your credentials at *my\-path*\.

```
shared_creds = Aws::SharedCredentials.new(path: 'my_path')
Aws.config.update(credentials: shared_creds)
```

### Setting Credentials in a Client Object<a name="aws-ruby-sdk-credentials-client"></a>

Set the credentials in your code by specifying them when you create an AWS client\.

The following example creates an Amazon S3 client using the access key `your_access_key_id` and the secret access key `your_secret_access_key`\.

```
s3 = Aws::S3::Client.new(
  access_key_id: 'your_access_key_id',
  secret_access_key: 'your_secret_access_key'
)
```

### Setting Credentials Using IAM<a name="aws-ruby-sdk-credentials-iam"></a>

For an Amazon Elastic Compute Cloud instance, create an AWS Identity and Access Management role, and then give your Amazon EC2 instance access to that role\. For more information, see [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) in the Amazon EC2 User Guide for Linux Instances or [IAM Roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/iam-roles-for-amazon-ec2.html) in the Amazon EC2 User Guide for Windows Instances\.

## Creating an AWS STS Access Token<a name="aws-ruby-sdk-credentials-access-token"></a>

Use the [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/AssumeRoleCredentials.html) method to create an AWS Security Token Service \(AWS STS\) access token\.

The following example uses an access token to create an Amazon S3 client object, where `linked::account::arn` is the Amazon Resource Name \(ARN\) of the role to assume and `session-name` is an identifier for the assumed role session\.

```
role_credentials = Aws::AssumeRoleCredentials.new(
  client: Aws::STS::Client.new,
  role_arn: "linked::account::arn",
  role_session_name: "session-name"
)

s3 = Aws::S3::Client.new(credentials: role_credentials)
```

## Setting a Region<a name="aws-ruby-sdk-setting-region"></a>

You need to set a [region](https://docs.aws.amazon.com/general/latest/gr/rande.html) when using most AWS services\. You can set the AWS Region in ways similar to setting your AWS credentials\. The AWS SDK for Ruby searches for a region in the following order:
+  [Setting the Region in a Client or Resource Object](#aws-ruby-sdk-region-client-resource) 
+  [Setting the Region Using `Aws.config`](#aws-ruby-sdk-region-aws-config) 
+  [Setting the Region Using Environment Variables](#aws-ruby-sdk-region-environment) 

The rest of this section describes how to set a region, starting with the most flexible approach\.

### Setting the Region Using Environment Variables<a name="aws-ruby-sdk-region-environment"></a>

Set the region by setting the `AWS_REGION` environment variable\.

Use the `export` command to set this variable on Unix\-based systems, such as Linux or OS X\. The following example sets the region to `us-west-2`\.

```
export AWS_REGION=us-west-2
```

To set this variable on Windows, use the `set` command\. The following example sets the region to `us-west-2`\.

```
set AWS_REGION=us-west-2
```

### Setting the Region Using `Aws.config`<a name="aws-ruby-sdk-region-aws-config"></a>

Set the region by adding a `region` value to the `Aws.config` hash\. The following example updates the `Aws.config` hash to use the `us-west-1` region\.

```
Aws.config.update({region: 'us-west-1'})
```

Any clients or resources you subsequently create are bound to this region\.

### Setting the Region in a Client or Resource Object<a name="aws-ruby-sdk-region-client-resource"></a>

Set the region when you create an AWS client or resource\. The following example creates an Amazon S3 resource object in the `us-west-1` region\.

```
s3 = Aws::S3::Resource.new(region: 'us-west-1')
```

## Setting a Nonstandard Endpoint<a name="aws-ruby-sdk-setting-non-standard-endpoint"></a>

If you need to use a nonstandard endpoint in the region you’ve selected, add an `endpoint` entry to `Aws.config` or set the `endpoint:` when creating a service client or resource object\. The following example creates an Amazon S3 resource object in the `other_endpoint` endpoint\.

```
s3 = Aws::S3::Resource.new(endpoint: other_endpoint)
```

**Topics**