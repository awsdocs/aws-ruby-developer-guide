# Paging Response Data<a name="paging-responses"></a>

Some AWS calls provide paged responses to limit the amount of data returned with each response\. A page of data represents up to 1,000 items\.

## Paged Responses Are Enumerable<a name="aws-ruby-sdk-paged-response-enumerable"></a>

The simplest way to handle paged response data is to use the built\-in enumerator in the response object, as shown in the following example\.

```
s3 = Aws::S3::Client.new

s3.list_objects(bucket:'aws-sdk').each do |response|
  puts response.contents.map(&:key)
end
```

This yields one response object per API call made, and enumerates objects in the named bucket\. The SDK retrieves additional pages of data to complete the request\.

## Handling Paged Responses Manually<a name="aws-ruby-sdk-handling-paged-response-handling"></a>

To handle paging yourself, use the response’s `next_page?` method to verify there are more pages to retrieve, or use the `last_page?` method to verify there are no more pages to retrieve\.

If there are more pages, use the `next_page` \(notice there is no `?`\) method to retrieve the next page of results, as shown in the following example\.

```
s3 = Aws::S3::Client.new

# Get the first page of data
response = s3.list_objects(bucket:'aws-sdk')

# Get additional pages
while response.next_page? do
  response = response.next_page
  # Use the response data here...
end
```

**Note**  
If you call the `next_page` method and there are no more pages to retrieve, the SDK raises an [Aws::PageableResponse::LastPageError](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/PageableResponse/LastPageError.html) exception\.

## Paged Data Classes<a name="aws-ruby-sdk-paged-data-classes"></a>

Paged data in the AWS SDK for Ruby is handled by the [Aws::PageableResponse](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/PageableResponse.html) class, which is included with [Seahorse::Client::Response](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Seahorse/Client/Response.html) to provide access to paged data\.