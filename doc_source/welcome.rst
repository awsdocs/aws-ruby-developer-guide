.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-about-ruby-sdk:

####################
About the |sdk-ruby|
####################

The |sdk-ruby| helps take the complexity out of coding by providing Ruby classes for almost all AWS
services, including |S3|, |EC2|, and |DDBlong|. For a complete list of services supported by the
|sdk-ruby|, see `the SDK readme file <#supported-services>`_.

.. _aws-ruby-sdk-developer-guide-contents:

About This Guide
================

The |sdk-ruby| Developer Guide provides information about how to install, set up, and use the
|sdk-ruby| to create Ruby applications that use AWS services.

This guide contains the following sections:

:ref:`aws-ruby-sdk-getting-started`
    Describes how to set up and use the |sdk-ruby|.

:ref:`aws-ruby-sdk-hello-world-tutorial`
    Steps you through creating an application using the |sdk-ruby|.

:ref:`aws-ruby-sdk-programming`
    Provides general information about developing software with the |sdk-ruby|.

:ref:`aws-ruby-sdk-recipes`
    Provides code samples that developers can copy and paste to program AWS services with the
    |sdk-ruby|.

:ref:`aws-ruby-sdk-document-history`
    Describes the history of this document.


.. _aws-ruby-sdk-additional-information:

Other Resources
===============

In addition to this guide, here are other resources available for |sdk-ruby| developers:

* `AWS SDK for Ruby API Reference <http://docs.aws.amazon.com/sdkforruby/api/>`_
* `Developer blog <http://ruby.awsblog.com/>`_
* `Developer forums <https://forums.aws.amazon.com/forum.jspa?forumID=125>`_
  (You must have an AWS account to access the forums)
* `Gitter channel <https://gitter.im/aws/aws-sdk-ruby>`_
* `@awsforruby <https://twitter.com/awsforruby>`_ on Twitter

GitHub:

* `Releases <https://github.com/aws/aws-sdk-ruby/releases>`_ (includes source, gems, and documentation)
* `Source <https://github.com/aws/aws-sdk-ruby>`_
* `Change log <https://github.com/aws/aws-sdk-ruby/blob/master/CHANGELOG.md>`_
* `Migration Guide <https://github.com/aws/aws-sdk-ruby/blob/master/MIGRATING.md>`_
* `Issues <https://github.com/aws/aws-sdk-ruby/issues>`_
* `Feature requests <https://github.com/aws/aws-sdk-ruby/blob/master/FEATURE_REQUESTS.md>`_
* `Upgrading notes <https://github.com/aws/aws-sdk-ruby/blob/master/UPGRADING.md>`_

.. _aws-ruby-sdk-deploying:

Deploying to the AWS Cloud
--------------------------

You can use AWS services such as |AEBlong|, |OPS|, and |ACD| to deploy your application to the AWS cloud.
For information about deploying Ruby applications with |AEB|, see
`Working with Ruby <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_Ruby.html>`_
in the |AEB| Developer Guide. For information about deploying a Ruby on Rails application with |OPS|, see
`Deploying Ruby on Rails Applications to AWS OpsWorks <http://ruby.awsblog.com/post/Tx7FQMT084INCR/Deploying-Ruby-on-Rails-Applications-to-AWS-OpsWorks>`_.
For an overview of AWS deployment services, see
`Overview of Deployment Options on AWS <https://d0.awsstatic.com/whitepapers/overview-of-deployment-options-on-aws.pdf>`_.

About Amazon Web Services
-------------------------

Amazon Web Services (AWS) is a collection of digital infrastructure services that developers can leverage when developing their applications.
The services include computing, storage, database, and application synchronization(messaging and queuing).
AWS uses a pay-as-you-go service model.
You are charged only for the services that you-or your applications-use.
Also, to make AWS more approachable as a platform for prototyping and experimentation, AWS offers a free usage tier.
On this tier, services are free below a certain level of usage.
For more information about AWS costs and the Free Tier, see
`Test-Driving AWS in the Free Usage Tier <http://docs.aws.amazon.com/FeaturedArticles/latest/TestDriveFreeTier.html>`_.
To obtain an AWS account, open the `AWS home page <https://portal.aws.amazon.com/gp/aws/developer/registration/index.html>`_ and follow the instructions on the page.
