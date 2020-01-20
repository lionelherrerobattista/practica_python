sandwich_orders = ['pastrami','tuna','pastrami','bacon','pastrami','beef']
finished_sandwiches = []

print("We ran out of pastrami.\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")

    finished_sandwiches.append(sandwich)
    
# Lista de pedidos terminados:
print("\nFinished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
    
