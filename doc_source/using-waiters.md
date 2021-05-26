# Using Waiters<a name="using-waiters"></a>

Waiters are utility methods that poll for a particular state to occur on a client\. Waiters can fail after a number of attempts at a polling interval defined for the service client\. For an example of how a waiter is used, see [Creating an Amazon DynamoDB Table](dynamo-example-create-table.md#aws-ruby-sdk-dynamo-example-create-table)\.

## Invoking a Waiter<a name="aws-ruby-sdk-waiter-invoking"></a>

To invoke a waiter, call `#wait_until` on a service client\. In the following example, a waiter waits until the instance `i-12345678` is running before continuing\.

```
ec2 = Aws::EC2::Client.new

begin
  ec2.wait_until(:instance_running, instance_ids:['i-12345678'])
  puts "instance running"
rescue Aws::Waiters::Errors::WaiterFailed => error
  puts "failed waiting for instance running: #{error.message}"
end
```

The first parameter is the waiter name, which is specific to the service client and indicates which operation is being waited for\. The second parameter is a hash of parameters that are passed to the client method called by the waiter, which varies according to the waiter name\.

For a list of operations that can be waited for and the client methods called for each operation, see the `#waiter_names` and `#wait_until` field documentation for the client you are using\.

## Wait Failures<a name="aws-ruby-sdk-wait-failures"></a>

Waiters can fail with any of the following exceptions\.

** [Aws::Waiters::Errors::FailureStateError](https://docs.aws.amazon.com/sdk-for-ruby/v3/api//Aws/Waiters/Errors/FailureStateError.html) **  
A failure state was encountered while waiting\.

** [Aws::Waiters::Errors::NoSuchWaiterError](https://docs.aws.amazon.com/sdk-for-ruby/v3/api//Aws/Waiters/Errors/NoSuchWaiterError.html) **  
The specified waiter name is not defined for the client being used\.

** [Aws::Waiters::Errors::TooManyAttemptsError](https://docs.aws.amazon.com/sdk-for-ruby/v3/api//Aws/Waiters/Errors/TooManyAttemptsError.html) **  
The number of attempts exceeded the waiter’s `max_attempts` value\.

** [Aws::Waiters::Errors::UnexpectedError](https://docs.aws.amazon.com/sdk-for-ruby/v3/api//Aws/Waiters/Errors/UnexpectedError.html) **  
An unexpected error occurred while waiting\.

** [Aws::Waiters::Errors::WaiterFailed](https://docs.aws.amazon.com/sdk-for-ruby/v3/api//Aws/Waiters/Errors/WaiterFailed.html) **  
One of the wait states was exceeded or another failure occurred while waiting\.

All of these errors—except `NoSuchWaiterError`—are based on `WaiterFailed`\. To catch errors in a waiter, use `WaiterFailed`, as shown in the following example\.

```
rescue Aws::Waiters::Errors::WaiterFailed => error
  puts "failed waiting for instance running: #{error.message}"
end
```

## Configuring a Waiter<a name="aws-ruby-sdk-configuring-waiters"></a>

Each waiter has a default polling interval and a maximum number of attempts it will make before returning control to your program\. To set these values, use the `max_attempts` and `delay:` parameters in your `#wait_until` call\. The following example waits for up to 25 seconds, polling every five seconds\.

```
# Poll for ~25 seconds
client.wait_until(...) do |w|
  w.max_attempts = 5
  w.delay = 5
end
```

To disable wait failures, set the value of either of these parameters to `nil`\.

## Extending a Waiter<a name="aws-ruby-sdk-extending-waiters"></a>

To modify the behavior of waiters, you can register callbacks that are triggered before each polling attempt and before waiting\.

The following example implements an exponential backoff in a waiter by doubling the amount of time to wait on every attempt\.

```
ec2 = Aws::EC2::Client.new

ec2.wait_until(:instance_running, instance_ids:['i-12345678']) do |w|
  w.interval = 0 # disable normal sleep
  w.before_wait do |n, resp|
    sleep(n ** 2)
  end
end
```

The following example disables the maximum number of attempts, and instead waits for one hour \(3600 seconds\) before failing\.

```
started_at = Time.now
client.wait_until(...) do |w|
  # Disable max attempts
  w.max_attempts = nil

  # Poll for one hour, instead of a number of attempts
  w.before_wait do |attempts, response|
    throw :failure if Time.now - started_at > 3600
  end
end
```