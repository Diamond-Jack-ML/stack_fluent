# main.py
from setup import initialize_ontology, define_basic_classes
from entity_extraction import extract_entities
from ontology_population import populate_ontology
from reasoning import run_reasoner
from visualization import visualize_ontology

def main():
    # Initialize ontology
    onto = initialize_ontology()
    onto = define_basic_classes(onto)
    
    # Extract entities from documentation
    sample_text = """
    The Calculator module contains methods for add, subtract, multiply, and divide.
    The factorial function is used recursively and depends on the math library.
    """
    entities = extract_entities(sample_text)
    
    # Populate ontology with extracted entities
    onto = populate_ontology(onto, entities)
    
    # Apply reasoning
    onto = run_reasoner(onto)
    
    # Visualize the ontology
    visualize_ontology(onto)

if __name__ == "__main__":
    main()
