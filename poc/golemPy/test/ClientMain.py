
import sys
sys.path.append('../src/')
sys.path.append('../src/core')
sys.path.append('../src/vm')
sys.path.append('../src/task')
sys.path.append('../src/task/resource')
sys.path.append('../src/network')
sys.path.append('../src/manager')
sys.path.append('../src/manager/server')
sys.path.append('../src/manager/client')
sys.path.append('../testtasks/minilight/src')
sys.path.append('../testtasks/pbrt')

from twisted.internet import reactor

from AppConfig import AppConfig
from Client import Client
from Message import initMessages
from ClientConfigDescriptor import ClientConfigDescriptor




def main():

    

    initMessages()

    cfg = AppConfig.loadConfig()

    optNumPeers     = cfg.getOptimalPeerNum()
    managerPort     = cfg.getManagerListenPort()
    startPort       = cfg.getStartPort()
    endPort         = cfg.getEndPort()
    seedHost        = cfg.getSeedHost()
    seedHostPort    = cfg.getSeedHostPort()
    sendPings       = cfg.getSendPings()
    pingsInterval   = cfg.getPingsInterval()
    clientUid       = cfg.getClientUid()
    addTasks        = cfg.getAddTasks()

    gettingPeersInterval    = cfg.getGettingPeersInterval()
    gettingTasksInterval    = cfg.getGettingTasksInterval()
    taskRequestInterval     = cfg.getTaskRequestInterval()
    estimatedPerformance    = cfg.getEstimatedPerformance()
    nodeSnapshotInterval    = cfg.getNodeSnapshotInterval()

    configDesc = ClientConfigDescriptor()

    configDesc.clientUid      = clientUid
    configDesc.startPort      = startPort
    configDesc.endPort        = endPort
    configDesc.managerPort    = managerPort
    configDesc.optNumPeers    = optNumPeers
    configDesc.sendPings      = sendPings
    configDesc.pingsInterval  = pingsInterval
    configDesc.addTasks       = addTasks
    configDesc.clientVersion  = 1

    configDesc.seedHost               = seedHost
    configDesc.seedHostPort           = seedHostPort

    configDesc.gettingPeersInterval   = gettingPeersInterval
    configDesc.gettingTasksInterval   = gettingTasksInterval
    configDesc.taskRequestInterval    = taskRequestInterval 
    configDesc.estimatedPerformance   = estimatedPerformance
    configDesc.nodeSnapshotInterval   = nodeSnapshotInterval
    configDesc.maxResultsSendignDelay = cfg.getMaxResultsSendingDelay()

    print "Adding tasks {}".format( addTasks )
    print "Creating public client interface with uuid: {}".format( clientUid )
    c = Client( configDesc ) 

    print "Starting all asynchronous services"
    c.startNetwork( )

    reactor.run()


main()
