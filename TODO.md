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


Stale Lockfiles
---------------

Handle stale lockfiles better than this:

    # python /home/jjneely/nagiosreload.py
    Traceback (most recent call last):
      File "/home/jjneely/nagiosreload.py", line 116, in <module>
        with CronScript():
      File "/usr/lib/python2.7/dist-packages/pycronscript/__init__.py", line 132, in __enter__
        self.lock.acquire(timeout=self.options.locktimeout)
      File "/usr/lib/python2.7/dist-packages/lockfile.py", line 261, in acquire
        raise LockTimeout
    lockfile.LockTimeout

