# Installing the AWS SDK for Ruby<a name="setup-install"></a>

This section includes prerequisites and installation instructions for the AWS SDK for Ruby\.

## Prerequisites<a name="aws-ruby-sdk-prerequisites"></a>

Before you install the AWS SDK for Ruby, you need an AWS account and Ruby version 1\.9 or later\.

If you don’t have an AWS account, use the following procedure to create one\.

1. Open [http://aws\.amazon\.com/](https://aws.amazon.com/) and choose **Create an AWS Account**\.

1. Follow the online instructions\.

## Installing the SDK<a name="installing-the-sdk"></a>

If your project uses [Bundler](http://bundler.io/), add the following line to your `Gemfile` to add the AWS SDK for Ruby to your project\.

```
gem 'aws-sdk'
```

If you don’t use Bundler, the easiest way to install the SDK is to use [RubyGems](https://rubygems.org/gems/aws-sdk/)\. To install the latest version of the SDK, use the following command\.

```
gem install aws-sdk
```

If the previous command fails on your Unix\-based system, use `sudo` to install the SDK, as shown in the following command\.

```
sudo gem install aws-sdk
```