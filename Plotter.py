import matplotlib.pyplot as plt
import networkx as nx
from netgraph import EditableGraph

graph_data = [(0, 1), (1, 0)]
plot_instance = EditableGraph(graph_data, node_size=2, node_shape="s")
plt.show()
labels = plot_instance.artist_to_text_object.values()
G = nx.Graph()

# Node Label
for label in labels:
    try:
        x, y = label.get_position()
        label = label.get_text()
        plt.text(x, y, label, fontsize=10, ha='center', va='center')
    except Exception as e:
        print(f"Error placing label: {e}")

# Node Weight
for x, y in plot_instance.edge_label_artists.keys():
    try:
        label_text = plot_instance.edge_label_artists[(x, y)].get_text()
        print(f"Edge ({x}, {y}) label: {label_text}") 
        try:
            weight = int(label_text)
        except ValueError:
            weight = 0
        G.add_weighted_edges_from([(x, y, weight)])
    except Exception as e:
        print(f"Error placing label: {e}")

# NX and Plot
G.add_edges_from(plot_instance.edge_paths.keys())
pos = plot_instance.node_positions
nx.draw(G, pos=pos, node_size=500, node_color="lightblue", font_size=10, edge_color="gray", node_shape="s")
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# Save
if input("Save Graph? (y/n) : ").lower() == "y":
    file = input("Name: ")

    # Save node labels to a file
    with open(f"{file}.labels", "w") as f:
        nx.write_edgelist(G, f"{file}.edgelist")
        for label in labels:
            x, y = label.get_position()
            label = label.get_text()
            plt.text(x, y, label, fontsize=10, ha='center', va='center')
            f.write(f"{x}\t{y}\t{label}\n")

    with open(f"{file}.Pos", "w") as f:
        for node, (x, y) in plot_instance.node_positions.items():
                f.write(f"{node}\t{x}\t{y}\n")

# import networkx as nx
# import matplotlib.pyplot as plt

# def showGraph():
#     file = "Test"
#     G = nx.read_edgelist(f"{file}.edgelist")

#     # Read labels from OK_labels.txt
#     labels = {}
#     with open(f"{file}.labels") as f:
#         for line in f:
#             parts = line.strip().split('\t')
#             if len(parts) == 3:
#                 x, y, label = parts
#                 labels[label] = (float(x), float(y))

#     # Read node positions from Test.Pos
#     positions = {}
#     with open(f"{file}.Pos") as f:
#         for line in f:
#             parts = line.strip().split('\t')
#             if len(parts) == 3:
#                 node, x, y = parts
#                 positions[node] = (float(x), float(y))

#     # Draw the graph with specified positions
#     nx.draw(G, pos=positions)

#     # Display the labels
#     for label, (x, y) in labels.items():
#         plt.text(x, y, label, fontsize=10, ha='center', va='center')

#     plt.show()