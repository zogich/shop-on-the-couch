
import os

from buildbot_worker.bot import Worker
from twisted.application import service

basedir = '/Users/ivan/Desktop/egor_learning/github/shop-on-the-couch/.buildbot/worker-main'
rotateLength = 10000000
maxRotatedFiles = 10

# if this is a relocatable tac file, get the directory containing the TAC
if basedir == '.':
    import os.path
    basedir = os.path.abspath(os.path.dirname(__file__))

# note: this line is matched against to check that this is a worker
# directory; do not edit it.
application = service.Application('buildbot-worker')

from twisted.python.logfile import LogFile
from twisted.python.log import ILogObserver, FileLogObserver
logfile = LogFile.fromFullPath(
    os.path.join(basedir, "twistd.log"), rotateLength=rotateLength,
    maxRotatedFiles=maxRotatedFiles)
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

buildmaster_host = 'localhost'
port = 9989
workername = 'worker-main'
passwd = 'pass'
keepalive = 600
umask = None
maxdelay = 300
numcpus = None
allow_shutdown = None
maxretries = None
use_tls = 0
delete_leftover_dirs = 0
proxy_connection_string = None
protocol = 'pb'

s = Worker(buildmaster_host, port, workername, passwd, basedir,
           keepalive, umask=umask, maxdelay=maxdelay,
           numcpus=numcpus, allow_shutdown=allow_shutdown,
           maxRetries=maxretries, protocol=protocol, useTls=use_tls,
           delete_leftover_dirs=delete_leftover_dirs,
           proxy_connection_string=proxy_connection_string)
s.setServiceParent(application)
