glossary = {
"function": 
"their syntax are example(), where example is the function.",
"method":
"their syntax are variable.method(), where method is the method.",
"variable":
"variables are controlled by you, like so: variable = value.",
"conditonal statement":
"either true or false.",
"list":
"a data structure to store data.",
}

for key, item in glossary.items():
    print(str(key) + ":\n\t" + str(item))