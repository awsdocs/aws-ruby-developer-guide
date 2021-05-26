# Using AWS Cloud9 with the AWS SDK for Ruby<a name="cloud9-ruby"></a>

You can use AWS Cloud9 with the AWS SDK for Ruby to write and run your Ruby code using just a browser\. AWS Cloud9 includes tools such as a code editor and terminal\. Because the AWS Cloud9 IDE is cloud based, you can work on your projects from your office, home, or anywhere using an internet\-connected machine\. For general information about AWS Cloud9, see the \.

Follow these instructions to set up AWS Cloud9 with the AWS SDK for Ruby:
+  [Step 1: Set up Your AWS Account to Use AWS Cloud9](#cloud9-ruby-account) 
+  [Step 2: Set up Your AWS Cloud9 Development Environment](#cloud9-ruby-environment) 
+  [Step 3: Set up the AWS SDK for Ruby](#cloud9-ruby-sdk) 
+  [Step 4: Download Example Code](#cloud9-ruby-examples) 
+  [Step 5: Run Example Code](#cloud9-ruby-run) 

## Step 1: Set up Your AWS Account to Use AWS Cloud9<a name="cloud9-ruby-account"></a>

Start to use AWS Cloud9 by signing in to the AWS Cloud9 console as an AWS Identity and Access Management \(IAM\) entity \(for example, an IAM user\) in your AWS account who has access permissions for AWS Cloud9\.

To set up an IAM entity in your AWS account to access AWS Cloud9, and to sign in to the AWS Cloud9 console, see [Team Setup for AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/setup.html) in the \.

## Step 2: Set up Your AWS Cloud9 Development Environment<a name="cloud9-ruby-environment"></a>

After you sign in to the AWS Cloud9 console, use the console to create an AWS Cloud9 development environment\. After you create the environment, AWS Cloud9 opens the IDE for that environment\.

See [Creating an Environment in AWS Cloud9](https://docs.aws.amazon.com/cloud9/latest/user-guide/create-environment.html) in the for details\.

**Note**  
As you create your environment in the console for the first time, we recommend that you choose the option to **Create a new instance for environment \(EC2\)**\. This option tells AWS Cloud9 to create an environment, launch an Amazon EC2 instance, and then connect the new instance to the new environment\. This is the fastest way to begin using AWS Cloud9\.

## Step 3: Set up the AWS SDK for Ruby<a name="cloud9-ruby-sdk"></a>

After AWS Cloud9 opens the IDE for your development environment, use the IDE to set up the AWS SDK for Ruby in your environment, as follows\.

1. If the terminal isn’t already open in the IDE, open it\. On the menu bar in the IDE, choose **Window, New Terminal**\.

1. Run the following command to install the AWS SDK for Ruby\.

   ```
   sudo gem install aws-sdk
   ```

If the IDE can’t find RubyGems, run the following command to install it\. \(This command assumes you chose the option to **Create a new instance for environment \(EC2\)**, earlier in this topic\.\)

```
sudo yum -y install gem
```

If the IDE can’t find Ruby, run the following command to install it\. \(This command assumes you chose the option to **Create a new instance for environment \(EC2\)**, earlier in this topic\.\)

```
sudo yum -y install ruby
```

## Step 4: Download Example Code<a name="cloud9-ruby-examples"></a>

Use the terminal you opened in the previous step to download example code for the AWS SDK for Ruby into the AWS Cloud9 development environment\.

To do this, run the following command\. This command downloads a copy of all of the code examples used in the official AWS SDK documentation into your environment’s root directory\.

```
git clone https://github.com/awsdocs/aws-doc-sdk-examples.git
```

To find code examples for the AWS SDK for Ruby, use the **Environment** window to open the `ENVIRONMENT_NAME/aws-doc-sdk-examples/ruby` directory, where `ENVIRONMENT_NAME` is the name of your development environment\.

To learn how to work with these and other code examples, see [AWS SDK for Ruby Code Examples](examples.md)\.

## Step 5: Run Example Code<a name="cloud9-ruby-run"></a>

To run code in your AWS Cloud9 development environment, see [Run Your Code](https://docs.aws.amazon.com/cloud9/latest/user-guide/build-run-debug.html#build-run-debug-run) in the \.