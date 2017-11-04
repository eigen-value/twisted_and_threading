from twisted.application import internet, service
from outside import ServiceUsingThreadingAndDeferred
from twisted.internet import reactor
from twisted.python.log import ILogObserver, FileLogObserver
from twisted.python.logfile import DailyLogFile
from server import port
from server import MyFactory


service = ServiceUsingThreadingAndDeferred()

# Application set-up
application = service.Application("appName")

logfile = DailyLogFile("twistd.log", ".")
application.setComponent(ILogObserver, FileLogObserver(logfile).emit)

protocol_factory = MyFactory()
my_server = internet.TCPServer(port, protocol_factory)
my_server.setServiceParent(application)

reactor.callLater(1, service.start)