#%% 
import networkx as nx

graph = nx.Graph()

#%% add nodes

for i in range(1, 4+1):
    graph.add_node(F"n{i}")

print(graph.nodes)

#%% add edges

graph.add_edge("n1", "n2", weight=1)
graph.add_edge("n1", "n3", weight=5)
graph.add_edge("n2", "n3", weight=7)
graph.add_edge("n3", "n4", weight=8)

print(graph.edges)

#%% draw the graph

pos = nx.spring_layout(graph, seed=16)
nx.draw(graph, pos=pos, with_labels=True)

weight_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos=pos, edge_labels=weight_labels)

#%% calculate shortest paths

path_no_weight = nx.shortest_path(graph, "n2", "n4")
print(path_no_weight)

path_with_weight = nx.shortest_path(graph, "n2", "n4", weight="weight")
print(path_with_weight)

# %%
