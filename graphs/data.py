import networkx as nx
import matplotlib.pyplot as plt

eropa_positions = {
    'Oradea': (0.15, 0.95), 'Zerind': (0.07, 0.84), 'Arad': (0.05, 0.72),
    'Sibiu': (0.3, 0.7), 'Fagaras': (0.5, 0.65), 'Pitesti': (0.55, 0.45),
    'Lugoj': (0.17, 0.38), 'Mehadia': (0.23, 0.25), 'Drobeta': (0.22, 0.08),
    'Crainova': (0.46, 0.10), 'Bucharest': (0.70, 0.39), 'Hirsova': (0.96, 0.45),
    'Eforie': (0.99, 0.2), 'Neamt': (0.60, 0.93), 'Iasi': (0.81, 0.91),
    'Vaslui': (0.88, 0.75), 'Timisoara': (0.032, 0.47), 'Rimnicu Vilcea': (0.35, 0.55),
    'Giurgiu': (0.65, 0.2), 'Urziceni': (0.82, 0.45)
}

jawa_positions = {
    'Jakarta': (0.05, 0.60), 'Bandung': (0.25, 0.45), 'Cirebon': (0.33, 0.57),
    'Yogyakarta': (0.54, 0.42), 'Semarang': (0.59, 0.59), 'Surabaya': (0.95, 0.60),
    'Malang': (0.9, 0.45), 'Surakarta': (0.68, 0.48)
}

eropa_edges = [
    ('Oradea', 'Zerind'), ('Oradea', 'Sibiu'),
    ('Zerind', 'Arad'),
    ('Arad', 'Sibiu'), ('Arad', 'Timisoara'),
    ('Sibiu', 'Fagaras'), ('Sibiu', 'Rimnicu Vilcea'),
    ('Fagaras', 'Bucharest'),
    ('Bucharest', 'Urziceni'),
    ('Urziceni', 'Hirsova'), ('Urziceni', 'Vaslui'),
    ('Vaslui', 'Iasi'),
    ('Iasi', 'Neamt'),
    ('Hirsova', 'Eforie'),
    ('Timisoara', 'Lugoj'),
    ('Lugoj', 'Mehadia'),
    ('Mehadia', 'Drobeta'),
    ('Drobeta', 'Crainova'),
    ('Crainova', 'Pitesti'), ('Crainova', 'Rimnicu Vilcea'),
    ('Pitesti', 'Bucharest'),
    ('Giurgiu', 'Bucharest'),
    ('Rimnicu Vilcea', 'Pitesti'),
]

jawa_edges = [
    ('Jakarta', 'Bandung'), ('Jakarta', 'Cirebon'),
    ('Bandung', 'Cirebon'), ('Bandung', 'Yogyakarta'),
    ('Cirebon', 'Semarang'), ('Cirebon', 'Yogyakarta'),
    ('Semarang', 'Yogyakarta'), ('Semarang', 'Surakarta'), ('Semarang', 'Surabaya'),
    ('Yogyakarta', 'Surakarta'),
    ('Surakarta', 'Malang'),
    ('Surabaya', 'Malang')
]

G_eropa = nx.Graph()
G_jawa = nx.Graph()

G_eropa.add_edges_from(eropa_edges)
G_jawa.add_edges_from(jawa_edges)

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
nx.draw(G_eropa, pos=eropa_positions, with_labels=True, node_size=500, node_color='lightblue', font_size=8)
plt.title("Eropa Map")

plt.subplot(1, 2, 2)
nx.draw(G_jawa, pos=jawa_positions, with_labels=True, node_size=500, node_color='lightgreen', font_size=8)
plt.title("Jawa Map")

plt.tight_layout()
plt.show()
