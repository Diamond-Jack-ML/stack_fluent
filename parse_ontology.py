from owlready2 import *
import argparse
import json

def load_ontology(file_path):
    # Load the ontology using owlready2
    onto = get_ontology(file_path).load()
    return onto

def extract_labels(ontology):
    labels = []
    
    # Extract class names
    for cls in ontology.classes():
        labels.append(cls.name)
    
    # Extract property names
    for prop in ontology.object_properties():
        labels.append(prop.name)
    for prop in ontology.data_properties():
        labels.append(prop.name)
    
    return labels

def save_labels(labels, output_file):
    with open(output_file, 'w') as f:
        json.dump(labels, f, indent=4)
    print(f"Candidate labels saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Parse an ontology and generate candidate labels for text classification.')
    parser.add_argument('ontology_file', type=str, help='Path to the ontology file')
    parser.add_argument('--output', type=str, default='candidate_labels.json', help='Output file to save candidate labels')
    
    args = parser.parse_args()
    
    ontology = load_ontology(args.ontology_file)
    labels = extract_labels(ontology)
    save_labels(labels, args.output)

if __name__ == "__main__":
    main()
