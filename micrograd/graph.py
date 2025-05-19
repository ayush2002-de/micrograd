from graphviz import Digraph
def trace(root):
    nodes, edges = set(), set()
    def add_edges(node):
        if node not in nodes:
            nodes.add(node)
            for child in node._prev:
                edges.add((child, node))
                add_edges(child)
    add_edges(root)
    return nodes, edges

def draw_graph(root):
    dot = Digraph(format='svg', graph_attr={'rankdir': 'LR'})
    nodes, edges = trace(root)
    for node in nodes:
        uid = str(id(node))
        label = f"<label> {node.label} | <data> data {node.data:.4f} | <grad> grad {node.grad:.4f}"
        dot.node(name = uid, label=label, shape = 'record')
        if node._op:
            dot.node(name = uid + node._op, label = node._op, shape = 'circle')
            dot.edge(uid + node._op, uid)

    for edge1, edge2 in edges:
        dot.edge(str(id(edge1)), str(id(edge2)) + edge2._op)
    return dot