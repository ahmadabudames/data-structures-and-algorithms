from graph_breadth_first.breathFirst import *


class Queue():
    def __init__(self):
        self.dq = deque()
    def enqueue(self, value):
        self.dq.appendleft(value)
    def dequeue(self):
        return self.dq.pop()
    def __len__(self):
        return len(self.dq)

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


    def BreadthFirst(self,node):
            if node not in self.adjacency_list:
                return 'no node in graph'
            list_nodes=[]
            breadth_first = Queue()
            local = set()

            breadth_first.enqueue(node)
            local.add(node)

            while breadth_first:
                front=breadth_first.dequeue()
                list_nodes.append(front)
                for edge in self.adjacency_list[front]:

                    if edge.Node not in local:

                        local.add(edge.Node)
                        breadth_first.enqueue(edge.Node)

            return list_nodes


if __name__ == '__main__':
    test = Graph()
    pandora= test.add_node('pandora')
    arendelle= test.add_node('arendelle')
    metroville= test.add_node('metroville')
    narina= test.add_node('narina')
    naboo= test.add_node('naboo')
    manstropolis= test.add_node('manstropolis')

    print(test.__str__())


