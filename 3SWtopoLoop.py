#!/usr/bin/env python
"""
example Unknown Topology
  
   h0----S0 ------ S1----h1
          |        |
           |      |
            |    |
             |  | 
              ||
              S2
              |
              |
             h2
"""

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def topology():

   #net = Mininet()
   #Define a remote controller
   net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)
   c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.1', port=6633)
   #Create nodes in the network
   #c0 = net.addController()
   h1 = net.addHost('h1')
   s1 = net.addSwitch('s1')
   h2 = net.addHost('h2')
   s2 = net.addSwitch('s2')
   h3 = net.addHost('h3')
   s3 = net.addSwitch('s3')

   #Creating links between nodes in network
   net.addLink(h1, s1)
   net.addLink(h2, s2)
   net.addLink(h3, s3)

   #Creating links between switches (loop configuration)
   net.addLink(s1, s2)
   #net.addLink(s1, s3)
   net.addLink(s2, s3)

   #Configuring of IP addresses in interfaces
   h1.setIP('192.168.1.1', 24)
   h2.setIP('192.168.1.2', 24)
   h3.setIP('192.168.1.3', 24)

   c1.start()
   # s1.start()
   # s2.start()
   # s3.start()
   net.start()
   #net.staticArp()
   net.pingAll()
   CLI( net )
   net.stop()
if __name__ == '__main__':
     setLogLevel( 'info' )
     topology()