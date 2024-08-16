# setup.py
from owlready2 import get_ontology, Thing, ObjectProperty

def initialize_ontology():
    onto = get_ontology("http://example.org/software.owl")
    return onto

def define_basic_classes(onto):
    with onto:
        # Define basic classes
        class SoftwareModule(Thing):
            pass

        class Function(Thing):
            pass

        # Define basic relationships
        class hasDependency(ObjectProperty):
            domain = [SoftwareModule]
            range = [SoftwareModule]
    return onto
