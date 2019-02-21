#This program shows "delay" vs. "Number of Nodes" characteristics when GSA exist
#and when there is no GSA

from create_graph import Topology
from betweenness import BaseClass
from ClusteringAlgorithmn import ClusteringAlgo

import matplotlib.pylab as plt
import matplotlib.lines as mlines

plt.clf()
plt.cla()
plt.close()

D_req = 10
n = 11
s_25 = {}
c_25 = {}
s_100 = {}
c_100 = {}
for i in range(4, 10):
    t = Topology().CreateTopo(i)
    s_25[i*i], c_25[i*i] = ClusteringAlgo().Clustering(t, D_req)
    s_100[i*i], c_100[i*i] = ClusteringAlgo().Clustering(t, 200)
    

lists_25 = sorted(s_25.items())
lists_100 = sorted(s_100.items())

x_25, y_25 = zip(*lists_25)
x_100, y_100 = zip(*lists_100)
plot1, = plt.plot(x_25, y_25)
plot2, = plt.plot(x_100, y_100)

plt.setp(plot1, color='b', linewidth=2.0, marker = '+')
plt.setp(plot2, color='g', linewidth=2.0, marker = '*')

plt.title("Delay vs. Number of nodes")

plt.xlabel("Number of nodes")
plt.ylabel("Delay (ms)")

#legend
plt.legend([plot1, plot2], ("with algorithm", "without algorithm"), 'best')

plt.xlim(0.0, 85.0)
plt.ylim(0.0, 60.)

plt.show()
