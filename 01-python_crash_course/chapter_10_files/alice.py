filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exist."
    print(msg)
else:
    #Count the approximate number of words in the file.
    words = contents.split() #divide el texto en palabras y los guarda en una lista
    num_words = len(words)
    print("The file " + filename + " has about " + str(num_words) + " words.")
