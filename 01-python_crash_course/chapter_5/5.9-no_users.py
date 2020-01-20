# ~ users = ['admin', 'juan', 'maria', 'pedro', 'laura']
users = []

if users: #si no está vacía
    for user in users:
        if user == 'admin':
            print("Hello " + user + ", would you like to see " 
                    + "a status report?")
        else:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")
