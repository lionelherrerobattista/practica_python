filenames = ["huckleberry_finn.txt", "alice.txt"]

for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print("File not found!")
    else:
        repetitions = content.lower().count('the')
        print("Times 'the' appears in " + filename + ": " + str(repetitions))
