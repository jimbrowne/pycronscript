Mechanism for suppressing repeated failures
------------------------------------------

Could take the output, hash it, and cache the result.  Would allow
emitting an error once (or a few times), then emitting a reminder
every N occurrences.

Timeout for run time
--------------------

Set an alarm and throw an exception if timeout reached before
```__exit__``` is called.

Warnings when run time is running longer than expected
------------------------------------------------------

Possibly use an alarm to emit a logging message (or email) when time
is running longer than expected.

Possibly use an average of previous run times rather than a hard-coded
value.

Logging to logstash/redis
-------------------------

Add option for direct logging to logstash/redis

