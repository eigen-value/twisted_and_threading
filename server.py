from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import connectionDone

port = 45678


class MyFactory(Factory):

    def __init__(self):
        print "Protocol Factory open"

    def buildProtocol(self, addr):
        return MyProtocol()


class MyProtocol(LineReceiver):

    def __init__(self):
        pass

    def connectionMade(self):
        print "connection made from ", self.transport.getPeer()

    def connectionLost(self, reason=connectionDone):
        print "connection with %s dropped" % self.transport.getPeer()

    def lineReceived(self, line):
        print "received line: %s" % line