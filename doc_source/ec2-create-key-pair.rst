.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-ec2-create-key-pair:

###############################
Working with Key Pairs in |EC2|
###############################

.. meta::
    :description:
        Learn to work with key pairs in Amazon EC2 using this AWS SDK for Ruby code example.
    :keywords: AWS SDK for Ruby code examples, Amazon EC2

The following examples show you how to use the |sdk-ruby| with |EC2| to:

* Create a key pair.
* Get information about key pairs.
* Delete a key pair.

For more information about key pairs, see :EC2-ug:`Amazon EC2 Key Pairs <ec2-key-pairs>` in the |EC2-ug| or
:EC2-ug-win:`Amazon EC2 Key Pairs and Windows Instances <ec2-key-pairs>` in the |EC2-ug-win|.

For additional code that you can use to run these examples, see :ref:`aws-ruby-sdk-ec2-create-key-pair-code`.

.. _aws-ruby-sdk-ec2-create-key-pair-create:

Create a Key Pair
=================

Call the :ruby-sdk-api:`create_key_pair <Aws/EC2/Client.html#create_key_pair-instance_method>` method, specifying the name of the key pair to create.

.. code-block:: Ruby

 key_pair = ec2.create_key_pair({
   key_name: key_pair_name
 })

In this code:

* :code:`ec2` is a variable representing an :ruby-sdk-api:`Aws::EC2::Client <Aws/EC2/Client.html>` object.
* :code:`key_pair_name` is a string variable representing the name of the key pair.
* :code:`key_pair` is a variable representing an :ruby-sdk-api:`Aws::EC2::KeyPair <Aws/EC2/KeyPair.html>` object that is
  returned by calling the :code:`create_key_pair` method.

For more information, see :ref:`aws-ruby-sdk-ec2-create-key-pair-code`.

.. _aws-ruby-sdk-ec2-create-key-pair-info:

Get Information about Key Pairs
===============================

To get information about a single key pair, use attributes such as:

* :ruby-sdk-api:`key_name <Aws/EC2/KeyPair.html#key_name-instance_method>`, which gets the key pair's name.
* :ruby-sdk-api:`key_fingerprint <Aws/EC2/KeyPair.html#key_fingerprint-instance_method>`, which gets the SHA-1 digest of the DER
  encoded private key.
* :ruby-sdk-api:`key_material <Aws/EC2/KeyPair.html#key_material-instance_method>`, which gets the unencrypted PEM encoded RSA private key.

.. code-block:: Ruby

  puts "Created key pair '#{key_pair.key_name}'."
  puts "\nSHA-1 digest of the DER encoded private key:"
  puts "#{key_pair.key_fingerprint}"
  puts "\nUnencrypted PEM encoded RSA private key:"
  puts "#{key_pair.key_material}"

In this code, :code:`key_pair` is a variable representing an :ruby-sdk-api:`Aws::EC2::KeyPair <Aws/EC2/KeyPair.html>`
object. This is
returned by calling the :ruby-sdk-api:`create_key_pair <Aws/EC2/Client.html#create_key_pair-instance_method>` method in the previous example.

To get information about multiple key pairs, call the :ruby-sdk-api:`describe_key_pairs <Aws/EC2/Client.html#describe_key_pairs-instance_method>` method.

.. code-block:: Ruby

 key_pairs_result = ec2.describe_key_pairs()

 if key_pairs_result.key_pairs.count > 0
  puts "\nKey pair names:"
  key_pairs_result.key_pairs.each do |kp|
    puts kp.key_name
  end
 end
 
In this code:

* :code:`ec2` is a variable representing an :ruby-sdk-api:`Aws::EC2::Client <Aws/EC2/Client.html>` object.
* :code:`key_pair_result` is a variable representing an :ruby-sdk-api:`Aws::EC2::Types::DescribeKeyPairsResult <Aws/EC2/Types/DescribeKeyPairsResult.html>` object
  that is returned by calling the :code:`describe_key_pairs` method.
* Calling the :code:`Aws::EC2::Types::DescribeKeyPairsResult` object's :ruby-sdk-api:`key_pairs <Aws/EC2/Types/DescribeKeyPairsResult.html#key_pairs-instance_method>` method
  returns an array of :ruby-sdk-api:`Aws::EC2::Types::KeyPairInfo <Aws/EC2/Types/KeyPairInfo.html>` objects, which represent the key pairs.

For more information, see :ref:`aws-ruby-sdk-ec2-create-key-pair-code`.

.. _aws-ruby-sdk-ec2-create-key-pair-delete:

Delete a Key Pair
=================

Call the :ruby-sdk-api:`delete_key_pair <Aws/EC2/Client.html#delete_key_pair-instance_method>` method, specifying the name of the key pair to delete.

.. code-block:: Ruby

 ec2.delete_key_pair({
 key_name: key_pair_name
 })

In this code:

* :code:`ec2` is a variable representing an :ruby-sdk-api:`Aws::EC2::Client <Aws/EC2/Client.html>` object.
* :code:`key_pair_name` is a string variable representing the name of the key pair.

For more information, see :ref:`aws-ruby-sdk-ec2-create-key-pair-code`.

.. _aws-ruby-sdk-ec2-create-key-pair-code:

Complete Example
================

The following code, which you can adapt and run, combines the preceding examples into a single example.

.. literalinclude:: ./example_code/ec2/ec2-ruby-example-key-pairs.rb
   :dedent: 0
   :language: ruby

To run this code, you must:

#. Install the |sdk-ruby|. For more information, see :doc:`setup-install`.
#. Set the AWS access credentials that the |sdk-ruby| will use to verify your access to AWS services and resources. For more information, see :doc:`setup-config`.
   Be sure the AWS credentials map to an |IAMlong| (|IAM|) entity with access to the AWS actions and resources described in this example. This example assumes you
   have set the credentials in the AWS credentials profile file or in the :envvar:`AWS_ACCESS_KEY_ID` and :envvar:`AWS_SECRET_ACCESS_KEY` environment variables on your local system.
