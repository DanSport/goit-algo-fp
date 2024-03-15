import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, label=node.val)  # Використання id та збереження значення вузла
        pos[node.id] = (x, y)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_dfs(tree_root):
    def dfs_visit(node, dfs_colors):
        nonlocal current_color
        dfs_colors[node.id] = current_color
        current_color += color_step

        if node.left:
            dfs_visit(node.left, dfs_colors)
        if node.right:
            dfs_visit(node.right, dfs_colors)

    tree = nx.DiGraph()
    pos = {}
    dfs_colors = {}
    current_color = 0
    color_step = 1 / len(tree_root.id)
    dfs_visit(tree_root, dfs_colors)  # Проведення обходу у глибину для забарвлення вузлів
    tree = add_edges(tree, tree_root, pos)
    colors = [dfs_colors[node[0]] for node in tree.nodes(data=True)]  # Використання кольорів з обходу для вузлів

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels={node[0]: node[1]['label'] for node in tree.nodes(data=True)}, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()

def draw_tree_bfs(tree_root):
    def bfs_visit(node, bfs_colors):
        nonlocal current_color
        bfs_colors[node.id] = current_color
        current_color += color_step

    tree = nx.DiGraph()
    pos = {}
    bfs_colors = {}
    current_color = 0
    color_step = 1 / len(tree_root.id)

    queue = [tree_root]
    while queue:
        node = queue.pop(0)
        bfs_visit(node, bfs_colors)  # Проведення обходу у ширину для забарвлення вузлів
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    for node_id, color in bfs_colors.items():
        tree.add_node(node_id, label=node_id)
    tree = add_edges(tree, tree_root, pos)

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels={node[0]: node[1]['label'] for node in tree.nodes(data=True)}, arrows=False,
            node_size=2500, node_color=list(bfs_colors.values()))
    plt.show()

# Створення дерева
root = Node(0)
root.left = Node(1)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)

# Відображення дерева з обходом у глибину
draw_tree_dfs(root)

# Відображення дерева з обходом у ширину
draw_tree_bfs(root)
