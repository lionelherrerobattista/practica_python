filenames = ['cats.txt','dogs.txt']

for filename in filenames:
    try:
        with open(filename) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        pass
    else:
        print(content + "\n")
