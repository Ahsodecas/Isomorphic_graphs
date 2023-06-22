from collections import defaultdict
import itertools


class Graph:
    def __init__(self, num_of_nodes: int = 0):
        self.num_of_nodes: int = num_of_nodes
        self.edges = defaultdict(set)
        self.nodes: list[str] = []
        self.degrees_of_all_nodes = set()

    def add_node(self, node: str) -> None:
        """
        Adds one node to the list of all nodes of the graph.
        :param node: character, which represents new node, ex. 'A'
        :return: None
        """
        self.nodes += node

    def add_edges_to_node(self, node: str, edges: set) -> None:
        """
        Adds edges formed with the node to the dictionary of all edges.
        node is the key, and edges is the set of values of the dictionary.
        Adds the degree of the node to the set of all nodes' degrees of the graph.
        :param node: character, which represents a node
        :param edges: set of nodes, that form edges with the given node
        :return: None
        """
        self.edges[node] = edges
        self.degrees_of_all_nodes.add(self.degree_of_node(node))

    def degree_of_node(self, node: str) -> int:
        """
        Calculates the degree of one node by calculating the number of nodes
        (which are stored as a set) it forms edges with.
        :param node: character, which represents a node
        :return: degree of the node - length of the set of edges
        """
        return len(self.edges[node])

    def compare_number_of_nodes(self, graph) -> bool:
        """
        Compares the total number of nodes of two graphs.
        :param graph: another graph of type Graph to compare with
        :return: True if equal, False otherwise
        """
        return self.num_of_nodes == graph.num_of_nodes

    def compare_degrees_of_nodes(self, graph) -> bool:
        """
        Checks if two graphs have nodes with the same degrees in general.
        :param graph: another graph of type Graph to compare with
        :return: True if equal, False otherwise
        """
        return self.degrees_of_all_nodes == graph.degrees_of_all_nodes

    def create_nodes_map(self, nodes_map: dict[str, str], permutation_list: list[str], graph) -> bool:
        """
        Creates(updates) a dictionary nodes_map that defines the relation between names of nodes of the first graph
        and those of the second graph, tells which node of the second graph should be replaced
        with which node of the first graph to make them the same.
        (ex. {'A' : 'd', 'B' : 'c'}, where 'A', 'B' are node of the first graph, 'd' and 'c' - of the second graph).
        If due to the given permutation some corresponding nodes of different graphs have different degrees,
        nodes_map is not created, return False.
        :param nodes_map: dictionary that assigns nodes of one graph to the nodes of the other graph
        :param permutation_list: ordered list of nodes of the graph
        :param graph: the second graph which nodes are listed in permutation_list,
        the goal is to define how to replace its nodes with nodes of the first graph
        :return: True if nodes_map was successfully created, False otherwise
        """
        for i in range(self.num_of_nodes):
            if self.degree_of_node(chr(ord('A') + i)) == graph.degree_of_node(permutation_list[i]):
                nodes_map[chr(ord('A') + i)] = permutation_list[i]
            else:
                return False
        return True

    def are_isomorphic(self, graph):
        """
        Checks whether two graphs are isomorphic.
        At first, checks that the two graphs have the same number of nodes
        and equal number of nodes of the same degree.
        Then, creates all possible permutations of nodes of the second graph, and creates a dictionary nodes_map
        that assigns a node from one permutation to node of the first graph in form of dictionary
        (ex. {'A' : 'd', 'B' : 'c'}, where 'A', 'B' are new names, 'd' and 'c' are old names).
        Replaces all names of nodes in the dict of edges of the second graph using node_map,
        and checks whether it is identical to the dict of edges of the first graph.
        :param graph: another graph of type Graph to compare with
        :return: True and nodes_map(instruction how to replace names of nodes of second graph
         with respective nodes of the first graph) if two graphs are isomorphic,
         False otherwise
        """
        if not (self.compare_number_of_nodes(graph)):
            return False
        if not (self.compare_degrees_of_nodes(graph)):
            return False
        all_nodes_permutations: list[()] = create_all_permutations(graph.nodes)
        for permutation in all_nodes_permutations:
            permutation = list(permutation)
            copied_graph_edges: dict[str, set] = graph.edges.copy()
            nodes_map: dict[str, str] = {}
            if not self.create_nodes_map(nodes_map, permutation, graph):
                break
            replace_nodes_names_in_dict_of_edges(copied_graph_edges, nodes_map)
            if copied_graph_edges == self.edges:
                print(nodes_map)  # uncomment for unittests
                return True, nodes_map
        return False


def replace_nodes_names_in_dict_of_edges(edges: dict[str, set], nodes_map: dict[str, str]):
    """
    Using nodes_map replaces all old names in the dictionary of edges with new names accordingly.
    :param edges: dictionary of edges with names that have to be replaced
    :param nodes_map: a dictionary that tells which new name of each node corresponds to which old name
    (ex. {'A' : 'd', 'B' : 'c'}, where 'A', 'B' are new names, 'd' and 'c' are old names)
    :return: None
    """
    for new_name, old_name in nodes_map.items():
        set_of_new_edges = set()
        set_of_old_edges: set = edges[old_name]
        for edge in set_of_old_edges:
            for key in nodes_map:
                if nodes_map[key] == edge:
                    edge = key
                    break
            set_of_new_edges.add(edge)
        del edges[old_name]
        edges[new_name] = set_of_new_edges


def create_all_permutations(nodes: list[str]) -> list[()]:
    """
    Creates all possible permutations of the given nodes.
    :param nodes: list of nodes
    :return: list of tuples containing all possible permutations
    """
    return list(itertools.permutations(nodes))


def get_input_edges(graph: Graph, first_node_name: str):
    """
    Gets input from the user: neighbouring nodes of each node(can be with repetitions).
    Stores obtained data and each node into graph.
    :param graph: object of type Graph representing a simple graph.
    :param first_node_name: name of the first node of the graph, ex. 'A', or 'a',
    others will be created in alphabetical order
    :return: None
    """
    for i in range(graph.num_of_nodes):
        current_node: str = chr(ord(first_node_name) + i)
        nodes_forming_edges: set = set(input(f"{current_node}: ").split())
        graph.add_node(current_node)
        graph.add_edges_to_node(current_node, nodes_forming_edges)


def print_result(isomorphic: bool, nodes_map: dict[str, str] = None):
    """
    Prints whether the graphs are isomorphic. If they are, additionally prints nodes_map.
    :param isomorphic: True if graphs are isomorphic, False otherwise
    :param nodes_map: a dictionary that tells which node of the second graph should be replaced
    with which node of the first graph to make them the same
    :return: None
    """
    if isomorphic:
        print("The graphs are isomorphic.")
        print("Second graph can be transformed into the first one by replacing nodes names in the following way:")
        print(nodes_map)
    else:
        print("The graphs are not isomorphic.")


def main():
    graph1 = Graph(int(input("Enter number of nodes in the first graph: ")))
    get_input_edges(graph1, 'A')

    graph2 = Graph(int(input("Enter number of nodes in the second graph: ")))
    get_input_edges(graph2, 'a')

    print_result(graph1.are_isomorphic(graph2))


if __name__ == '__main__':
    main()


