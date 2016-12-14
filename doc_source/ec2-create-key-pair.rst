.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-create-key-pair:

Creating a Key Pair
===================

You need a key pair when you connect to your |EC2| instance. The following example creates an unencrypted, PEM-encoded RSA private key :file:`MyGroovyKeyPair.pem` in your home folder.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-create-key-pair.rb
   :lines: 13-22
   :dedent: 0
   :language: ruby