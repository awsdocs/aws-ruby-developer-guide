.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-migrating-to-v3:

############################################################
Migrating from Version 1 or 2 to Version 3 of the |sdk-ruby|
############################################################

.. meta::
    :description:
        Details about how to migrate from version 1 or 2 to version 3 of the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby

The purpose of this topic is to help you migrate from version 1 or 2 of the |sdk-ruby| to version 3.

.. _side-by-side-usage:

Side-by-Side Usage
==================

It isn't necessary to replace the version 1 or 2 of the |sdk-ruby| with
version 3.
You can use them together in the same application.
See `this blog post <http://ruby.awsblog.com/post/TxFKSK2QJE6RPZ/Upcoming-Stable-Release-of-AWS-SDK-for-Ruby-Version-2>`_
for more information.

A quick example follows.

.. code-block:: ruby

   require 'aws-sdk-v1' # version 1
   require 'aws-sdk'    # version 2
   require 'aws-sdk-s3' # version 3

   s3 = AWS::S3::Client.new # version 1
   s3 = Aws::S3::Client.new # version 2 or 3

You don't need to rewrite existing working version 1 or 2 code to start using
the version 3 SDK.
A valid migration strategy is to only write new code against the version 3 SDK.

.. _general-differences:

General Differences
===================

Version 3 differs from version 2 in one important way.

* Each service is available as a separate gem.

Version 2 differs from version 1 in several important ways.

* Different root namespace |ndash| :code:`Aws` versus :code:`AWS`. This enables side-by-side usage.
* :code:`Aws.config` |ndash| Now a vanilla Ruby hash, instead of a method.
* Strict constructor options - When constructing a client or resource object in the version 1 SDK,
  unknown constructor options are ignored. In version 2, unknown constructor options trigger an
  :code:`ArgumentError`. For example:

  .. code-block:: ruby

     # version 1
     AWS::S3::Client.new(http_reed_timeout: 10)
     # oops, typo'd option is ignored

     # version 2
     Aws::S3::Client.new(http_reed_timeout: 10)
     # => raises ArgumentError

.. _client-differences:

Client Differences
==================

There are no differences between the client classes in version 2 and version 3.

Between version 1 and version 2, the client classes have the fewest external differences. Many service clients
will have compatible interfaces after client construction. Some important differences:

* :code:`Aws::S3::Client` - The version 1 |S3| client class was hand-coded. Version 2 is generated from a
  service model. Method names and inputs are very different in version 2.
* :code:`Aws::EC2::Client`- Version 2 uses plural names for output lists, version 1 uses the suffix :code:`_set`.
  For example:

  .. code-block:: ruby

     # version 1
     resp = AWS::EC2::Client.new.describe_security_groups
     resp.security_group_set
     #=> [...]

     # version 2
     resp = Aws::EC2::Client.new.describe_security_groups
     resp.security_groups
     #=> [...]

* :code:`Aws::SWF::Client` |ndash| Version 2 uses structured responses, where version 1 uses vanilla
  Ruby hashes.
* Service class renames |ndash| Version 2 uses a different name for multiple services:

  * :code:`AWS::SimpleWorkflow` has become :code:`Aws::SWF`
  * :code:`AWS::ELB` has become :code:`Aws::ElasticLoadBalancing`
  * :code:`AWS::SimpleEmailService` has become :code:`Aws::SES`

* Client configuration options |ndash| Some of the version 1 configuration options are renamed in
  version 2.
  Others are removed or replaced. Here are the primary changes:

  * :code:`:use_ssl` has been removed. Version 2 uses SSL everywhere. To disable SSL you must configure an
    :code:`:endpoint` that uses :code:`http://`.
  * :code:`:ssl_ca_file` is now :code:`:ssl_ca_bundle`
  * :code:`:ssl_ca_path` is now :code:`:ssl_ca_directory`
  * Added :code:`:ssl_ca_store`.
  * :code:`:endpoint` must now be a fully qualified HTTP or HTTPS URI instead of a hostname.
  * Removed :code:`:*_port` options for each service, now replaced by :code:`:endpoint`.
  * :code:`:user_agent_prefix` is now :code:`:user_agent_suffix`

.. _resource-differences:

Resource Differences
====================

There are no differences between the resource interfaces in version 2 and version 3.

There are significant differences between the resource interfaces in version 1 and version 2. Version 1 was
entirely hand-coded, where as version 2 resource interfaces are generated from a model. Version 2 resource
interfaces are significantly more consistent. Some of the systemic differences include:

* Separate resource class |ndash| In version 2, the service name is a module, not a class. In this
  module, it is the resource interface:

  .. code-block:: ruby

     # version 1
     s3 = AWS::S3.new

     # version 2
     s3 = Aws::S3::Resource.new

* Referencing resources |ndash| The version 2 SDK separates collections and individual resource getters
  into two different methods:

  .. code-block:: ruby

     # version 1
     s3.buckets['bucket-name'].objects['key'].delete

     # version 2
     s3.bucket('bucket-name').object('key').delete

* Batch operations |ndash| In version 1, all batch operations were hand-coded utilities. In version 2,
  many batch operations are autogenerated batching operations over the API.
  **Version 2 batching interfaces are very different from version 1.**
