.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-eb-recipes:

#################
|AEBlong| Recipes
#################

You can use the following recipes to access |AEBlong| (|AEB|) using the |sdk-ruby|. For more
information about |AEB|, see the `Elastic Beanstalk Developer Guide <http://docs.aws.amazon.com/elasticbeanstalk/latest/dg>`_.

**Recipes**

* :ref:`aws-ruby-sdk-eb-recipe-get-apps`

* :ref:`aws-ruby-sdk-eb-recipe-get-app`

* :ref:`aws-ruby-sdk-eb-recipe-update-ruby-on-rails-app`

.. _aws-ruby-sdk-eb-recipe-get-apps:

Getting Information about All Applications
==========================================

The following example lists the names, descriptions, and URLs of all of your |AEB| applications in the :code-ruby:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/elb/elb-ruby-example-list-all-apps.rb
   :lines: 13-26
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-eb-recipe-get-app:

Getting Information about a Specific Application
================================================

The following example lists the name, description, and URL of the :code:`MyRailsApp` application in the :code-ruby:`us-west-2` region.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/elb/elb-ruby-example-list-name-description-url-myrailsapp.rb
   :lines: 13-25
   :dedent: 0
   :language: ruby

.. _aws-ruby-sdk-eb-recipe-update-ruby-on-rails-app:

Updating a Ruby on Rails Application
====================================

The following example updates the Ruby on Rails application :code:`MyRailsApp` in the :code-ruby:`us-west-2` region.

.. note:: You must be in the root of your Rails app to succesfully run the script.

.. literalinclude:: ../build_dependencies/1/ruby/example_code/elb/elb-ruby-example-update-myrailsapp.rb
   :lines: 13-79
   :dedent: 0
   :language: ruby
