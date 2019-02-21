from collections import defaultdict
from betweenness import BaseClass
import random

class ClusteringAlgo(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)
        
        self.dic_sw_time = {}
        self.dic_clusters = {}
        
        self.clusters = dict()
        
    
    def Clustering(self, Graph, D_req):
        rem_nodes = []
        nodes_rem = []
        delay_mat = self.delay_matrix(Graph)

        j = 0
        clustering = True
        
        while clustering:
            nodes_cluster = []
            
            if j == 0:
                
                r_n = self.Max_Betweenness(Graph)
                #print "reference node", r_n
                delay_ref_node = {}
                d_mat = delay_mat[r_n]
                for k in range(0, len(d_mat)):
                    delay_ref_node[k] = d_mat[k]
                #print "delay ref node", delay_ref_node 
            else:
                delay_ref_node = {}
                sub_g = Graph.subgraph(nodes_rem)
                #print "sub graph nodes", sub_g.nodes()
                
                r_n = self.Max_Betweenness(sub_g)
                #print "reference node", r_n

                d_mat = delay_mat[r_n]
                
                for k in range(0, len(d_mat)):
                    delay_ref_node[k] = d_mat[k]
                #print "delay ref node", delay_ref_node
               
                del rem_nodes[:]
                del nodes_rem[:]
                
            for i in delay_ref_node.keys():
                if delay_ref_node[i] <= D_req:
                    nodes_cluster.append(i)
                else:
                    rem_nodes.append(i)
                    
            self.clusters[r_n] = nodes_cluster
            #print "cluster", clusters
            j+=1
            #print "rem_nodes", rem_nodes
            val = self.clusters.values()
            lst_val = []
            for i in range(0, len(val)):
                for k in range(0, len(val[i])):
                    lst_val.append(val[i][k])
            #print "values", lst_val
            
            for z in rem_nodes:
                if z not in lst_val:
                    nodes_rem.append(z)
                    #print "added", z
                else:
                    pass
                    #print "already in a cluster"
                
            #print "candidate cluster", nodes_cluster
            #print "remaining nodes", nodes_rem
            if len(nodes_rem) == 0:
                clustering = False
                #print "false"
        #print "cluster with gateway:list of nodes", self.clusters

        
        """check whether a node present in different clusters
        if a node present in different clusters, check delay
        between the gateway node of the clusters and the node.
        The node finally remains in the cluster with less delay"""
        
        list1 = self.clusters.items()
        #print list1
        for i in range(0,len(list1)):
            (k1,set1) = list1[i]
            #print "set1", set1
            for j in range(i+1,len(list1)):
                (k2, set2) = list1[j]
                #print "set2", set2
                for e in range(0, len(set1)):
                    for f in range(0, len(set2)):
                        try:
                            if set1[e] == set2[f]:
                                #print "%s in set2" %set1[e]
                                d1 = delay_mat[k1][set1[e]]
                                d2 = delay_mat[k2][set1[e]]
                                                     
                                if d1 <= d2:
                                    set2.remove(set2[f])
                                    #print "after element being removed set2", set2
                                    self.clusters[k2] = set2
                                else:
                                    set1.remove(set1[e])
                                    #print "after element being removed set1", set1
                                    self.clusters[k1] = set1
                        except:
                            #print "error handeled"
                            pass
        #print "final cluster", self.clusters
        
        max_tree = dict()
        cost_g_v = dict()
        for y in self.clusters.keys():
            cluster_value = self.clusters[y]
            #print cluster_value
            for v in range(0, len(cluster_value)):
                #cost of trees in a cluster
                cost_g_v.setdefault(y, []).append(delay_mat[y][cluster_value[v]])
        #print "cost of each node from the gateway of a cluster", cost_g_v

        for y in cost_g_v.keys():
            #max tree cost in a cluster
            max_tree[y] = max(cost_g_v[y])
        #print "Maximum cost of the tree in a cluster", max_tree

        #Maximum cost among the cluster is the switching time of the network
        sw_time = max(max_tree.values())
        #print "Network switching time",sw_time

        no_of_cluster = 0
        for y in self.clusters.keys():
            no_of_cluster += 1

        n = len(Graph.nodes())
        self.dic_clusters[n] = no_of_cluster
        self.dic_sw_time[n] = sw_time
        
        #print "number of cluster", self.dic_clusters 
        #print "Numer of nodes:S/w time", self.dic_sw_time
        return sw_time, no_of_cluster
            
