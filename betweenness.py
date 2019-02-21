import networkx as nx
from collections import defaultdict
import random

class BaseClass(object):
    def __init__(self):
        pass
    
    def cost_link(self, graph, path):
        """calculate cost of a link"""
        
        i=0
        cost = 0
        while i<len(path):
            s1 = path[i]
            #print s1
            try:
                s2 = path[i+1]
                #print s2
                if not s1 == s2:
                    for n1, n2, attr in graph.edges(data=True):
                        if (s1==n1 and s2==n2) or (s1==n2 and s2==n1):
                            #print "(%s, %s) weight: %s" %(s1, s2, attr['weight'])
                            cost = cost + attr['weight']
            except:
                pass
                #print "end of list"
            finally:
                i+=1
        
        return cost

    #link_c = cost_link(path)
    #print "cost", link_c

    def delay_matrix(self, graph):
        """calculates delay matrix, from a node to every
        other nodes in the network"""
        
        cost_i_j = dict()
        x = {}
        for node in graph.nodes():
            x[node]= node
        for j in graph.nodes():
            i=0
            while i<len(x):
                paths = nx.shortest_path(graph, x[j], x[i], weight = 'weight')
                #print paths
                cost_i_j.setdefault(j, []).append(self.cost_link(graph, paths)) 
                i+=1
        return cost_i_j

    #self.delay_mat = self.delay_matrix(Graph)
    #print "total delay matrix",self.delay_mat
    #print "delay from node: 0 to 8", delay_mat[0][8]

    def Betweenness(self, graph):
        #calculates nodes betweenness centrality 
        node_bet_cen = nx.betweenness_centrality(graph, k=None,
                                                 normalized=False, weight='weight',
                                                 endpoints=False, seed=None)

        return node_bet_cen

    #betweenness_cent = Betweenness(g)
    #print "nodes betweenness centrality", betweenness_cent

    def Max_Betweenness(self, graph):
        #select the node(s) with high betweenness centrality
        betweenness_cent = self.Betweenness(graph)
        #print "nodes betweenness centrality", betweenness_cent
        node_max = []
        node_max.append(max(betweenness_cent, key=betweenness_cent.get))
        #print "node(s) with high betweenness centrality", node_max

        #choose a node randomly from node_max
        ref_node = random.choice(node_max)
        #print "reference node", ref_node
        return ref_node
        
 
