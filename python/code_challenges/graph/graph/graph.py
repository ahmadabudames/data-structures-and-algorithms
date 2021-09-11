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


if __name__ == '__main__':

    graph = Graph()
    ahmad = graph.add_node('ahmad')
    shaher = graph.add_node('shaher')
    ameen = graph.add_node('ameen')
    abu = graph.add_node('abu')
    dames = graph.add_node('dames')

    graph.add_edge(ahmad, ameen)
    graph.add_edge(ahmad, abu)
    graph.add_edge(shaher, ameen)
    graph.add_edge(shaher, dames)
    graph.add_edge(ameen, ahmad)
    graph.add_edge(ameen, shaher)
    graph.add_edge(abu, ahmad)

    print(graph.__str__())
