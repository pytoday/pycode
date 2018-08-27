#!/usr/bin/env python3
# coding=utf-8
# title          : tsTcintTW.py
# description    :
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/15 17:44
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from twisted.internet import protocol, reactor


HOST = '127.0.0.1'
PORT = 12345


class TSCintProtocol(protocol.Protocol):
    def sendData(self):
        self.data = input('> ')
        if self.data:
            print('....sending %s ...' % self.data)
            self.transport.write(self.data.encode('utf-8'))
        else:
            self.transport.loseConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print(data.decode('utf-8'))
        self.sendData()


class TSCintFactory(protocol.ClientFactory):
    protocol = TSCintProtocol
    clientConnectiongLost = clientConnectiongFailed = lambda self, connector, reason: reactor.stop()


reactor.connectTCP(HOST, PORT, TSCintFactory())
reactor.run()
