.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

#######################################
Hello World Tutorial for the |sdk-ruby|
#######################################

.. meta::
    :description:
        Use this Hello World tutorial to get started using the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby hello world, aws.rb, aws-sdk-core gem, AWS SDK for Ruby code examples

This tutorial shows you how to use the |sdk-ruby| to create a command line program that performs some
common |S3| operations.

.. _aws-ruby-sdk-hello-world-require:

Using the |sdk-ruby| in Your Program
====================================

Add a :code:`require` statement to the top of your Ruby source file so you can use the classes and
methods provided by the |sdk-ruby|.

.. code-block:: ruby

    require 'aws-sdk'

.. _aws-ruby-sdk-hello-world-get-resource:

Creating an |S3| Resource
=========================

Create an
`Aws::S3::Resource <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Resource.html>`_
object in the appropriate region.
The following example creates an |S3| resource object in the :code:`us-west-2` region.
Note that the region is not important because |S3| resources are not specific to a region.

.. code-block:: ruby

    s3 = Aws::S3::Resource.new(region: 'us-west-2')

.. _aws-ruby-sdk-hello-world-create-bucket:

Creating a Bucket
=================

To store anything on |S3|, you need a bucket to put it in.

Create an `Aws::S3::Bucket <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html>`_ object.
The following example creates the bucket :code:`my_bucket` with the name :code:`my-bucket`.

.. code-block:: ruby

    my_bucket = s3.bucket('my-bucket')
    my_bucket.create

.. _aws-ruby-sdk-hello-world-add-to-bucket:

Adding a File to the Bucket
===========================

Use the :code:`#upload_file` method to add a file to the bucket. The following example adds the file
named :code:`my_file` to the bucket named :code:`my-bucket`.

.. code-block:: ruby

    name = File.basename 'my_file'
    obj = s3.bucket('my-bucket').object(name)
    obj.upload_file('my_file')

.. _aws-ruby-sdk-hello-world-list-bucket-contents:

Listing the Contents of a Bucket
================================

To list the contents of a bucket, use the `Aws::S3::Bucket:Objects
<http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html#objects-instance_method>`_ method. The
following example lists up to 50 bucket items for the bucket :code:`my-bucket`.

.. code-block:: ruby

    my_bucket.objects.limit(50).each do |obj|
      puts "  #{obj.key} => #{obj.etag}"
    end

.. _aws-ruby-sdk-hello-world-listing:

Complete Program
================

The following is the entire :code:`hello-s3.rb` program.

.. code-block:: ruby

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

.. _aws-ruby-sdk-hello-world-running:

Running the Program
===================

To list the contents of a bucket, use either of the following commands, where :code:`bucket-name` is the
name of the bucket to list. You don't have to include :code:`list` because it's the default operation.

.. code-block:: sh

    ruby hello-s3.rb bucket-name list
    ruby hello-s3.rb bucket-name

To create a bucket, use the following command, where :code:`bucket-name` is the name of the bucket you
want to create.

.. code-block:: sh

    ruby hello-s3.rb bucket-name create

If |S3| already has a bucket named :code:`bucket-name`, the service issues an error message and does not
create another copy.

After you create your bucket, you can upload an object to the bucket. The following command adds
:code:`your_file.txt` to the bucket.

.. code-block:: sh

    ruby hello-s3.rb bucket-name upload your_file.txt

.. _aws-ruby-sdk-hello-world-next-steps:

Next Steps
==========

Now that you've completed your first |sdk-ruby| application, here are some suggestions to extend the
code you just wrote:

* Use the :code:`buckets` collection from the `Aws::S3::Resource <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Resource.html>`_ class to get a list of buckets.

* Use :code:`#get` method from the `Bucket <http://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/Bucket.html>`_ class to download an object from the bucket.

* Use the code in :ref:`aws-ruby-sdk-hello-world-add-to-bucket` to confirm the item exists in the bucket, and then update that bucket item.
