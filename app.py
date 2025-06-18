import tkinter as tk
from tkinter import ttk, messagebox
import networkx as nx
import matplotlib.pyplot as plt
from load_graph import load_graph_from_file
from bellman_ford import bellman_ford

vertices, edges = load_graph_from_file("data/test_data1.txt")
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

def run_algorithm():
    start = selected_vertex.get()
    if not start:
        messagebox.showwarning("Chyba", "Musíš zvolit počáteční vrchol.")
        return

    try:
        distances = bellman_ford(vertices, edges, start)
        result_text.delete(1.0, tk.END)
        for v in distances:
            result_text.insert(tk.END, f"{v}: {distances[v]}\n")
        draw_graph(distances)
    except ValueError as e:
        messagebox.showerror("Chyba", str(e))

def draw_graph(distances):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12, arrows=True)
    
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    
    for node, dist in distances.items():
        if dist != float('inf'):
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_color='lightgreen')

    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("Bellman-Ford GUI")

ttk.Label(root, text="Zvol počáteční vrchol:").pack(pady=5)
selected_vertex = ttk.Combobox(root, values=vertices, state="readonly")
selected_vertex.pack()

ttk.Button(root, text="Spustit algoritmus", command=run_algorithm).pack(pady=10)

result_text = tk.Text(root, height=10, width=40)
result_text.pack()

root.mainloop()