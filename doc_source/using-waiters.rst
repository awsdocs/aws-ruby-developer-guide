.. Copyright 2010-2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

   This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0
   International License (the "License"). You may not use this file except in compliance with the
   License. A copy of the License is located at http://creativecommons.org/licenses/by-nc-sa/4.0/.

   This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
   either express or implied. See the License for the specific language governing permissions and
   limitations under the License.

.. _aws-ruby-sdk-waiters:

#############
Using Waiters
#############

.. meta::
    :description:
        Use waiters with the AWS SDK for Ruby to poll for specific states to occur on clients.
    :keywords: AWS SDK for Ruby

Waiters are utility methods that poll for a particular state to occur on a client. Waiters can fail
after a number of attempts at a polling interval defined for the service client. For an example of
how a waiter is used, see :ref:`aws-ruby-sdk-dynamo-example-create-table`.

.. _aws-ruby-sdk-waiter-invoking:

Invoking a Waiter
=================

To invoke a waiter, call :code:`#wait_until` on a service client. In the following example, a waiter
waits until the instance :code:`i-12345678` is running before continuing.

.. code-block:: ruby

    ec2 = Aws::EC2::Client.new

    begin
      ec2.wait_until(:instance_running, instance_ids:['i-12345678'])
      puts "instance running"
    rescue Aws::Waiters::Errors::WaiterFailed => error
      puts "failed waiting for instance running: #{error.message}"
    end

The first parameter is the waiter name, which is specific to the service client and indicates which
operation is being waited for. The second parameter is a hash of parameters that are passed to the
client method called by the waiter, which varies according to the waiter name.

For a list of operations that can be waited for and the client methods called for each operation,
see the :code:`#waiter_names` and :code:`#wait_until` field documentation for the client you are
using.

.. _aws-ruby-sdk-wait-failures:

Wait Failures
=============

Waiters can fail with any of the following exceptions.

:sdk-ruby-api:`Aws::Waiters::Errors::FailureStateError </Aws/Waiters/Errors/FailureStateError>`
    A failure state was encountered while waiting.

:sdk-ruby-api:`Aws::Waiters::Errors::NoSuchWaiterError </Aws/Waiters/Errors/NoSuchWaiterError>`
    The specified waiter name is not defined for the client being used.

:sdk-ruby-api:`Aws::Waiters::Errors::TooManyAttemptsError </Aws/Waiters/Errors/TooManyAttemptsError>`
    The number of attempts exceeded the waiter's :code:`max_attempts` value.

:sdk-ruby-api:`Aws::Waiters::Errors::UnexpectedError </Aws/Waiters/Errors/UnexpectedError>`
    An unexpected error occurred while waiting.

:sdk-ruby-api:`Aws::Waiters::Errors::WaiterFailed </Aws/Waiters/Errors/WaiterFailed>`
    One of the wait states was exceeded or another failure occurred while waiting.

All of these errors |mdash| except :code:`NoSuchWaiterError` |mdash| are based on
:code:`WaiterFailed`. To catch errors in a waiter, use :code:`WaiterFailed`, as shown in the
following example.

.. code-block:: ruby

    rescue Aws::Waiters::Errors::WaiterFailed => error
      puts "failed waiting for instance running: #{error.message}"
    end

.. _aws-ruby-sdk-configuring-waiters:

Configuring a Waiter
====================

Each waiter has a default polling interval and a maximum number of attempts it will make before
returning control to your program. To set these values, use the :code:`max_attempts` and
:code:`delay:` parameters in your :code:`#wait_until` call. The following example waits for up to 25
seconds, polling every five seconds.

.. code-block:: ruby

    # Poll for ~25 seconds
    client.wait_until(...) do |w|
      w.max_attempts = 5
      w.delay = 5
    end

To disable wait failures, set the value of either of these parameters to :code:`nil`.

.. _aws-ruby-sdk-extending-waiters:

Extending a Waiter
==================

To modify the behavior of waiters, you can register callbacks that are triggered before each polling
attempt and before waiting.

The following example implements an exponential backoff in a waiter by doubling the
amount of time to wait on every attempt.

.. code-block:: ruby

    ec2 = Aws::EC2::Client.new

    ec2.wait_until(:instance_running, instance_ids:['i-12345678']) do |w|
      w.interval = 0 # disable normal sleep
      w.before_wait do |n, resp|
        sleep(n ** 2)
      end
    end

The following example disables the maximum number of attempts, and instead waits for one hour (3600
seconds) before failing.

.. code-block:: ruby

    started_at = Time.now
    client.wait_until(...) do |w|
      # Disable max attempts
      w.max_attempts = nil

      # Poll for one hour, instead of a number of attempts
      w.before_wait do |attempts, response|
        throw :failure if Time.now - started_at > 3600
      end
    end
