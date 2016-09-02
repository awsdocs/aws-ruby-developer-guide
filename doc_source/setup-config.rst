.. Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-configuration:

##########################
Configuring the |sdk-ruby|
##########################

This section describes how to configure the |sdk-ruby|. To use the SDK, you must set the AWS region
and either set AWS credentials or create an |STS| access token.

.. _aws-ruby-sdk-setting-credentials:

Setting AWS Credentials
=======================

Before you can use the |sdk-ruby| to make a call to an AWS service, you must set the AWS access
credentials that will be used by the |sdk-ruby| to verify your access to AWS services and resources.
You can set credentials in a number of ways.

The |sdk-ruby| searches for credentials in the following order.

* :ref:`aws-ruby-sdk-credentials-client`

* :ref:`aws-ruby-sdk-credentials-aws-config`

* :ref:`aws-ruby-sdk-credentials-environment`

* :ref:`aws-ruby-sdk-credentials-shared`

* :ref:`aws-ruby-sdk-credentials-iam`

The following sections describe how to set credentials, starting with the most flexible approach.
For more information about AWS credentials and recommended approaches for credential management, see
`AWS Security Credentials
<http://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`_ in the AWS General
Reference.

.. _aws-ruby-sdk-credentials-shared:

Setting Shared Credentials
--------------------------

Set shared credentials in the AWS credentials profile file on your local system.

On Unix-based systems, such as Linux or OS X, this file is located in the following location:

.. code-block:: none

    ~/.aws/credentials

On Windows, this file is located in the following location:

.. code-block:: none

    %HOMEPATH%\.aws\credentials

This file must have the following format, where :code:`default` is the name of the default
configuration profile given to these credentials, *your_access_key_id* is the value of your access
key, and *your_secret_access_key* is the value of your secret access key.

.. code-block:: none

    [default]
    aws_access_key_id = your_access_key_id
    aws_secret_access_key = your_secret_access_key

.. _aws-ruby-sdk-credentials-environment:

Setting Credentials Using Environment Variables
-----------------------------------------------

Set the :code:`AWS_ACCESS_KEY_ID` and :code:`AWS_SECRET_ACCESS_KEY` environment variables.

Use the :code:`export` command to set these variables on a Unix-based systems, such as Linux or OS
X. The following example sets the value of your access key to *your_access_key_id* and the value of
your secret access key to *your_secret_access_key*.

.. code-block:: none

    export AWS_ACCESS_KEY_ID=your_access_key_id
    export AWS_SECRET_ACCESS_KEY=your_secret_access_key

To set these variables on Windows, use the :code:`set` command, as shown in the following example.

.. code-block:: none

    set AWS_ACCESS_KEY_ID=your_access_key_id
    set AWS_SECRET_ACCESS_KEY=your_secret_access_key

.. _aws-ruby-sdk-credentials-aws-config:

Setting Credentials Using Aws.config
------------------------------------

Set the credentials in your code by updating the values in the :code:`Aws.config` hash.

The following example sets the value of your access key to *your_access_key_id* and the value of
your secret access key to *your_secret_access_key*. Any client or resource you create subsequently
will use these credentials.

.. code-block:: ruby

    Aws.config.update({
       credentials: Aws::Credentials.new('your_access_key_id', 'your_secret_access_key')
    })

.. _aws-ruby-sdk-credentials-client:

Setting Credentials in a Client Object
--------------------------------------

Set the credentials in your code by specifying them when you create an AWS client.

The following example creates an S3 client using the access key *your_access_key_id* and the secret
access key *your_secret_access_key*.

.. code-block:: ruby

    s3 = Aws::S3::Client.new(
      access_key_id: 'your_access_key_id',
      secret_access_key: 'your_secret_access_key'
    )

.. _aws-ruby-sdk-credentials-iam:

Setting Credentials Using IAM
-----------------------------

For an |EC2| instance, create an |IAM| role, and then give your |EC2| instance access to that role.
For more information, see
`IAM Roles for Amazon EC2 <http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html>`_
in the |EC2| User Guide.

.. _aws-ruby-sdk-credentials-access-token:

Creating an |STS| Access Token
==============================

Use the
`Aws::AssumeRoleCredentials <http://docs.aws.amazon.com/sdkforruby/api/Aws/AssumeRoleCredentials.html>`_
method to create an |STS| access token.

The following example uses an access token to create an S3 client object, where
*linked::account::arn* is the Amazon Resource Name (ARN) of the role to assume and *session-name* is
an identifier for the assumed role session.

.. code-block:: ruby

    role_credentials = Aws::AssumeRoleCredentials.new(
      client: Aws::STS::Client.new,
      role_arn: "linked::account::arn",
      role_session_name: "session-name"
    )
    
    s3 = Aws::S3::Client.new(credentials: role_credentials)

.. _aws-ruby-sdk-setting-region:

Setting a Region
================

You need to set a `region <http://docs.aws.amazon.com/general/latest/gr/rande.html>`_ when using
most AWS services. The AWS region can be set in ways similar to setting your AWS credentials. The
|sdk-ruby| searches for a region in the following order.

* :ref:`aws-ruby-sdk-region-client-resource`

* :ref:`aws-ruby-sdk-region-aws-config`

* :ref:`aws-ruby-sdk-region-environment`

The rest of this section describes how to set a region, starting with the most flexible approach.

.. _aws-ruby-sdk-region-environment:

Setting the Region Using Environment Variables
----------------------------------------------

Set the region by setting the :code:`AWS_REGION` environment variable.

Use the :code:`export` command to set this variable on Unix-based systems, such as Linux or OS X.
The following example sets the region to :code:`us-west-2`:

.. code-block:: none

    export AWS_REGION=us-west-2

To set this variable on Windows, use the :code:`set` command. The following example sets the region
to :code:`us-west-2`:

.. code-block:: none

    set AWS_REGION=us-west-2

.. _aws-ruby-sdk-region-aws-config:

Setting the Region Using Aws.config
-----------------------------------

Set the region by adding a :code:`region` value to the :code:`Aws.config` hash. The following
example updates the :code:`Aws.config` hash to use the :code:`us-west-1` region:

.. code-block:: ruby

    Aws.config.update({region: 'us-west-1'})

Any clients or resources you subsequently create are bound to this region.

.. _aws-ruby-sdk-region-client-resource:

Setting the Region in a Client or Resource Object
-------------------------------------------------

Set the region when you create an AWS client or resource. The following example creates an S3
resource object in the :code:`us-west-1` region:

.. code-block:: ruby

    s3 = Aws::S3::Resource.new(region: 'us-west-1')

.. _aws-ruby-sdk-setting-non-standard-endpoint:

Setting a Non-Standard Endpoint
===============================

If you need to use a non-standard endpoint in the region you've selected, add an :code:`endpoint`
entry to :code:`Aws.config` or set the :code:`endpoint:` when creating a service client or resource
object. The following example creates an S3 resource object in the *other_endpoint* endpoint:

.. code-block:: ruby

    s3 = Aws::S3::Resource.new(endpoint: other_endpoint)
