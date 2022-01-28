# Hello World Tutorial for the AWS SDK for Ruby<a name="hello"></a>

This tutorial shows you how to use the AWS SDK for Ruby to create a command line program that performs some common Amazon S3 operations\.

## Using the AWS SDK for Ruby in Your Program<a name="aws-ruby-sdk-hello-world-require"></a>

Add a `require` statement to the top of your Ruby source file so you can use the classes and methods provided by the AWS SDK for Ruby\.

```
require 'aws-sdk'
```

## Creating an Amazon S3 Resource<a name="aws-ruby-sdk-hello-world-get-resource"></a>

Create an [Aws::S3::Resource](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Resource.html) object in the appropriate region\. The following example creates an Amazon S3 resource object in the `us-west-2` region\. Note that the region is not important because Amazon S3 resources are not specific to a region\.

```
s3 = Aws::S3::Resource.new(region: 'us-west-2')
```

## Creating a Bucket<a name="aws-ruby-sdk-hello-world-create-bucket"></a>

To store anything on Amazon S3, you need a bucket to put it in\.

Create an [Aws::S3::Bucket](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html) object\. The following example creates the bucket `my_bucket` with the name `my-bucket`\.

```
my_bucket = s3.bucket('my-bucket')
my_bucket.create
```

## Adding a File to the Bucket<a name="aws-ruby-sdk-hello-world-add-to-bucket"></a>

Use the `#upload_file` method to add a file to the bucket\. The following example adds the file named `my_file` to the bucket named `my-bucket`\.

```
name = File.basename 'my_file'
obj = s3.bucket('my-bucket').object(name)
obj.upload_file('my_file')
```

## Listing the Contents of a Bucket<a name="aws-ruby-sdk-hello-world-list-bucket-contents"></a>

To list the contents of a bucket, use the [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html#objects-instance_method](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html#objects-instance_method) method\. The following example lists up to 50 bucket items for the bucket `my-bucket`\.

```
my_bucket.objects.limit(50).each do |obj|
  puts "  #{obj.key} => #{obj.etag}"
end
```

## Complete Program<a name="aws-ruby-sdk-hello-world-listing"></a>

The following is the entire `hello-s3.rb` program\.

```
require 'aws-sdk'

NO_SUCH_BUCKET = "The bucket '%s' does not exist!"

USAGE = <<DOC

Usage: hello-s3 bucket_name [operation] [file_name]

Where:
  bucket_name (required) is the name of the bucket

  operation   is the operation to perform on the bucket:
              create  - creates a new bucket
              upload  - uploads a file to the bucket
              list    - (default) lists up to 50 bucket items

  file_name   is the name of the file to upload,
              required when operation is 'upload'

DOC

# Set the name of the bucket on which the operations are performed
# This argument is required
bucket_name = nil

if ARGV.length > 0
  bucket_name = ARGV[0]
else
  puts USAGE
  exit 1
end

# The operation to perform on the bucket
operation = 'list' # default
operation = ARGV[1] if (ARGV.length > 1)

# The file name to use with 'upload'
file = nil
file = ARGV[2] if (ARGV.length > 2)

# Get an Amazon S3 resource
s3 = Aws::S3::Resource.new(region: 'us-west-2')

# Get the bucket by name
bucket = s3.bucket(bucket_name)

case operation
when 'create'
  # Create a bucket if it doesn't already exist
  if bucket.exists?
    puts "The bucket '%s' already exists!" % bucket_name
  else
    bucket.create
    puts "Created new S3 bucket: %s" % bucket_name
  end

when 'upload'
  if file == nil
    puts "You must enter the name of the file to upload to S3!"
    exit
  end

  if bucket.exists?
    name = File.basename file

    # Check if file is already in the bucket
    if bucket.object(name).exists?
      puts "#{name} already exists in the bucket"
    else
      obj = s3.bucket(bucket_name).object(name)
      obj.upload_file(file)
      puts "Uploaded '%s' to S3!" % name
    end
  else
    NO_SUCH_BUCKET % bucket_name
  end

when 'list'
  if bucket.exists?
    # Enumerate the bucket contents and object etags
    puts "Contents of '%s':" % bucket_name
    puts '  Name => GUID'

    bucket.objects.limit(50).each do |obj|
      puts "  #{obj.key} => #{obj.etag}"
    end
  else
    NO_SUCH_BUCKET % bucket_name
  end

else
  puts "Unknown operation: '%s'!" % operation
  puts USAGE
end
```

## Running the Program<a name="aws-ruby-sdk-hello-world-running"></a>

To list the contents of a bucket, use either of the following commands, where `bucket-name` is the name of the bucket to list\. You don’t have to include `list` because it’s the default operation\.

```
ruby hello-s3.rb bucket-name list
ruby hello-s3.rb bucket-name
```

To create a bucket, use the following command, where `bucket-name` is the name of the bucket you want to create\.

```
ruby hello-s3.rb bucket-name create
```

If Amazon S3 already has a bucket named `bucket-name`, the service issues an error message and does not create another copy\.

After you create your bucket, you can upload an object to the bucket\. The following command adds `your_file.txt` to the bucket\.

```
ruby hello-s3.rb bucket-name upload your_file.txt
```

## Next Steps<a name="aws-ruby-sdk-hello-world-next-steps"></a>

Now that you’ve completed your first AWS SDK for Ruby application, here are some suggestions to extend the code you just wrote:
+ Use the `buckets` collection from the [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Resource.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Resource.html) class to get a list of buckets\.
+ Use `#get` method from the [https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html](https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html) class to download an object from the bucket\.
+ Use the code in [Adding a File to the Bucket](#aws-ruby-sdk-hello-world-add-to-bucket) to confirm the item exists in the bucket, and then update that bucket item\.