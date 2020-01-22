users = ['admin', 'juan', 'maria', 'pedro', 'laura']

for user in users:
    if user == 'admin':
        print("Hello " + user + ", would you like to see " 
                + "a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")
