import unittest
from main import Graph


class TestIsomorphism(unittest.TestCase):

    def test_graphs_with_different_numbers_of_nodes(self):
        graph1 = Graph(2)
        graph2 = Graph(3)
        self.assertFalse(graph1.are_isomorphic(graph2))

    def test_graphs_with_different_nodes_degrees(self):
        graph1 = Graph(2)
        graph2 = Graph(2)
        graph1.edges = {'A': {'B', 'C'},
                        'B': {'A'}}
        graph1.degrees_of_all_nodes = {2, 1}
        graph2.edges = {'a': {'b'},
                        'b': {'a'}}
        graph2.degrees_of_all_nodes = {1, 1}
        self.assertFalse(graph1.are_isomorphic(graph2))

    def test_isomorphic_graphs1(self):
        graph1 = Graph(6)
        graph1.edges = {'A': {'B', 'D', 'F'},
                        'B': {'A', 'C', 'E'},
                        'C': {'B', 'D', 'F'},
                        'D': {'A', 'C', 'E'},
                        'E': {'F', 'D', 'B'},
                        'F': {'A', 'C', 'E'}}
        graph1.degrees_of_all_nodes = {3, 3, 3, 3, 3, 3}
        graph1.nodes = ['A', 'B', 'C', 'D', 'E', 'F']
        graph2 = Graph(6)
        graph2.edges = {'u': {'x', 'y', 'z'},
                        'x': {'u', 'v', 'w'},
                        'v': {'x', 'y', 'z'},
                        'y': {'u', 'v', 'w'},
                        'w': {'x', 'y', 'z'},
                        'z': {'w', 'v', 'u'}}
        graph2.degrees_of_all_nodes = {3, 3, 3, 3, 3, 3}
        graph2.nodes = ['u', 'x', 'v', 'y', 'w', 'z']
        self.assertTrue(graph1.are_isomorphic(graph2))

    def test_isomorphic_graphs2(self):
        graph1 = Graph(5)
        graph1.edges = {'A': {'C', 'D'},
                        'B': {'D', 'E'},
                        'C': {'E', 'A'},
                        'D': {'A', 'B'},
                        'E': {'B', 'C'}}
        graph1.degrees_of_all_nodes = {2, 2, 2, 2, 2}
        graph1.nodes = ['A', 'B', 'C', 'D', 'E']
        graph2 = Graph(5)
        graph2.edges = {'a': {'e', 'b'},
                        'b': {'a', 'c'},
                        'c': {'d', 'b'},
                        'd': {'e', 'c'},
                        'e': {'a', 'd'}}
        graph2.degrees_of_all_nodes = {2, 2, 2, 2, 2}
        graph2.nodes = ['a', 'b', 'c', 'd', 'e']
        self.assertTrue(graph1.are_isomorphic(graph2))

    def test_non_isomorphic_graphs1(self):
        graph1 = Graph(8)
        graph1.edges = {'A': {'B', 'C', 'E'},
                        'B': {'A', 'D'},
                        'C': {'A', 'D', 'F'},
                        'D': {'B', 'C'},
                        'E': {'A', 'G', 'F'},
                        'F': {'C', 'H', 'E'},
                        'G': {'E', 'H'},
                        'H': {'F', 'G'}}
        graph1.degrees_of_all_nodes = {3, 2, 2, 3, 3, 3, 2, 2}
        graph1.nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        graph2 = Graph(8)
        graph2.edges = {'u': {'x', 'v'},
                        'x': {'u', 'w', 'y'},
                        'v': {'u', 'k', 'w'},
                        'y': {'x', 'z', 'j'},
                        'w': {'x', 'v'},
                        'z': {'y', 'k'},
                        'k': {'j', 'z', 'v'},
                        'j': {'k', 'y'}}
        graph2.degrees_of_all_nodes = {3, 2, 2, 3, 3, 3, 2, 2}
        graph2.nodes = ['u', 'x', 'v', 'y', 'w', 'z', 'k', 'j']
        self.assertFalse(graph1.are_isomorphic(graph2))

    def test_non_isomorphic_graphs2(self):
        graph1 = Graph(5)
        graph1.edges = {'A': {'E', 'D'},
                        'B': {'E', 'D'},
                        'C': {'E', 'D'},
                        'D': {'A', 'B', 'C'},
                        'E': {'B', 'C', 'A'}}
        graph1.degrees_of_all_nodes = {2, 2, 2, 3, 3}
        graph1.nodes = ['A', 'B', 'C', 'D', 'E']
        graph2 = Graph(5)
        graph2.edges = {'a': {'e', 'b'},
                        'b': {'a', 'c', 'd'},
                        'c': {'d', 'b'},
                        'd': {'e', 'c', 'b'},
                        'e': {'a', 'd'}}
        graph2.degrees_of_all_nodes = {2, 2, 2, 3, 3}
        graph2.nodes = ['a', 'b', 'c', 'd', 'e']
        self.assertFalse(graph1.are_isomorphic(graph2))


if __name__ == '__main__':
    unittest.main()