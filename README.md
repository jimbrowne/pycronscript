A python class encapsulating common functions for cron scripts
--------------------------------------------------------------

This python class handles features common to many cron scripts to avoid
repeating code in many scripts.

Here are the included options:

    Options:
      -d, --debug           Minimum log level of DEBUG
      -q, --quiet           Only WARN and above to stdout
      --syslog              Log to local syslog
      --nolog               Do not log to LOGFILE
      --logfile=LOGFILE     File to log to, default /var/log/PROGNAME.log
      --syslog              Log to syslog instead of a file
      --nolock              Do not use a lockfile
      --lockfile=LOCKFILE   Lock file, default /var/lock/PROGNAME.lock
      --nostamp             Do not use a success stamp file
      --stampfile=STAMPFILE
                            Success stamp file, default /var/tmp/PROGNAME.success
      --locktimeout=LOCKTIMEOUT
                            Lock timeout in seconds, default 90
      --splay=SPLAY         Sleep a random time between 0 and N seconds before
                            starting, default 0
      -h, --help            show this help message and exit


Overview
--------

The intention is to use the class as a context manager.  It sets up
logging; handles writing logging (optionally) to a file and INFO and
above to STDERR.  It (optionally) locks against a log file to ensure
only one copy of the script is running at a time.  It (optionally)
waits a random amount of time when starting to allow staggering of
runs across many hosts.

Logging
-------

By default:

* all logging of INFO and above goes to LOGFILE
* all logging of INFO and above goes to STDERR

Optionally:

* ```-d``` changes the minimum logging level to DEBUG
* ```-q``` changes the STDERR minimum level to WARNING
* ```--nolog``` turns off logging to LOGFILE
* ```--syslog``` enables logging to a local syslog daemon

In general it is useful to use ```-d``` when debugging.  Generally
```-q``` is added to invocations once a cron job is stable; in that
case only errors will wind up in email, but useful INFO messages wind
up in the log file in case they need to be reviewed (rather than
spamming email.)

Example Use
-----------

See test.py file.

Requirements
------------

Probably Python 2.7.  (Might work on earlier versions.)

TODO
----

See TODO.md file.  Patches welcome.

License
-------

See LICENSE file for details; Apache 2.0
