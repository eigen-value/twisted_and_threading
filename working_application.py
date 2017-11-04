from twisted.internet import reactor
from outside import ServiceUsingThreadingAndDeferred
from server import port
from server import MyFactory

service = ServiceUsingThreadingAndDeferred()

protocol_factory = MyFactory()
reactor.listenTCP(port, protocol_factory)

service.start()

reactor.run()