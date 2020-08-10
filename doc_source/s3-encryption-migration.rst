.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

#####################################
Amazon S3 Encryption Client Migration
#####################################

.. meta::
   :description: Describes how to migrate to the latest S3 encryption clients for |sdk-ruby|.

This topic shows how to migrate your applications from Version 1 (V1) of the Amazon Simple Storage Service (Amazon S3) encryption 
client to Version 2 (V2), and ensure application availability throughout the migration process.

Migration Overview
==================

This migration happens in two phases: 

1. **Update existing clients to read new formats.** First, deploy an updated version of the |sdk-ruby| 
to your application. This will allow existing V1 encryption clients to decrypt objects written by the 
new V2 clients. If your application uses multiple AWS SDKs, you must upgrade each SDK separately. 

2. **Migrate encryption and decryption clients to V2.** Once all of your V1 encryption clients can 
read new formats, you can migrate your existing encryption and decryption clients to their respective 
V2 versions.


Update Existing Clients to Read New Formats
===========================================

The V2 encryption client uses encryption algorithms that older versions of the client don't support. 
The first step in the migration is to update your V1 decryption clients to the latest SDK release. 
After completing this step, your application’s V1 clients will be able to decrypt objects encrypted 
by V2 encryption clients.  See details below for each major version of the AWS SDK for Ruby.

Update AWS SDK for Ruby Version 3
---------------------------------

Version 3 is the latest version of the AWS SDK For Ruby. To complete this migration, you need to 
use version 1.76.0 or later of the ``aws-sdk-s3`` gem.

**Installing from the Command Line**

For projects that install the ``aws-sdk-s3`` gem, use the version option to verify that the minimum 
version of 1.76.0 is installed.

.. code-block:: ruby

 gem install aws-sdk-s3 -v '>= 1.76.0'

**Using Gemfiles**

For projects that use a Gemfile to manage dependencies, set the minimum version of the 
``aws-sdk-s3`` gem to 1.76.0. For example:

.. code-block:: ruby

  gem 'aws-sdk-s3', '>= 1.76.0'

#. Modify your Gemfile.
#. Run ``bundle update aws-sdk-s3``. To verify your version, run ``bundle info aws-sdk-s3``.

Upgdate AWS SDK for Ruby Version 2
----------------------------------

Version 2 of the AWS SDK for Ruby will enter `maintenance mode <https://aws.amazon.com/blogs/developer/deprecation-schedule-for-aws-sdk-for-ruby-v2/>`__ on 
November 21st, 2021. To complete this migration, you need to use version 2.11.562 or later of the aws-sdk gem.

**Installing from the Command Line**

For projects that install the ``aws-sdk`` gem, from the command line, use the version option 
to verify that the minimum version of 2.11.562 is installed.

.. code-block:: ruby

 gem install aws-sdk -v '>= 2.11.562'

**Using Gemfiles**

For projects that use a Gemfile to manage dependencies, set the minimum version of the ``aws-sdk`` gem to 2.11.562. 
For example:

.. code-block:: ruby

 gem 'aws-sdk', '>= 2.11.562'

#. Modify your Gemfile. If you have a Gemfile.lock file, delete or update it.
#. Run ``bundle update aws-sdk``. To verify your version, run ``bundle info aws-sdk``.

Migrate Encryption and Decryption Clients to V2
===============================================

After updating your clients to read the new encryption formats, you can update your applications to the V2 
encryption and decryption clients. The following steps show you how to successfully migrate your code from V1 to V2.

Before updating your code to use the V2 encryption client, ensure that you have followed the preceding steps and are 
using  the ``aws-sdk-s3`` gem version 2.11.562 or later. 

.. note:: When decrypting with AES-GCM, read the entire object to the end before you start using the decrypted data. This is to verify that the object has not been modified since it was encrypted.


Configuring V2 Encryption Clients
---------------------------------

The `EncryptionV2::Client` requires additional configuration. For detailed configuration 
information, see the `EncryptionV2::Client documentation <https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/S3/EncryptionV2/Client.html#initialize-instance_method>`__ 
or the examples provided later in this topic.

1. **The key wrap method and content encryption algorithm must be specified on client construction.**
When creating a new ``EncryptionV2::Client``, you need to provide values for ``key_wrap_schema`` and ``content_encryption_schema``.  
    
``key_wrap_schema`` - If you are using AWS KMS, this must be set to ``:kms_context``.  If you are using a symmetric (AES) key, it must 
be set to ``:aes_gcm``. If you are using an asymmetric (RSA) key, it must be set to ``:rsa_oaep_sha1``.  
    
``content_encryption_schema`` - This must be set to `:aes_gcm_no_padding`.
    
    
2. **security_profile must be specified on client construction.**
When creating a new ``EncryptionV2::Client``, you need to provide a value for ``security_profile``. The `security_profile` parameter determines 
the support for reading objects written using the older V1 ``Encryption::Client``.  There are two values: `:v2` and `:v2_and_legacy`.  
To support migration, set the ``security_profile`` to `:v2_and_legacy`.  Use `:v2` only for new application development.  
    
3. **AWS KMS CMK ID is enforced by default.**
In V1, ``Encryption::Client``, the ``kms_key_id`` used to create the client was not provided to the AWS KMS ``Decrypt call``. 
AWS KMS can get this information from metadata and add it to the symmetric ciphertext blob.  In V2, E`ncryptionV2::Client`, 
the `kms_key_id` is passed to the AWS KMS Decrypt call, and the call fails if it does not match the key used to encrypt the object.  
If your code previously relied on not setting a specific ``kms_key_id``, either set ``kms_key_id: :kms_allow_decrypt_with_any_cmk`` on 
client creation or set ``kms_allow_decrypt_with_any_cmk: true`` on ``get_object`` calls.

Example: Using a Symmetric (AES) Key
------------------------------------

**Pre-migration**

 .. code-block:: ruby

  client = Aws::S3::Encryption::Client.new(encryption_key: aes_key)
  client.put_object(bucket: bucket, key: key, body: secret_data)
  resp = client.get_object(bucket: bucket, key: key)

**Post-migration**

.. code-block:: ruby

  client = Aws::S3::EncryptionV2::Client.new(
    encryption_key: rsa_key,
    key_wrap_schema: :rsa_oaep_sha1, # the key_wrap_schema must be rsa_oaep_sha1 for asymmetric keys
    content_encryption_schema: :aes_gcm_no_padding, 
    security_profile: :v2_and_legacy # to allow reading/decrypting objects encrypted by the V1 encryption client
   )
  client.put_object(bucket: bucket, key: key, body: secret_data)  # No changes
  resp = client.get_object(bucket: bucket, key: key) # No changes

Example: Using AWS KMS with kms_key_id
--------------------------------------

**Pre-migration**

.. code-block:: ruby

 client = Aws::S3::Encryption::Client.new(kms_key_id: kms_key_id)
 client.put_object(bucket: bucket, key: key, body: secret_data)
 resp = client.get_object(bucket: bucket, key: key)

**Post-migration**

.. code-block:: ruby

 client = Aws::S3::EncryptionV2::Client.new(
   kms_key_id: kms_key_id,
   key_wrap_schema: :kms_context, # the key_wrap_schema must be kms_context for KMS keys
   content_encryption_schema: :aes_gcm_no_padding, 
   security_profile: :v2_and_legacy # to allow reading/decrypting objects encrypted by the V1 encryption client
 )
 client.put_object(bucket: bucket, key: key, body: secret_data)  # No changes
 resp = client.get_object(bucket: bucket, key: key) # No change

Example: Using AWS KMS without kms_key_id
-----------------------------------------

**Pre-migration**

.. code-block:: ruby

 client = Aws::S3::Encryption::Client.new(kms_key_id: kms_key_id)
 client.put_object(bucket: bucket, key: key, body: secret_data)
 resp = client.get_object(bucket: bucket, key: key)

**Post-migration**

.. code-block:: ruby

 client = Aws::S3::EncryptionV2::Client.new(
   kms_key_id: kms_key_id,
   key_wrap_schema: :kms_context, # the key_wrap_schema must be kms_context for KMS keys
   content_encryption_schema: :aes_gcm_no_padding, 
   security_profile: :v2_and_legacy # to allow reading/decrypting objects encrypted by the V1 encryption client
 )
 client.put_object(bucket: bucket, key: key, body: secret_data)  # No changes
 resp = client.get_object(bucket: bucket, key: key, kms_allow_decrypt_with_any_cmk: true) # To allow decrypting with any cmk

**Post-Migration Alternative**

If you only read and decrypt (never write and encrypt) objects using the S2 encryption client, use this code.

.. code-block:: ruby

 client = Aws::S3::EncryptionV2::Client.new(
   kms_key_id: :kms_allow_decrypt_with_any_cmk, # set kms_key_id to allow all get_object requests to use any cmk
   key_wrap_schema: :kms_context, # the key_wrap_schema must be kms_context for KMS keys
   content_encryption_schema: :aes_gcm_no_padding, 
   security_profile: :v2_and_legacy # to allow reading/decrypting objects encrypted by the V1 encryption client
 )
 resp = client.get_object(bucket: bucket, key: key) # No change

 