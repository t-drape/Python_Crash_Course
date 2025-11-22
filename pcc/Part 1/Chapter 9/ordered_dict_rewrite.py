from collections import OrderedDict

glossary = OrderedDict()

glossary["dictionary"] = "another data structure to store data."
glossary["string"] = "list of characters."
glossary["integer"] = "a whole number."
glossary["float"] = "a decimal number."
glossary["character"] = "a letter is an example of a character."

for key, item in glossary.items():
    print(str(key) + ":\n\t" + str(item))