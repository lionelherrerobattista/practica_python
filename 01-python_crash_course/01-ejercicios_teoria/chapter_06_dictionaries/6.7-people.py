person_1 = {
    'first_name':'lionel',
    'last_name':'herrero',
    'age':31,
    'city':'buenos aires',
    }
    
person_2 = {
    'first_name':'lionel',
    'last_name':'messi',
    'age':32,
    'city':'barcelona',
    }
    
person_3 = {
    'first_name':'cristiano',
    'last_name':'ronaldo',
    'age':34,
    'city':'turín',
    }

people = [person_1, person_2, person_3]

for person in people:
    full_name = person['first_name'] + " " + person['last_name']
    age = person['age']
    city = person['city']
    
    print("Full name: " + full_name.title())
    print("Age: " + str(age))
    print("City: " + city.title() + "\n")
    
