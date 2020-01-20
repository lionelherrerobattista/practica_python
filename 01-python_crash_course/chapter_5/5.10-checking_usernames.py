current_users = ['juan123', 'maria123', 'pablo123', 'laura123', 'jose123']
new_users = ['JUAN123', 'maria123', 'pedro123', 'julia123', 'mmatias']

for user in new_users:
    if user.lower() in current_users: #si está en la lista, case insensitive
        print("Nombre de usuario ya utilizado. Debe ingresar uno nuevo.")
    else:
        print("El nombre de usuario está disponible.")
