# visualization.py
import matplotlib.pyplot as plt
import networkx as nx

def visualize_ontology(onto):
    G = nx.DiGraph()
    for s, p, o in onto.world.sparql("""
    SELECT ?s ?p ?o WHERE { ?s ?p ?o }
    """):
        G.add_edge(str(s), str(o), label=str(p))
    
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.show()
