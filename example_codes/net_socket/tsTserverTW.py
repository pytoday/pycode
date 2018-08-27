#!/usr/bin/env python3
# coding=utf-8
# title          : tsTserverTW.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/15 17:12
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from twisted.internet import protocol, reactor
from time import ctime


PORT = 12345


class TSServerProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print('...connected from:', clnt.encode('utf-8'))

    def dataReceived(self, data):
        self.transport.write(('['+ctime()+']: ').encode('utf-8') + data)


factory = protocol.Factory()
factory.protocol = TSServerProtocol
print('waiting for connecting ....')
reactor.listenTCP(PORT, factory)
reactor.run()
