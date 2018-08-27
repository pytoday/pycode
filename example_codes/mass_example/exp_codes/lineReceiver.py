#!/usr/bin/env python3
# coding=utf-8
# title          :lineReceiver.py
# description    :
# author         :JackieTsui
# organization   :pytoday.org
# date           :2017/10/26 18:41
# email          :jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
from twisted.internet import reactor
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver


class SimpleLogger(LineReceiver):
    def connectionMade(self):
        print("Got connection from: ", self.transport.client)

    def connectionLost(self, reason):
        print(self.transport.client, "disconnected.")

    def lineReceived(self, line):
        print(line)


factory = Factory()
factory.protocol = SimpleLogger
reactor.listenTCP(1234, factory)
reactor.run()
