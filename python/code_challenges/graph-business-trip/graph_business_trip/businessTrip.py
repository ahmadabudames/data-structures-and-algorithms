class Node:
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return f'Node > {self.data}'

class Edge:
    def __init__(self, Node , weight):
        self.Node = Node
        self.weight = weight

class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, data):
        item = Node(data)
        self.adjacency_list[item] = []
        return item

    def add_edge(self, first_node, last_node, weight=0):
        nodes=self.adjacency_list.keys()
        if not first_node in nodes and not last_node in nodes:
            return 'nothing in graph'
        elif not first_node in nodes:
            return 'first node empty'
        elif not last_node in nodes:
            return 'second node empty'

        edges = Edge(last_node, weight)
        self.adjacency_list[first_node].append(edges)

    def get_nodes(self):
        lists=[]
        for Node in self.adjacency_list.keys():
            lists.append(Node)
        if len(lists)==0:
            return None
        return lists

    def get_neighbors(self, node):
        lists=[]

        if node in self.adjacency_list :

            for edges in self.adjacency_list[node]:

               lists.append((edges.Node, edges.weight))

            return lists
        if len(lists)==0:
            return None


    def size(self):
        return len(self.adjacency_list.keys())

    def __str__(self):
        output = ''
        for Node in self.adjacency_list.keys():

            output += Node.data

            for edges in self.adjacency_list[Node]:
                output += ' -> ' + edges.Node.data

            output += '\n'
        return output

def business_trip(Graph,name_ofCity):
        possibility_path = True
        count = 0
        for i in range(len(name_ofCity)-1):
            for name in Graph.get_neighbors(name_ofCity[i]):
             if name_ofCity[i+1]==name[0]:
                count+=name[1]
                break
             else:
                possibility_path=False

        if possibility_path==False:
            count=0

        return possibility_path, f'${count}'


if __name__ == '__main__':

    graph = Graph()

    pandora= graph.add_node('pandora')
    arendelle= graph.add_node('arendelle')
    metroville= graph.add_node('metroville')
    narina= graph.add_node('narina')
    naboo= graph.add_node('naboo')
    manstropolis= graph.add_node('manstropolis')

    graph.add_edge(pandora,arendelle,150)
    graph.add_edge(pandora,metroville,82)
    graph.add_edge(arendelle,pandora,150)
    graph.add_edge(arendelle,metroville,99)
    graph.add_edge(arendelle,manstropolis,42)
    graph.add_edge(manstropolis,metroville,105)
    graph.add_edge(metroville,manstropolis,105)
    graph.add_edge(metroville,pandora,82)
    graph.add_edge(narina,metroville,37)
    graph.add_edge(metroville,narina,37)
    graph.add_edge(narina,naboo,250)
    graph.add_edge(naboo,narina,250)
    graph.add_edge(naboo,metroville,26)
    graph.add_edge(metroville,arendelle,99)
    graph.add_edge(manstropolis,arendelle,42)
    graph.add_edge(metroville,naboo,26)
    graph.add_edge(naboo,manstropolis,73)
    graph.add_edge(manstropolis,naboo,73)

    print(business_trip(graph,[naboo,pandora]))
    print(business_trip(graph,[narina,arendelle,naboo]))


