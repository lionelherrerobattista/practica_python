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




