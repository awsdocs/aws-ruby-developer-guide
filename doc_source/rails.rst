.. Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ruby-on-rails:

################################
Using the SDK with Ruby on Rails
################################

`Ruby on Rails <http://rubyonrails.org/>`_ provides a web development framework for Ruby that makes
it easy to create websites with Ruby.

The |sdk-ruby| provides a gem to enable easy integration with Rails. You can use |AEBlong|, |OPSlong|,
or |ACDlong| to deploy and run your Rails applications in the AWS Cloud.

.. _aws-ruby-sdk-integrating-the-sdk-ruby-with-rails:

Integrating the |sdk-ruby| with Rails
=====================================

AWS provides a gemfile, :code:`aws-sdk-rails`, that supports integration of the |sdk-ruby| with
Rails. You can view its GitHub repository at https://github.com/aws/aws-sdk-rails.

Add the gem to your application's Gemfile, as shown in the following example.

.. code-block:: none

    gem 'aws-sdk-rails'

The gem includes the |sdk-ruby|, so adding the gem is all you need to do to add AWS support to your
Rails application.

.. _aws-ruby-sdk-ses-support-for-actionmailer:

|SES| Support for ActionMailer
==============================

When you use the :code:`aws-sdk-rails` gem in a :code:`config/environments` file of your Rails
project (for example, :file:`config/environments/production.rb`), you can use |SESlong| (|SES|) as
the back end for the :code:`ActionMailer` class, as shown in the following example.

.. code-block:: none

    config.action_mailer.delivery_method = :aws_sdk

For more information about :code:`ActionMailer`, see the `Action Mailer Basics
<http://guides.rubyonrails.org/action_mailer_basics.html>`_ on the Ruby on Rails website.

.. _aws-ruby-sdk-logging:

Logging
=======

The :code:`aws-sdk-rails` gem configures the SDK logger to use :code:`Rails.logger`.

The gem also configures the SDK log messages to use the :code:`:info` log level. You can change the
log level by setting :code:`:log_level` in the `Aws.config
<http://docs.aws.amazon.com/sdkforruby/api/Aws.html#config-class_method>`_ hash. The following
example sets the log level to :code:`:debug`.

.. code-block:: ruby

    Aws.config.update({log_level: :debug})
