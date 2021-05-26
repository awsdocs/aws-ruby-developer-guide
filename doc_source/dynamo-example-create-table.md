# Creating an Amazon DynamoDB Table<a name="dynamo-example-create-table"></a>

The following example creates the table `Movies` with two required attributes: `year` and `title` in the `us-west-2` region\.

The `wait_until` call blocks you from using the table until DynamoDB has created it\. By default, the DynamoDB client’s `wait_until` method checks every 20 seconds, up to a maximum of 500 seconds, to see if the table was created\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

require 'aws-sdk-dynamodb'

# Creates a table in Amazon DynamoDB.
#
# @param dynamodb_client [Aws::DynamoDB::Client] An initialized
#   Amazon DynamoDB client.
# @param table_definition [Hash] The properties of the new table, 
#   specified in the correct hash format.
# @return [String] The creation status of the new table or the
#   string 'Error'.
# @example
#   puts create_table(
#     Aws::DynamoDB::Client.new(region: 'us-west-2'),
#     {
#       table_name: 'Movies',
#       key_schema: [
#         {
#           attribute_name: 'year',
#           key_type: 'HASH'  # Partition key.
#         },
#         {
#           attribute_name: 'title',
#           key_type: 'RANGE' # Sort key.
#         }
#       ],
#       attribute_definitions: [
#         {
#           attribute_name: 'year',
#           attribute_type: 'N'
#         },
#         {
#           attribute_name: 'title',
#           attribute_type: 'S'
#         }
#       ],
#       provisioned_throughput: {
#         read_capacity_units: 10,
#         write_capacity_units: 10
#       }
#     }
#   )
def create_table(dynamodb_client, table_definition)
  response = dynamodb_client.create_table(table_definition)
  response.table_description.table_status
rescue StandardError => e
  puts "Error creating table: #{e.message}"
  'Error'
end

# Full example call:
def run_me
  region = 'us-west-2'
  table_name = 'Movies'

  dynamodb_client = Aws::DynamoDB::Client.new(region: region)

  table_definition = {
    table_name: table_name,
    key_schema: [
      {
        attribute_name: 'year',
        key_type: 'HASH'  # Partition key.
      },
      {
        attribute_name: 'title',
        key_type: 'RANGE' # Sort key.
      }
    ],
    attribute_definitions: [
      {
        attribute_name: 'year',
        attribute_type: 'N'
      },
      {
        attribute_name: 'title',
        attribute_type: 'S'
      }
    ],
    provisioned_throughput: {
      read_capacity_units: 10,
      write_capacity_units: 10
    }
  }

  puts "Creating the table named '#{table_name}'..."
  create_table_result = create_table(dynamodb_client, table_definition)

  if create_table_result == 'Error'
    puts 'Table not created.'
  else
    puts "Table created with status '#{create_table_result}'."
  end
end

run_me if $PROGRAM_NAME == __FILE__
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/dynamodb/dynamodb_ruby_example_create_movies_table.rb) on GitHub\.