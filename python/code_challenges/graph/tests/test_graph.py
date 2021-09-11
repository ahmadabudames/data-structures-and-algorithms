from graph.graph import Graph
from graph.graph import *




def test_successfully_added():
    graph = Graph()
    graph.add_node('ahmad')
    graph.add_node('shaher')
    actual=graph.size()
    expected=2
    assert actual == expected




















