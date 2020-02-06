filename = "learning_python.txt"

with open(filename) as file_object:
    # ~ contents = file_object.read()
    # ~ print(contents + "\n")
    
    # ~ for line in file_object:
        # ~ print(line.strip())
        
    lines = file_object.readlines()
    
string = ''

for line in lines:
    string += line
    
print(string)
        

