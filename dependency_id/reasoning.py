# reasoning.py
from owlready2 import sync_reasoner_pellet

def run_reasoner(onto):
    sync_reasoner_pellet([onto], infer_property_values=True, debug=1)
    return onto
