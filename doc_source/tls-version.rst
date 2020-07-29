.. Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

###################################
Using TLS 1.2 in |SERVICENAMETITLE|
###################################

.. meta::
   :description: Learn how how to use TLS 1.2 or later to ensure the security of communication with |AWS| services.
   :keywords:

.. include:: common/_security-includes.txt

Communication between the |sdk-ruby| and |AWS| is secured using Secure Sockets Layer (SSL) or Transport Layer Security (TLS). 
All versions of SSL, and versions of TLS earlier than 1.2, have vulnerabilities that can compromise the security of your communication
with |AWS|. For this reason, you should make sure that you're using the |sdk-ruby| with a version of Ruby that supports TLS 
version 1.2 or later.

Ruby uses the OpenSSL library to secure HTTP connections. Supported versions of Ruby (1.9.3 and later) installed through
system `package managers`_  (``yum``, ``apt``, and others), an `official installer`_, or Ruby `managers`_ (rbenv, RVM, and others)
typically incorporate  OpenSSL 1.0.1 or later, which supports TLS 1.2.

.. _package managers: https://www.ruby-lang.org/en/documentation/installation/#package-management-systems
.. _official installer: https://www.ruby-lang.org/en/documentation/installation/#installers
.. _managers: https://www.ruby-lang.org/en/documentation/installation/#managers

When used with a supported version of Ruby with OpenSSL 1.0.1 or later, the |sdk-ruby| prefers TLS 1.2, and uses the latest version 
of SSL or TLS supported by both the client and server. This is always at least TLS 1.2 for AWS services.  (The SDK uses the Ruby 
``Net::HTTP`` class with ``use_ssl=true``.) 

Checking the OpenSSL version
============================

To make sure your installation of Ruby is using OpenSSL 1.0.1 or later, enter the following command.

.. code-block:: none

   ruby -r openssl -e 'puts OpenSSL::OPENSSL_VERSION'

An alternative way to get the OpenSSL version is to query the ``openssl`` executable directly.  First, locate the appropriate
executable using the following command.

.. code-block:: none

   ruby -r rbconfig -e 'puts RbConfig::CONFIG["configure_args"]'

The output should have ``--with-openssl-dir=/path/to/openssl`` indicating the location of the OpenSSL installation. Make a note of
this path.  To check the version of OpenSSL, enter the following commands.

.. code-block:: none

   cd /path/to/openssl
   bin/openssl version

This latter method might not work with all installations of Ruby.

Upgrading TLS support
=====================

If the version of OpenSSL used by your Ruby installation is earlier than 1.0.1, upgrade your Ruby or OpenSSL installation using your system package
manager, Ruby installer, or Ruby manager, as described in Ruby's `installation guide`_. If you're installing Ruby `from source`_, 
install the `latest OpenSSL`_ first, and then pass ``--with-openssl-dir=/path/to/upgraded/openssl`` when running ``./configure``.

.. _installation guide: https://www.ruby-lang.org/en/documentation/installation/
.. _from source: https://www.ruby-lang.org/en/documentation/installation/#building-from-source
.. _latest OpenSSL: https://www.openssl.org/source/
