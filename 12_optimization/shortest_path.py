# shortest_path.py
from graph import Digraph
from graph import Graph
from graph import Node
from graph import Edge

def print_path(path):
    '''Assumes path is a list of nodes'''
    result = ''
    for i in range(0, len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result


def depth_first_search(graph, start, end, path, shortest, to_print = False):
    '''
    Assumes graph is a Digraph; start and end are nodes;
        path and shortest ate lists of nodes
    Returns a shortest path froms tart to end in graph
    '''
    path = path + [start]
    if to_print:
        print('Current DFS path:', print_path(path))
    if start == end:
        return path
    for node in graph.children_of(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                new_path = depth_first_search(graph, node, end, path, shortest, to_print)
                if new_path != None:
                    shortest = new_path
    return shortest


def breadth_first_search(graph, start, end, to_print = False):
    '''
    Assumes graph is a Drigraph; start and end are nodes
    Returns a shortest path froms tart to end in graph
    '''
    init_path = [start]
    path_queue = [init_path]
    while len(path_queue) != 0:
        # get and remove oldest element in path_queue
        temp_path = path_queue.pop(0)
        if to_print:
            print('Current BFS path:', print_path(temp_path))
        last_node = temp_path[-1]
        if last_node == end:
            return temp_path
        for next_node in graph.children_of(last_node):
            if next_node not in temp_path:
                new_path = temp_path + [next_node]
                path_queue.append(new_path)
    return None


def shortest_path(graph, start, end, alg = 'dfs', to_print = False):
    '''
    Assumes graph is a Digraph; start and end are nodes; alg can be
        `bfs` or `dfs`, default is `dfs`
    Returns a shortest path from start to end in graph
    '''
    assert alg in ('dfs', 'bfs')
    if alg == 'dfs':
        return depth_first_search(graph, start, end, [], None, to_print)
    else:
        return breadth_first_search(graph, start, end, to_print)


def test_shortest_path():
    nodes = []
    # create 6 nodes
    for name in range(0, 6):
        nodes.append(Node(str(name)))
    g = Digraph()
    # add nodes to graph
    for n in nodes:
        g.add_node(n)
    # add edges to graph
    g.add_edge(Edge(nodes[0], nodes[1]))
    g.add_edge(Edge(nodes[1], nodes[2]))
    g.add_edge(Edge(nodes[2], nodes[3]))
    g.add_edge(Edge(nodes[2], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[4]))
    g.add_edge(Edge(nodes[3], nodes[5]))
    g.add_edge(Edge(nodes[0], nodes[2]))
    g.add_edge(Edge(nodes[1], nodes[0]))
    g.add_edge(Edge(nodes[3], nodes[1]))
    g.add_edge(Edge(nodes[4], nodes[0]))
    # compute shortest path
    for alg in ('dfs', 'bfs'):
        sp = shortest_path(g, nodes[0], nodes[5], alg = alg, to_print = True)
        print('Shortest path is: ', print_path(sp))
        print('')


if __name__ == '__main__':
    test_shortest_path()