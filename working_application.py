from twisted.internet import reactor
from outside import ServiceUsingThreadingAndDeferred
from server import port
from server import MyFactory

third_party_service = ServiceUsingThreadingAndDeferred()

protocol_factory = MyFactory()
reactor.listenTCP(port, protocol_factory)

third_party_service.start()

reactor.run()