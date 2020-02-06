from collections import OrderedDict

glossary = OrderedDict()

glossary['dictionary'] = "a collection of key-value pairs"
glossary['conditional_test'] = "evaluates if an expression is True or False"
glossary['pep_8'] = "a Python style guide"
glossary['tuple'] = "an immutable list"
glossary['list'] = "collection of items in a particular order"
glossary['set'] ="similar to a list. Each item is unique"
glossary['cross-platform'] = "runs on all major operating systems"
glossary['interpreter'] = "determines what each word in the program means"
glossary['variable'] = "holds a value"
glossary['value'] = "information associated with a variable"

for name, definition in glossary.items():
    print(name.title() + ":\n\t" + definition + ".\n")
