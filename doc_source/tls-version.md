# Using TLS 1\.2 in AWS SDK for Ruby<a name="tls-version"></a>

Communication between the AWS SDK for Ruby and AWS is secured using Secure Sockets Layer \(SSL\) or Transport Layer Security \(TLS\)\. All versions of SSL, and versions of TLS earlier than 1\.2, have vulnerabilities that can compromise the security of your communication with AWS\. For this reason, you should make sure that you’re using the AWS SDK for Ruby with a version of Ruby that supports TLS version 1\.2 or later\.

Ruby uses the OpenSSL library to secure HTTP connections\. Supported versions of Ruby \(1\.9\.3 and later\) installed through system [package managers](https://www.ruby-lang.org/en/documentation/installation/#package-management-systems) \(`yum`, `apt`, and others\), an [official installer](https://www.ruby-lang.org/en/documentation/installation/#installers), or Ruby [managers](https://www.ruby-lang.org/en/documentation/installation/#managers) \(rbenv, RVM, and others\) typically incorporate OpenSSL 1\.0\.1 or later, which supports TLS 1\.2\.

When used with a supported version of Ruby with OpenSSL 1\.0\.1 or later, the AWS SDK for Ruby prefers TLS 1\.2, and uses the latest version of SSL or TLS supported by both the client and server\. This is always at least TLS 1\.2 for AWS services\. \(The SDK uses the Ruby `Net::HTTP` class with `use_ssl=true`\.\)

## Checking the OpenSSL version<a name="checking-the-openssl-version"></a>

To make sure your installation of Ruby is using OpenSSL 1\.0\.1 or later, enter the following command\.

```
ruby -r openssl -e 'puts OpenSSL::OPENSSL_VERSION'
```

An alternative way to get the OpenSSL version is to query the `openssl` executable directly\. First, locate the appropriate executable using the following command\.

```
ruby -r rbconfig -e 'puts RbConfig::CONFIG["configure_args"]'
```

The output should have `--with-openssl-dir=/path/to/openssl` indicating the location of the OpenSSL installation\. Make a note of this path\. To check the version of OpenSSL, enter the following commands\.

```
cd /path/to/openssl
bin/openssl version
```

This latter method might not work with all installations of Ruby\.

## Upgrading TLS support<a name="upgrading-tls-support"></a>

If the version of OpenSSL used by your Ruby installation is earlier than 1\.0\.1, upgrade your Ruby or OpenSSL installation using your system package manager, Ruby installer, or Ruby manager, as described in Ruby’s [installation guide](https://www.ruby-lang.org/en/documentation/installation/)\. If you’re installing Ruby [from source](https://www.ruby-lang.org/en/documentation/installation/#building-from-source), install the [latest OpenSSL](https://www.openssl.org/source/) first, and then pass `--with-openssl-dir=/path/to/upgraded/openssl` when running `./configure`\.