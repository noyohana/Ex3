import time
from unittest import TestCase
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.node_data import Node
import networkx as nx


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


class TestGraphAlgo(TestCase):

    def test_save_load_to_json(self):
        g_algo = GraphAlgo()
        file = "../data/A2"
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + '_saved')

    def test_shortest_path(self):
        graph = example_graph()
        g_algo = GraphAlgo(graph)
        shortest_path_value = 9
        shortest_path_list = [0,3,1,2]
        shortest_value = g_algo.shortest_path(0,2)[0]
        shortest_path = g_algo.shortest_path(0,2)[1]
        self.assertEqual(shortest_path_value,shortest_value)
        self.assertEqual(shortest_path_list,shortest_path)
        start = time.time()
        g_algo = GraphAlgo()
        file = "../data/G_30000_240000_1.json"
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + '_saved')
        g_algo.shortest_path(7, 2)
        end = time.time()
        print("time", end - start)

    def test_connected_component(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(1, 0, 0)
        graph.add_edge(2, 1, 0)
        graph.add_edge(0, 2, 0)
        graph.add_edge(0, 3, 0)
        graph.add_edge(3, 4, 0)
        graph_algo = GraphAlgo(graph)
        l1 = graph_algo.connected_component(0)
        l2 = graph_algo.connected_component(2)
        l1.sort()
        l2.sort()
        self.assertEqual(l1,l2)

    def test_connected_components(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_node(2)
        graph.add_node(3)
        graph.add_node(4)
        graph.add_edge(1, 0, 0)
        graph.add_edge(2, 1, 0)
        graph.add_edge(0, 2, 0)
        graph.add_edge(0, 3, 0)
        graph.add_edge(3, 4, 0)
        graph_algo = GraphAlgo(graph)
        ans = graph_algo.connected_components()
        l = [[0,1,2],[3],[4]]
        self.assertEqual(l,ans)
        start = time.time()
        g_algo = GraphAlgo()
        file = "../data/G_10_80_1.json"
        g_algo.load_from_json(file)
        g_algo.connected_components()
        end = time.time()
        print("time", end - start)

    def test_connected_components_nxGraph(self):
        start = time.time()
        g_algo = GraphAlgo()
        file = "../data/G_30000_240000_1.json"
        nx_graph: DiGraph = g_algo.nx_graph(file)
        nx.strongly_connected_components(nx_graph)
        for cc in nx.strongly_connected_components(nx_graph):
            print(cc)
        end = time.time()
        print("time", end - start)

    def test_plot_graph(self):
        g_algo = GraphAlgo()
        file = "../data/A0"
        g_algo.load_from_json(file)
        g_algo.save_to_json(file + '_saved')
        g_algo.plot_graph()
