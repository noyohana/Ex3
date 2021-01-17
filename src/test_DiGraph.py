from unittest import TestCase

from src.DiGraph import DiGraph
from src.node_data import Node


def example_graph():
    Graph = DiGraph()
    node_a = Node(0)
    node_b = Node(1)
    node_c = Node(2)
    node_d = Node(3)
    node_e = Node(4)
    Graph.add_node(node_a.key, (4.0, 6.0, 0.0))
    Graph.add_node(node_b.key, (7.0, 11.0, 0.0))
    Graph.add_node(node_c.key, (12.0, 11.0, 0.0))
    Graph.add_node(node_d.key, (7.0, 3.0, 0.0))
    Graph.add_node(node_e.key, (12.0, 3.0, 0.0))
    Graph.add_edge(node_a.key, node_b.key, 10.0)
    Graph.add_edge(node_a.key, node_d.key, 5.0)
    Graph.add_edge(node_b.key, node_c.key, 1.0)
    Graph.add_edge(node_b.key, node_d.key, 2.0)
    Graph.add_edge(node_c.key, node_e.key, 4.0)
    Graph.add_edge(node_d.key, node_e.key, 2.0)
    Graph.add_edge(node_d.key, node_c.key, 9.0)
    Graph.add_edge(node_d.key, node_b.key, 3.0)
    Graph.add_edge(node_e.key, node_a.key, 7.0)
    Graph.add_edge(node_e.key, node_c.key, 6.0)
    return Graph


def empty_graph():
    Graph = DiGraph()
    return Graph


class TestDiGraph(TestCase):

    def test_01(self):
        graph = example_graph();
        size = 5
        self.assertEqual(size, graph.v_size())
        for i in range(len(graph.graph)):
            graph.remove_node(i)
        # adding 5 vertexes and 10 edges and removing 5 vertexes
        self.assertEqual(20, graph.get_mc())
        size_after = 0
        self.assertEqual(size_after, graph.v_size())
        g = empty_graph()
        size_empty = 0
        self.assertEqual(size_empty, g.v_size())

    def test_02(self):
        graph = example_graph()
        size = 10
        self.assertEqual(size, graph.e_size())
        for i in range(len(graph.graph)):
            graph.remove_edge(0, 1)
        self.assertEqual(9, graph.e_size())
        for i in range(len(graph.graph)):
            graph.remove_edge(0, 5)
        self.assertEqual(9, graph.e_size())
        g = empty_graph()
        self.assertEqual(0, g.e_size())

    def test_03(self):
        # out
        graph = example_graph()
        node1 = graph.graph.get(0)
        ll_node1 = [1, 3]
        node2 = graph.graph.get(3)
        ll_node2 = [4, 2, 1]
        ll_test1 = []
        ll_test2 = []
        for i in graph.all_out_edges_of_node(node1.get_key()):
            ll_test1.append(i)
        for i in graph.all_out_edges_of_node(node2.get_key()):
            ll_test2.append(i)
        self.assertEqual(ll_node1, ll_test1)
        self.assertEqual(ll_node2, ll_test2)

        # in
        node1 = graph.graph.get(2)
        ll_node1 = [1, 3, 4]
        node2 = graph.graph.get(3)
        ll_node2 = [0, 1]
        ll_test1 = []
        ll_test2 = []
        for i in graph.all_in_edges_of_node(node1.get_key()):
            ll_test1.append(i)
        for i in graph.all_in_edges_of_node(node2.get_key()):
            ll_test2.append(i)
        self.assertEqual(ll_node1, ll_test1)
        self.assertEqual(ll_node2, ll_test2)

    def test_04(self):
        graph = example_graph()
        graph.add_node(9)
        graph.add_node(3)
        self.assertEqual(6,graph.v_size())
        graph.remove_node(9)
        self.assertEqual(5,graph.v_size())
        graph.remove_node(10)
        self.assertEqual(5, graph.v_size())
        self.assertEqual(10,graph.e_size())
        graph.add_edge(0,5,9)
        self.assertEqual(10, graph.e_size())
        print(graph.graph.get(0))
        graph.add_edge(0,1,4.0)
        self.assertEqual(10, graph.e_size())

