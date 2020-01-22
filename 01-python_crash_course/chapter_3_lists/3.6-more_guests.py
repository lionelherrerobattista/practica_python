guest_list = []
guest_list.append('juan')
guest_list.append('maria')
guest_list.append('julia')

print("Hola " + guest_list[0].title() + " te invito a la cena.")
print("Hola " + guest_list[1].title() + " te invito a la cena.")
print("Hola " + guest_list[2].title() + " te invito a la cena.")

absent_guest = 'juan'
print("\nCan't make it: " + absent_guest.title())
# replace absent guest:
guest_list[0] = 'matías'

print("\nHola " + guest_list[0].title() + " te invito a la cena.")
print("Hola " + guest_list[1].title() + " te invito a la cena.")
print("Hola " + guest_list[2].title() + " te invito a la cena.")

print("\nI've found a bigger dinner table!")
guest_list.insert(0,'lucas')
guest_list.insert(2,'laura')
guest_list.append('nicolás')

print("\nHola " + guest_list[0].title() + " te invito a la cena.")
print("Hola " + guest_list[1].title() + " te invito a la cena.")
print("Hola " + guest_list[2].title() + " te invito a la cena.")
print("Hola " + guest_list[3].title() + " te invito a la cena.")
print("Hola " + guest_list[4].title() + " te invito a la cena.")
print("Hola " + guest_list[5].title() + " te invito a la cena.")
