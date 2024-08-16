from owlready2 import *

# Create a new ontology
onto = get_ontology("http://example.org/software.owl")

with onto:
    # Define classes for software modules and dependencies
    class SoftwareModule(Thing):
        pass

    class Function(Thing):
        pass
    
    class hasDependency(ObjectProperty):
        domain = [SoftwareModule]
        range = [SoftwareModule]

    # Define specific software modules and their dependencies
    class Calculator(SoftwareModule):
        pass

    class Factorial(Function):
        pass

    # Define relationships between the classes
    Calculator.hasDependency.append(Factorial)
