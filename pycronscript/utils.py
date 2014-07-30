import shlex
import logging
import __main__

logger = logging.getLogger(__main__.__name__)


def run(cmd, cwd=None, shell=False, env=None):
    '''Run a command and gather exit code, stderr, stdout.  cmd should
       be a single string.  Return the exit code, stdout, and stderr
       strings.'''

    from subprocess import PIPE, Popen

    logger.info("Running: %s" % cmd)
    if shell:
        args = cmd
    else:
        args = shlex.split(cmd)

    p = Popen(args, shell=shell, cwd=cwd, stdout=PIPE, stderr=PIPE, env=env)
    stdout, stderr = p.communicate()

    return p.returncode, stdout, stderr


def run_log(cmd, cwd=None, shell=False, env=None):
    '''Run a command and gather exit code, stderr, stdout.  cmd should
       be a single string.  Output is logged.  Return the exit code,
       stdout and stderr strings.'''

    returncode, stdout, stderr = run(cmd, cwd, shell, evn)

    # Log command output
    if stdout:
        for i in stdout.split('\n'):
            logger.info("[stdout] %s" % i.strip())
    if stderr:
        for i in stderr.split('\n'):
            logger.warn("[stderr] %s" % i.strip())

    return p.returncode, stdout, stderr


def run_try(args, cwd=None, shell=False, env=None):
    '''Run a command; log and die if a failure occurs'''

    try:
        (exit_code, stdout, stderr) = \
                run_log(args, cwd=cwd, shell=shell, env=env)
    except Exception:
        logger.error('Command caused an exception: %s' % args)
        raise

    if exit_code != 0:
        logger.error('Command had non-zero exit status %d: : %s' % (exit_code,
                                                                    args))
        raise Exception('Non-zero exit status')

    return exit_code, stdout, stderr
