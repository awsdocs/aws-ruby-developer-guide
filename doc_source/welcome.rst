.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-about-ruby-sdk:

################################
AWS SDK for Ruby Developer Guide
################################

.. meta::
    :description:
        Build Ruby applications on top of APIs that use the cost-effective, scalable, and reliable
        AWS infrastructure services with the |sdk-ruby|.
    :keywords: AWS SDK for ruby, aws.rb, aws-sdk-core gem, ruby code examples

Welcome to the |sdk-ruby|.

The |sdk-ruby| helps take the complexity out of coding by providing Ruby classes for almost all AWS
services, including |S3long|, |EC2long|, and |DDBlong|.
For a complete list of services supported by the
|sdk-ruby|, see the `Supported Services
<https://github.com/aws/aws-sdk-ruby/blob/master/README.md#supported-services>`_
section of the |sdk-ruby| Readme file.
This section also lists the gems that the |sdk-ruby| supports as version 3
modularized the monolithic SDK gem into service-specific gems.

.. _aws-ruby-sdk-developer-guide-cloud9:

Using the AWS SDK for Ruby with AWS Cloud9
==========================================

AWS Cloud9 is a web-based integrated development environment (IDE) that
contains a collection of tools that you use to code, build, run, test, debug,
and release software in the cloud.

See :doc:`cloud9-ruby` for information on using |AC9long| with the |sdk-ruby|.

.. _aws-ruby-sdk-developer-guide-contents:

About This Guide
================

The |sdk-ruby-dg| provides information about how to install, set up, and use the |sdk-ruby| to
create Ruby applications that use AWS services.

This guide contains the following sections:

:doc:`getting-started`
    Describes how to install, configure, and use the |sdk-ruby|.

:doc:`setup-config`
    Steps you through how to configure the |sdk-ruby|.

:doc:`programming`
    Provides general information about developing applications with the |sdk-ruby|.

:doc:`examples`
    Provides code examples for programming AWS services with the |sdk-ruby|.
    You can browse the |sdk-ruby| examples in the
    `AWS Code Sample Catalog <https://docs.aws.amazon.com/code-samples/latest/catalog/code-catalog-ruby.html>`_.

:doc:`tips-and-tricks`
    Provides helpful information for using the |sdk-ruby| with AWS services.

:doc:`history`
    Describes the history of this document.

.. _aws-ruby-sdk-additional-information:

Additional Documentation and Resources
======================================

For more resources for |sdk-ruby| developers, see the following:

* :sdk-ruby-api:`AWS SDK for Ruby API Reference - Version 3`
* `Developer blog <http://ruby.awsblog.com/>`_
* `Developer forums <https://forums.aws.amazon.com/forum.jspa?forumID=125>`_
  (you must have an AWS account to access the forums)
* `Gitter channel <https://gitter.im/aws/aws-sdk-ruby>`_
* `@awsforruby <https://twitter.com/awsforruby>`_ on Twitter
* On GitHub:

  + :ruby-sdk:`Releases <releases>` (includes source, gems, and documentation)
  + :ruby-sdk:`Source <>`
  + :ruby-sdk:`Change logs under each gem <blob/master/gems>`
  + :ruby-sdk:`Moving from v1 to v2 <blob/master/MIGRATING.md>`
  + :ruby-sdk:`Moving from v2 to v3 <blob/master/V3_UPGRADING_GUIDE.md>`
  + :ruby-sdk:`Issues <issues>`
  + :ruby-sdk:`Core upgrade notes <blob/master/UPGRADING.md>`

.. _aws-ruby-sdk-deploying:

Deploying to the AWS Cloud
--------------------------

You can use AWS services such as |AEBlong|, |OPS|, and |ACD| to deploy your application to the AWS Cloud.
For deploying Ruby applications with |AEB|, see
:AEB-dg:`Deploying Elastic Beanstalk Applications in Ruby Using EB CLI and Git <create_deploy_Ruby>`
in the |AEB-dg|. For deploying a Ruby on Rails application with |OPS|, see
`Deploying Ruby on Rails Applications to AWS OpsWorks <http://ruby.awsblog.com/post/Tx7FQMT084INCR/Deploying-Ruby-on-Rails-Applications-to-AWS-OpsWorks>`_.
For an overview of AWS deployment services, see
`Overview of Deployment Options on AWS <https://d0.awsstatic.com/whitepapers/overview-of-deployment-options-on-aws.pdf>`_.
