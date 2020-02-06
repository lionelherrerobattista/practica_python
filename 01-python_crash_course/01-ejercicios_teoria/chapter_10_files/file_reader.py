# Reading all the contents:
# ~ with open('pi_digits.txt') as file_object:
    # ~ contents = file_object.read()
    # ~ print(contents.rstrip())

# Reading one line at a time:
# ~ filename = 'pi_digits.txt'

# ~ with open(filename) as file_object:
    # ~ for line in file_object: #una línea a la vez
        # ~ print(line.rstrip())
        
#Storing lines in a list:
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# ~ for line in lines: #una línea a la vez
    # ~ print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))
