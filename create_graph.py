import networkx as nx

class Topology(object):
    def __init__(self):
        pass
    
    def CreateTopo(self, n):
        g = nx.Graph()
        g.clear()
        x = {}
        #add nodes to graph
        for i in range(n*n):
            g.add_node(i)

        for node in g.nodes():
            x[node]= node

        #print x
        #print g.nodes()
        
        #connect the edges 
        for index in range(n*n):
            if index == (n*n-1):
                continue
            elif (index % n) == (n-1):
                g.add_edge(x[index], x[index+n], weight = 3.0)
            elif index >= (n*(n-1)):
                g.add_edge(x[index], x[index+1], weight = 4.0)
            else:
                g.add_edge(x[index], x[index+n], weight = 4.0)
                g.add_edge(x[index], x[index+1], weight = 3.0)
                
        #print g.edges()
        return g
