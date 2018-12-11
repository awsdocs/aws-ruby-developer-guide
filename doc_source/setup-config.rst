.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-setup-config:

##########################
Configuring the |sdk-ruby|
##########################

.. meta::
    :description:
        Build Ruby applications on top of APIs that use the cost-effective, scalable, and reliable
        AWS infrastructure services with the |sdk-ruby|.
    :keywords: AWS SDK for ruby, aws.rb, aws-sdk-core gem, ruby code examples

Learn how to configure the |sdk-ruby|. To use the SDK, you must set either
AWS credentials or create an AWS STS access token, and set the AWS Region you want
to use.

.. _aws-ruby-sdk-getting-credentials:

Get your AWS access keys
========================

.. include:: common/procedure-get-access-keys.txt

.. _aws-ruby-sdk-setting-credentials:

Setting AWS Credentials
=======================

Before you can use the |sdk-ruby| to make a call to an AWS service, you must set the AWS access
credentials that the SDK will use to verify your access to AWS services and resources.

The |sdk-ruby| searches for credentials in the following order:

1. :ref:`aws-ruby-sdk-credentials-environment`
2. :ref:`aws-ruby-sdk-credentials-shared`
3. :ref:`aws-ruby-sdk-credentials-iam`

You can override these settings in your code. The precedence is:

1. :ref:`aws-ruby-sdk-credentials-aws-config`
2. :ref:`aws-ruby-sdk-credentials-client`

The following sections describe the various ways you can set credentials, starting with
the most flexible approach. For more information about AWS credentials and recommended approaches
for credential management, see `AWS Security Credentials
<http://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html>`_ in the |AWS-gr|.

Note that the shared configuration is loaded only a single time,
and credentials are provided statically at client creation time.
Shared credentials do not refresh.

.. _aws-ruby-sdk-credentials-shared:

Setting Shared Credentials
--------------------------

Set shared credentials in the AWS credentials profile file on your local system.

On Unix-based systems, such as Linux or OS X, this file is located in the following location.

.. code-block:: none

    ~/.aws/credentials

On Windows, this file is located in the following location.

.. code-block:: none

    %HOMEPATH%\.aws\credentials

This file must have the following format, where :code:`default` is the name of the default
configuration profile given to these credentials, :code:`your_access_key_id` is the value of your access
key, and :code:`your_secret_access_key` is the value of your secret access key.

.. code-block:: none

    [default]
    aws_access_key_id = your_access_key_id
    aws_secret_access_key = your_secret_access_key

.. _aws-ruby-sdk-credentials-environment:

Setting Credentials Using Environment Variables
-----------------------------------------------

Set the :code:`AWS_ACCESS_KEY_ID` and :code:`AWS_SECRET_ACCESS_KEY` environment variables.

Use the :code:`export` command to set these variables on Unix-based systems, such as Linux or OS
X. The following example sets the value of your access key to :code:`your_access_key_id` and the value of
your secret access key to :code:`your_secret_access_key`.

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

The following example sets the value of your access key to :code:`your_access_key_id` and the value of
your secret access key to :code:`your_secret_access_key`. Any client or resource you create subsequently
will use these credentials.

.. code-block:: ruby

    Aws.config.update({
       credentials: Aws::Credentials.new('your_access_key_id', 'your_secret_access_key')
    })

.. _aws-ruby-sdk-credentials-move:

Changing your Credentials Location
----------------------------------

You can also use **Aws.config** to store your credentials in a non-standard location.

The following example updates your configuration to store your credentials
at *my-path*.

.. code-block:: ruby

    shared_creds = Aws::SharedCredentials.new(path: 'my_path')
    Aws.config.update(credentials: shared_creds)

.. _aws-ruby-sdk-credentials-client:

Setting Credentials in a Client Object
--------------------------------------

Set the credentials in your code by specifying them when you create an AWS client.

The following example creates an |S3| client using the access key :code:`your_access_key_id` and the
secret access key :code:`your_secret_access_key`.

.. code-block:: ruby

    s3 = Aws::S3::Client.new(
      access_key_id: 'your_access_key_id',
      secret_access_key: 'your_secret_access_key'
    )

.. _aws-ruby-sdk-credentials-iam:

Setting Credentials Using IAM
-----------------------------

For an |EC2long| instance, create an |IAMlong| role, and then give your |EC2| instance access to that
role. For more information, see :ec2-ug:`IAM Roles for Amazon EC2 <iam-roles-for-amazon-ec2>` in the
|EC2-ug| or :ec2-ug-win:`IAM Roles for Amazon EC2 <iam-roles-for-amazon-ec2>` in the |EC2-ug-win|.

.. _aws-ruby-sdk-credentials-access-token:

Creating an |STS| Access Token
==============================

Use the
`Aws::AssumeRoleCredentials <http://docs.aws.amazon.com/sdkforruby/api/Aws/AssumeRoleCredentials.html>`_
method to create an |STSlong| (|STS|) access token.

The following example uses an access token to create an |S3| client object, where
:code:`linked::account::arn` is the Amazon Resource Name (ARN) of the role to assume and
:code:`session-name` is an identifier for the assumed role session.

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

You need to set a :aws-gr:`region <rande>` when using most AWS services. You can set the AWS Region
in ways similar to setting your AWS credentials. The |sdk-ruby| searches for a region in the
following order:

* :ref:`aws-ruby-sdk-region-client-resource`

* :ref:`aws-ruby-sdk-region-aws-config`

* :ref:`aws-ruby-sdk-region-environment`

The rest of this section describes how to set a region, starting with the most flexible approach.

.. _aws-ruby-sdk-region-environment:

Setting the Region Using Environment Variables
----------------------------------------------

Set the region by setting the :code:`AWS_REGION` environment variable.

Use the :code:`export` command to set this variable on Unix-based systems, such as Linux or OS X.
The following example sets the region to :code:`us-west-2`.

.. code-block:: none

    export AWS_REGION=us-west-2

To set this variable on Windows, use the :code:`set` command. The following example sets the region
to :code:`us-west-2`.

.. code-block:: none

    set AWS_REGION=us-west-2

.. _aws-ruby-sdk-region-aws-config:

Setting the Region Using Aws.config
-----------------------------------

Set the region by adding a :code:`region` value to the :code:`Aws.config` hash. The following
example updates the :code:`Aws.config` hash to use the :code:`us-west-1` region.

.. code-block:: ruby

    Aws.config.update({region: 'us-west-1'})

Any clients or resources you subsequently create are bound to this region.

.. _aws-ruby-sdk-region-client-resource:

Setting the Region in a Client or Resource Object
-------------------------------------------------

Set the region when you create an AWS client or resource. The following example creates an |S3|
resource object in the :code:`us-west-1` region.

.. code-block:: ruby

    s3 = Aws::S3::Resource.new(region: 'us-west-1')

.. _aws-ruby-sdk-setting-non-standard-endpoint:

Setting a Nonstandard Endpoint
===============================

If you need to use a nonstandard endpoint in the region you've selected, add an :code:`endpoint`
entry to :code:`Aws.config` or set the :code:`endpoint:` when creating a service client or resource
object. The following example creates an |S3| resource object in the :code:`other_endpoint` endpoint.

.. code-block:: ruby

    s3 = Aws::S3::Resource.new(endpoint: other_endpoint)

.. Just for this CSM section

.. |language| replace:: Ruby 
.. |sdk| replace:: |sdk-ruby|
.. |CSM| replace:: SDK Metrics
.. |CSMlong| replace:: AWS SDK Metrics for Enterprise Support
.. |CSMmerge| replace:: AWS SDK Metrics for Enterprise Support (SDK Metrics)
.. |CreatePolicy| replace:: :ruby-sdk-api:`create_policy <Aws/IAM/Client.html#create_policy-instance_method>`
.. |CreateRole| replace:: :ruby-sdk-api:`create_role <Aws/IAM/Client.html#create_role-instance_method>`
.. |AttachRolePolicy| replace:: :ruby-sdk-api:`attach_role_policy <Aws/IAM/Client.html#attach_role_policy-instance_method>`

.. _csm_metrics:

Using |CSM| in the |sdk|
========================

.. meta::
   :description: Configure an agent for AWS SDK Metrics for Enterprise Support with the |sdk|.
   :keywords: |sdk|, AWS SDK Metrics for Enterprise Support with |language|, use |language| to monitor AWS Services

|CSMmerge| enables Enterprise customers to monitor their AWS service use.
|CSM| can help to identify the health of their AWS services
and diagnose latency caused by reaching their account usage limits or a service outage.

|CSM| for AWS SDKs delivers telemetry from within the AWS SDKs that makes it possible for AWS to know
when applications experience connection issues to AWS endpoints, and gain insight into why the issues occur.
Telemetry helps AWS reduce the time to resolve problems that impact your application's access to AWS services.

|CSM| monitors actions by using a |CWlong| agent running in the same environment as a client application
that is using the |sdk|.
The following steps to set up |CSM| focus on an |EC2| Linux instance.
|CSM| is also available for your production environments if you enable it while configuring the |sdk|. 

To utilize |CSM|, run the most current version of the |CW| agent.
Learn how to :CW-dg:`Configure the CloudWatch Agent for SDK Metrics<Configure-CloudWatch-Agent-SDK-Metrics.>` in the |CW-dg|.

To set up |CSM| with the |sdk|, follow these instructions:

1. Create an application with an |sdk| client to use an AWS service.
2. Host your project on an |EC2| instance or in your local environment.
3. Install and use the most current version of the |sdk|.
4. Install and configure an |CW| agent on an EC2 instance or in your local environment.
5. :ref:`csm-set-permissions`
6. :ref:`csm-enable-agent`
7. :ref:`csm-view-metrics`

For more information, see the following:

* :ref:`csm-update-agent`
* :ref:`csm-disable-agent`

.. _csm-set-permissions:

Configure |CSM| to Collect and Send Metrics
-------------------------------------------

You can configure |CSM| so that it collects and sends metrics by using the
|sdk| or the |IAM| console,
as explained in the following sections.

.. _csm_setup_sdk:

Set Up Access Permissions Using the |sdk|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create an IAM role for the instance that has permission for |SSMlong| and |CSM|.

First create a policy using |CreatePolicy|.
Then create a role using |CreateRole|.
Finally, attach the policy you created to your new role with |AttachRolePolicy|.

.. literalinclude:: example_code/iam/iam_ruby_example_create_csm_role.rb
   :language: ruby
   :start-after: snippet-start:[iam.ruby.create_csm_role]
   :end-before: snippet-end:[iam.ruby.create_csm_role]

.. _csm_setup_console:
                
Set Up Access Permissions Using the |IAM| Console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can also use the IAM console to create a role.

.. topic:: To create a role using the IAM console

1. Go to the `IAM console <https://console.aws.amazon.com/iam>`_, and create a role to use |EC2|.
2. In the navigation pane, choose **Roles**.
3. Choose **Create Role**.
4. Choose **AWS Service**, and then choose **EC2**.
5. Choose **Next: Permissions**.
6. Under **Attach permissions policies**, choose **create policy**.
7. For :guilabel:`Service`, choose **SSM**. For :guilabel:`Actions`, choose :code:`GetParameter`.
   For resources, specify the |CW| agent created in the previous section.
8. Add an additional permission.
9. Select **Choose a service**, and then **Enter service manually**.
   For :guilabel:`Service`, enter :code:`sdkmetrics`.
   Select all :code:`sdkmetrics` actions and all resources, and then choose **Review Policy**.
10. Name the :guilabel:`Role` :code:`AmazonCSM`, and add a description.
11. Choose **Create Role**.

.. _csm-enable-agent:

Enabling |CSM| for the |sdk|
----------------------------

|CSM| has the following default parameters.

.. code-block:: ini

    //default values
     [
         'enabled' => false,
         'port' => 31000,
         'client_id' => ''
     ]

You can enable |CSM| by setting an environment variable or by setting a value in the AWS Shared config file,
as explained in the following sections.

.. _enable_csm_env_var:

Enable |CSM| Using an Environment Variable
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To enable |CSM|, set the `AWS_CSM_ENABLED` environmental variable.

.. code-block:: ini

    AWS_CSM_ENABLED=true

Other configuration settings are available.
For more information about using shared files, see
:doc:`Shared Credentials File <shared_credentials_file>`.

Note: Enabling |CSM| does not configure your credentials to use an AWS service. 
To do that, see
:doc:`Specifying Credentials<specifying-credentials>`.

.. _enable_csm_config_file:

AWS Shared Config File
~~~~~~~~~~~~~~~~~~~~~~

If no CSM configuration is found in the environment variables, the SDK looks for your customized AWS profile field.
Then it checks the :code:`aws_csm` profile.
To enable |CSM|,
add :code:`csm_enabled` to the shared config file `~/.aws/config`.

.. code-block:: ini

    [custom_profile_from_aws_profile]
    csm_enabled = true

    [aws_csm]
    csm_enabled = true

Other configuration settings are available.
For more information about using AWS Shared files, see
:doc:`Specifying Credentials <specifying_credentials>`.

Note: Enabling |CSM| does not configure your credentials to use an AWS service.

.. _csm-view-metrics:

Viewing Metrics in |CW|
-----------------------

For Enterprise users, the agent automatically captures data about each client operation and passes the information to |CW|.

.. topic:: To access your metrics

1. Go to the `CloudWatch console <http://console.aws.amazon.com/cloudwatch>`_.
2. In the navigation pane, choose :guilabel:`Metrics`.
3. Choose :guilabel:`SDKMetrics`.
4. View the metrics.

.. You can use the |sdk| to get the monitored API call and call attempt events for an operation,
   as shown in the following example,
   which gets the events for *MyObject* in the |S3| bucket *MyBucket*.

   code-block:: ruby

   ???

.. _csm-update-agent:

Updating a |CW| Agent
---------------------

To change the port or client ID,
set the values and then restart any AWS jobs that are currently active.
You can set the values by using environment variables or in the shared configuration file,
as explained in the following sections.

.. _csm-update-agent-env-var:

Setting |CSM| Values Using Environment Variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|CSM| assigns a client ID to your application environment that is a
searchable index point in the |CW| dashboard.
To add a customized client ID string, add
`AWS_CSM_CLIENT_ID=[some_string]` to the host's environment variables.

Most services use the default port.
But if your service requires a unique port ID,
add `AWS_CSM_PORT=[port_number]`, to the host's environment variables.

.. code-block:: ini

    AWS_CSM_ENABLED=true
    AWS_CSM_CLIENT_ID=myAppName
    AWS_CSM_PORT=1234

.. _csm-update-agent-env-var:

Setting |CSM| Values Using the AWS Shared Config File
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|CSM| assigns a client ID to your application environment that is a
searchable index point in the |CW| dashboard.  To add a customized client ID string, add
`csm_client_id = [some_string]` to `~/.aws/config`.

Most services use the default port.
If your service requires a unique port ID,
add `csm_port = [port_number]` to `~/.aws/config`.

.. code-block:: ini

    [custom_profile_from_aws_profile]
    csm_enabled = false
    csm_client_id = myAppName
    csm_port = 1234

    [aws_csm]
    csm_enabled = false
    csm_client_id = myAppName
    csm_port = 1234

.. _restart_csm:
    
Restarting |CSM|
----------------

To restart |CSM|, stop and start the agent:

.. code-block:: ini

    amazon-cloudwatch-agent-ctl -a stop
    amazon-cloudwatch-agent-ctl -a start

.. _csm-disable-agent:

Disabling |CSM|
---------------

To disable |CSM|, set the `AWS_CSM_ENABLED` environment variable to `false`,
or set the `csm_enabled` value to `false` your AWS Shared config file `~/.aws/config`.
Then restart your |CW| agent so that the changes can take effect.

**Environment Variable**

.. code-block:: ini

    AWS_CSM_ENABLED=false

**AWS Shared Config File**

.. note:: Environment variables override the AWS Shared config file. If |CSM| is enabled in the environment variables, the |CSM| remains enabled.

.. code-block:: ini

    [custom_profile_from_aws_profile]
    csm_enabled = false

    [aws_csm]
    csm_enabled = false

To stop |CSM|, use the following command.

.. code-block:: ini

    amazon-cloudwatch-agent-ctl -a stop
