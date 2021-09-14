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


    def depth_first(self,first_point):
        if first_point not in self.adjacency_list.keys():
            return 'empty node'
        Exiest=[]

        def dfs(node):

            if not node in Exiest:
                Exiest.append(node)
            for second_node in self.get_neighbors(node):
                if not second_node[0] in Exiest:
                    dfs(second_node[0])

        dfs(first_point)

        return

if __name__ == '__main__':

    TEST = Graph()

    A= TEST.add_node('A')
    B= TEST.add_node('B')
    C= TEST.add_node('C')
    G= TEST.add_node('G')
    D= TEST.add_node('D')
    E= TEST.add_node('E')
    H= TEST.add_node('H')
    F= TEST.add_node('F')



    TEST.add_edge(A,B)
    TEST.add_edge(A,D)
    TEST.add_edge(B,A)
    TEST.add_edge(B,C)
    TEST.add_edge(B,D)
    TEST.add_edge(C,B)
    TEST.add_edge(C,G)
    TEST.add_edge(G,C)
    TEST.add_edge(D,A)


    print(TEST.depth_first(B))

