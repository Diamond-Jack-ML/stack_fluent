# ontology_population.py
from owlready2 import URIRef

def populate_ontology(onto, entities):
    with onto:
        for entity, entity_type in entities:
            if entity_type == "Module":
                module = URIRef(onto[entity])
                module.is_a.append(onto.SoftwareModule)
            elif entity_type == "Function":
                function = URIRef(onto[entity])
                function.is_a.append(onto.Function)
    return onto
