# Loading Items from a JSON File into an Amazon DynamoDB Table<a name="dynamo-example-load-table-items-from-json"></a>

The following example adds the items from the JSON file *movie\_data\.json* to the `Movies` table in the `us-west-2` region\.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

require 'aws-sdk-dynamodb'
require 'json'

# Adds an item to a table in Amazon DynamoDB.
#
# @param dynamodb_client [Aws::DynamoDB::Client] An initialized
#   Amazon DynamoDB client.
# @param table_item [Hash] The properties of the item, in the correct format.
# @example
#   add_item_to_table(
#     Aws::DynamoDB::Client.new(region, 'us-west-2'),
#     {
#       table_name: 'Movies',
#       item: {
#         "year": 1985,
#         "title": "The Big Movie",
#         "info": {
#           "directors": ["Mary"],
#           "release_date": "1985-12-25T00:00:00Z",
#           "rating": 5.5,
#           "genres": [
#             "Action",
#             "Drama"
#           ],
#           "image_url": "http://docs.aws.amazon.com/assets/images/aws_logo_dark.png",
#           "plot": "Nothing happens at all.",
#           "rank": 2,
#           "running_time_secs": 7380,
#           "actors": [
#             "Larry",
#             "Moe",
#             "Curly"
#           ]
#         }
#       }
#     }
#   )
def add_item_to_table(dynamodb_client, table_item)
  dynamodb_client.put_item(table_item)
  puts "Added movie: #{table_item[:item]['title']} " \
    "(#{table_item[:item]['year']})"
rescue StandardError => e
  puts 'Error adding movie ' \
    "#{table_item[:item]['title']} " \
    "(#{table_item[:item]['year']})': #{e.message}"
  puts 'Program stopped.'
  exit 1
end

# Full example call:
def run_me
  region = 'us-west-2'
  table_name = 'Movies'
  data_file = 'moviedata.json'

  dynamodb_client = Aws::DynamoDB::Client.new(region: region)
  file = File.read(data_file)
  movies = JSON.parse(file)

  puts "Adding movies from file '#{data_file}' " \
    "into table '#{table_name}'..."

  movies.each do |movie|
    table_item = {
      table_name: table_name,
      item: movie
    }
    add_item_to_table(dynamodb_client, table_item)
  end

  puts 'Done.'
end

run_me if $PROGRAM_NAME == __FILE__
```

Here is an example of a JSON file that loads two movies\.

```
[
    {
        "year": 2015,
        "title": "The Big New Movie",
        "info": {
            "plot": "Nothing happens at all.",
            "rating": 1.0,
            "directors" : [
                "Alice",
                "Bob"
            ],
            "release_date" : "2015-01-18T00:00:00Z",
            "genres" : [
                "Comedy",
                "Drama"
            ],
            "image_url" : "https://d0.awsstatic.com/logos/powered-by-aws.png",
            "rank" : 11,
            "running_time_secs" : 5215,
            "actors" : [
                "David",
                "Ann",
                "Jonathan"
            ]
        }
    },
    {
        "year": 2017,
        "title": "The Big New Movie 2",
        "info": {
            "plot": "Nothing happens at all again.",
            "rating": 2.0,
            "directors" : [
                "Joe",
                "Mary"
            ],
            "release_date" : "2017-01-17T00:00:00Z",
            "genres" : [
                "Comedy",
                "Drama"
            ],
            "image_url" : "https://d0.awsstatic.com/logos/powered-by-aws-white.png",
            "rank" : 10,
            "running_time_secs" : 5221,
            "actors" : [
                "Bob",
                "Sue",
                "Jim"
            ]
        }
    }
]
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/dynamodb/dynamodb_ruby_example_load_movies.rb) and the [JSON file](https://github.com/awsdocs/aws-doc-sdk-examples/blob/master/ruby/example_code/dynamodb/movie_data.json) on GitHub\.