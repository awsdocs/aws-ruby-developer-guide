.. Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _authorize_metrics:

########################################################
Authorize |CSM| to Collect and Send Metrics in the |sdk|
########################################################

To collect metrics from AWS SDKs using |CSM| for Enterprise Support,
Enterprise customers must create an |IAM| Role that gives |CW| agent permission
to gather data from their |EC2| instance or production environment.

Use the following |language| code sample or the AWS Console to create an
|IAM| Policy and Role for an |CW| agent to access |CSM| in your environment.

Learn more about using |CSM| with |sdk| in :doc:`setup-metrics`.

.. For more information about |CSM|, see |CW_IAM_CSM| in the *|CWlong| User Guide*.

.. _setup_access_permissions_sdk:

Set Up Access Permissions Using the |sdk|
=========================================

Create an |IAM| role for the instance that has permission for |EC2| Systems Manager and |CSM|.

First, create a policy using |CreatePolicy|.
Then create a role using |CreateRole|.
Finally, attach the policy you created to your new role with |AttachRolePolicy|.

.. replace with iam.ruby.create_csm_role once we release

.. code-block:: ruby
                
    require 'aws-sdk-iam' # v2: require 'aws-sdk'

    role_name = 'AmazonCSM'

    client = Aws::IAM::Client.new(region: 'us-west-2')

    csm_policy = {
        'Version': '2012-10-17',
        'Statement': [
            {
                'Effect': 'Allow',
                'Action': [
                    'sdkmetrics:*'
                ],
                'Resource': '*'
            },
            {
                'Effect': 'Allow',
                'Action': [
                    'ssm:GetParameter'
                ],
                'Resource': 'arn:aws:ssm:*:*:parameter/AmazonCSM*'
            }
        ]
    }

    # Create policy
    resp = client.create_policy({
                                    policy_name: role_name,
                                    policy_document: csm_policy.to_json,
                                })

    policy_arn = resp.policy.arn

    puts 'Created policy with ARN: ' + policy_arn

    policy_doc = {
        Version: '2012-10-17',
        Statement: [
            {
                Effect: 'Allow',
                Principal: {
                    Service: 'ec2.amazonaws.com'
                },
                Action: 'sts:AssumeRole'
            },]
    }

    # Create role
    client.create_role(
        {
            role_name: role_name,
            description: 'An instance role that has permission for AWS Systems Manager and SDK Metric Monitoring.',
            assume_role_policy_document: policy_doc.to_json,
        })

    puts 'Created role ' + role_name

    # Attach policy to role
    client.attach_role_policy(
        {
            policy_arn: policy_arn,
            role_name: role_name,
        })

    puts 'Attached policy ' + role_name + 'policy to role: ' + role_name

.. _setup_access_permissions_console:

Set Up Access Permissions by Using the |IAM| Console
====================================================

Alternatively, you can use the |IAM| console to create a role.

#. Go to the |IAM| console, and create a role to use |EC2|.

#. In the navigation pane, choose **Roles**.

#. Choose **Create Role**.

#. Choose **AWS Service**, and then **EC2**.

#. Choose **Next: Permissions**.

#. Under **Attach permissions policies**, choose **create policy**.

#. For **Service**, choose **Systems Manager**.
   For **Actions**, expand **Read**, and choose ``GetParameters``.
   For resources, specify your |CW| agent.

#. Add additional permission.

#. Select **Choose a service**, and then **Enter service manually**.
   For **Service**, enter ``sdkmetrics``.
   Select all ``sdkmetrics`` actions and all resources, and then choose **Review Policy**.

#. Name the **Role** ``AmazonSDKMetrics``, and add a description.

#. Choose **Create Role**.
