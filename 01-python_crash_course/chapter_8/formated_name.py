def get_formatted_name(first_name, last_name, middle_name=''): #valor opcional
    """Return a full name, neatly formatted."""
    if middle_name: # si no está vacía es True
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
