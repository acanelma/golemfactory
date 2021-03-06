
import sys
sys.path.append('../src/')
sys.path.append('../src/core')
sys.path.append('../src/ui')
sys.path.append('../src/vm')
sys.path.append('../src/task')
sys.path.append('../src/network')
sys.path.append('../src/manager')
sys.path.append('../src/task/resource')
sys.path.append('../src/manager/server')
sys.path.append('../testtasks/minilight/src')
sys.path.append('../testtasks/pbrt')

from UiGen import genUiFiles

genUiFiles( "./../src" )

from twisted.internet.protocol import Protocol, Factory

from threading import Thread
from AppConfig import AppConfig
from ClientConfigDescriptor import ClientConfigDescriptor
from NodesManager import  NodesManager
from NodesManagerLogic import EmptyManagerLogic
from Message import initMessages

def main():

    initMessages()

    port = AppConfig.managerPort()
    manager = NodesManager( None )
    logic = EmptyManagerLogic( port, manager.managerServer )
    manager.setManagerLogic( logic )

    try:
        import qt4reactor
    except ImportError:
        # Maybe qt4reactor is placed inside twisted.internet in site-packages?
        from twisted.internet import qt4reactor
    qt4reactor.install()
    from twisted.internet import reactor

    logic.setReactor( reactor )
    manager.execute( True )

    reactor.run()
    sys.exit( 0 )

main()
