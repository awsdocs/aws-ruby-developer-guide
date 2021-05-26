# Deleting an Amazon DynamoDB Table<a name="dynamo-example-delete-table"></a>

The following example deletes the `Movies` table in the `us-west-2` region\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

require 'aws-sdk-dynamodb'

# Deletes a table in Amazon DynamoDB.
#
# @param dynamodb_client [Aws::DynamoDB::Client] An initialized
#   Amazon DynamoDB client.
# @param table_name [String] The name of the table to delete.
# @return [Boolean] true if the table was deleted; otherwise, false.
# @example
#   ext 1 unless table_deleted?(
#     Aws::DynamoDB::Client.new(region, 'us-west-2'),
#     'Movies'
#   )
def table_deleted?(dynamodb_client, table_name)
  dynamodb_client.delete_table(table_name: table_name)
  true
rescue StandardError => e
  puts "Error deleting table: #{e.message}"
  false
end

# Full example call:
def run_me
  region = 'us-west-2'
  table_name = 'Movies'

  dynamodb_client = Aws::DynamoDB::Client.new(region: region)

  puts "Deleting table '#{table_name}'..."

  if table_deleted?(dynamodb_client, table_name)
    puts 'Table deleted.'
  else
    puts 'Table not deleted.'
  end
end

run_me if $PROGRAM_NAME == __FILE__
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/dynamodb/dynamodb_ruby_example_delete_movies_table.rb) on GitHub\.