.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-setup-install:

#########################
Installing the |sdk-ruby|
#########################

.. meta::
    :description: Learn how to install the AWS SDK for Ruby.
    :keywords: AWS SDK for Ruby installation, aws.rb, aws-sdk-core gem, AWS SDK for Ruby code examples

This section includes prerequisites and installation instructions for the |sdk-ruby|.

.. _aws-ruby-sdk-prerequisites:

Prerequisites
=============

Before you install the |sdk-ruby|, you need an AWS account and Ruby version 1.9 or later.

If you don't have an AWS account, use the following procedure to create one.

1. Open http://aws.amazon.com/ and choose **Create an AWS Account**.

2. Follow the online instructions.

Installing the SDK
==================

If your project uses `Bundler <http://bundler.io/>`_, add the following line to your :code:`Gemfile`
to add the |sdk-ruby| to your project.

.. code-block:: none

    gem 'aws-sdk'

If you don't use Bundler, the easiest way to install the SDK is to use `RubyGems
<https://rubygems.org/gems/aws-sdk/>`_. To install the latest version of the SDK, use the following
command.

.. code-block:: none

    gem install aws-sdk

If the previous command fails on your Unix-based system, use :code:`sudo` to install the SDK, as
shown in the following command.

.. code-block:: none

    sudo gem install aws-sdk
