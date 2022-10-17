#!/usr/bin/env python
import sys

from mininet.log import setLogLevel, info
from mn_wifi.cli import CLI
from mn_wifi.net import Mininet_wifi

def topology(args):

    net = Mininet_wifi()

    info("*** Creating nodes\n")
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    sta1 = net.addStation( 'sta1', mac='00:00:00:00:00:02', ip='10.0.0.2/8', range='5' )
    sta2 = net.addStation( 'sta2', mac='00:00:00:00:00:03', ip='10.0.0.3/8', range='5' )
    sta3 = net.addStation( 'sta3', mac='00:00:00:00:00:02', ip='10.0.0.4/8', range='5' )
    sta4 = net.addStation( 'sta4', mac='00:00:00:00:00:04', ip='10.0.0.5/8', range='5' )
    sta5 = net.addStation( 'sta5', mac='00:00:00:00:00:05', ip='10.0.0.6/8', range='5' )
    sta6 = net.addStation( 'sta6', mac='00:00:00:00:00:06', ip='10.0.0.7/8', range='5' )
    sta7 = net.addStation( 'sta7', mac='00:00:00:00:00:08', ip='10.0.0.8/8', range='5' )
    sta8 = net.addStation( 'sta8', mac='00:00:00:00:00:09', ip='10.0.0.9/8', range='5' )
    ap1 = net.addAccessPoint( 'ap1', ssid= 'ap1-ssid', mode= 'g', channel= '11', position='150,100,0', range='50' )
    ap2 = net.addAccessPoint( 'ap2', ssid= 'ap1-ssid', mode= 'g', channel= '11', position='100,150,0', range='30' )
    ap3 = net.addAccessPoint( 'ap3', ssid= 'ap2-ssid', mode= 'g', channel= '11', position='200,150,0', range='30' )
    ap4 = net.addAccessPoint( 'ap4', ssid= 'ap2-ssid', mode= 'g', channel= '11', position='225,100,0', range='30' )
    ap5 = net.addAccessPoint( 'ap5', ssid= 'ap3-ssid', mode= 'g', channel= '11', position='200,50,0', range='30' )
    ap6 = net.addAccessPoint( 'ap6', ssid= 'ap3-ssid', mode= 'g', channel= '11', position='100,50,0', range='30' )
    ap7 = net.addAccessPoint( 'ap7', ssid= 'ap4-ssid', mode= 'g', channel= '11', position='75,100,0', range='30' )
    
    c1 = net.addController( 'c1' )

    info("*** Configuring propagation model\n")
    net.setPropagationModel(model="logDistance", exp=4.5)

    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Associating and Creating links\n")
    net.addLink(ap1, h1)
    net.addLink(ap1, ap2)
    net.addLink(ap1, ap3)
    net.addLink(ap1, ap4)
    net.addLink(ap1, ap5)
    net.addLink(ap1, ap6)
    net.addLink(ap1, ap7)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)
    net.addLink(ap5, ap6)
    net.addLink(ap6, ap7)
    net.addLink(ap7, ap2)

    if '-p' not in args:
        net.plotGraph(max_x=300, max_y=200)

    net.setMobilityModel(time=0, model='RandomWayPoint', max_x=300, max_y=200, seed=30)

    info("*** Starting network\n")
    net.build()
    c1.start()
    ap1.start([c1])
    ap2.start([c1])
    ap3.start([c1])
    ap4.start([c1])
    ap5.start([c1])
    ap6.start([c1])
    ap7.start([c1])

    info("*** Running CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology(sys.argv)
