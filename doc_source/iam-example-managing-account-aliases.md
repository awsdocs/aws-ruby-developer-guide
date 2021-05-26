# Managing IAM Account Aliases<a name="iam-example-managing-account-aliases"></a>

If you want the URL for your sign\-in page to contain your company name or other friendly identifier instead of your AWS account ID, you can create an IAM account alias for your AWS account ID\. If you create an IAM account alias, your sign\-in page URL changes to incorporate the alias\. For more information about IAM account aliases, see [Your AWS Account ID and Its Alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html)\.

In this example, you use the AWS SDK for Ruby with IAM to:

1. List AWS account aliases, using [Aws::IAM::Client\#list\_account\_aliases](https://docs.aws.amazon.com/sdkforruby/api/Aws/IAM/Client.html#list_account_aliases-instance_method)\.

1. Create an account alias, using [Aws::IAM::Client\#create\_account\_alias](https://docs.aws.amazon.com/sdkforruby/api/Aws/IAM/Client.html#create_account_alias-instance_method)\.

1. Delete the account alias, using [Aws::IAM::Client\#delete\_account\_alias](https://docs.aws.amazon.com/sdkforruby/api/Aws/IAM/Client.html#delete_account_alias-instance_method)\.

## Prerequisites<a name="prerequisites"></a>

Before running the example code, you need to install and configure the AWS SDK for Ruby, as described in:
+  [Installing the AWS SDK for Ruby](setup-install.md#aws-ruby-sdk-setup-install) 
+  [Configuring the AWS SDK for Ruby](setup-config.md#aws-ruby-sdk-setup-config) 

In the example code, change the *my\-account\-alias* string to something that will be unique across all Amazon Web Services products\.

## Example<a name="example"></a>

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX - License - Identifier: Apache - 2.0

# The following code example shows how to:
# 1. List available AWS account aliases.
# 2. Create an account alias.
# 3. Delete an account alias.

require 'aws-sdk-iam'

# Lists available AWS account aliases.
#
# @param iam [Aws::IAM::Client] An initialized IAM client.
# @example
#   puts list_aliases(Aws::IAM::Client.new)
def list_aliases(iam)
  response = iam.list_account_aliases

  if response.account_aliases.count.positive?
    response.account_aliases.each do |account_alias|
      puts "  #{account_alias}"
    end
  else
    puts 'No account aliases found.'
  end
rescue StandardError => e
  puts "Error listing account aliases: #{e.message}"
end

# Creates an AWS account alias.
#
# @param iam [Aws::IAM::Client] An initialized IAM client.
# @param account_alias [String] The name of the account alias to create.
# @return [Boolean] true if the account alias was created; otherwise, false.
# @example
#   exit 1 unless alias_created?(Aws::IAM::Client.new, 'my-account-alias')
def alias_created?(iam, account_alias)
  iam.create_account_alias(account_alias: account_alias)
  return true
rescue StandardError => e
  puts "Error creating account alias: #{e.message}"
  return false
end

# Deletes an AWS account alias.
#
# @param iam [Aws::IAM::Client] An initialized IAM client.
# @param account_alias [String] The name of the account alias to delete.
# @return [Boolean] true if the account alias was deleted; otherwise, false.
# @example
#   exit 1 unless alias_deleted?(Aws::IAM::Client.new, 'my-account-alias')
def alias_deleted?(iam, account_alias)
  iam.delete_account_alias(account_alias: account_alias)
  return true
rescue StandardError => e
  puts "Error deleting account alias: #{e.message}"
  return false
end

# Full example call:
def run_me
  iam = Aws::IAM::Client.new
  account_alias = 'my-account-alias'
  create_alias = true # Change to false to not generate an account alias.
  delete_alias = true # Change to false to not delete any generated account alias.

  puts 'Account aliases are:'
  list_aliases(iam)

  if create_alias
    puts 'Attempting to create account alias...'
    if alias_created?(iam, account_alias)
      puts 'Account alias created. Account aliases now are:'
      list_aliases(iam)
    else
      puts 'Account alias not created. Stopping program.'
      exit 1
    end
  end

  if create_alias && delete_alias
    puts 'Attempting to delete account alias...'
    if alias_deleted?(iam, account_alias)
      puts 'Account alias deleted. Account aliases now are:'
      list_aliases(iam)
    else
      puts 'Account alias not deleted. You will need to delete ' \
        'the alias yourself.'
    end
  end
end

run_me if $PROGRAM_NAME == __FILE__
```