.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-iam-example-server-certificates:

####################################
Working with IAM Server Certificates
####################################

.. meta::
    :description:
        Learn to work with IAM server certificates using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, IAM

To enable HTTPS connections to your website or application on AWS, you need an SSL/TLS server certificate. To use a certificate that you obtained from an external provider with your website or application on AWS, you must upload the certificate to |IAM| or import it into AWS Certificate Manager. For more information about server certificates, see :IAM-ug:`Working with Server Certificates <id_credentials_server-certs>`.

In this example, you use the |sdk-ruby| with |IAM| to:

#. Update a server certificate, using :aws-ruby-iam-client-method:`update_server_certificate`.
#. Delete the server certificate, using :aws-ruby-iam-client-method:`delete_server_certificate`.
#. List information about any remaining server certificates, using :aws-ruby-iam-client-method:`list_server_certificates`.

*************
Prerequisites
*************

Before running the example code, you need to install and configure the |sdk-ruby|, as described
in:

* :ref:`aws-ruby-sdk-setup-install`
* :ref:`aws-ruby-sdk-setup-config`

.. note:: The server certificate must already exist, or the script will throw
          an `Aws::IAM::Errors::NoSuchEntity` error.

*******
Example
*******

.. literalinclude:: ./example_code/iam/iam-ruby-example-server-certificates.rb
   :dedent: 0
   :language: ruby
