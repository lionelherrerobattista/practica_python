sandwich_orders = ['tuna','bacon','beef']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made your " + sandwich + " sandwich.")

    finished_sandwiches.append(sandwich)
    
# Lista de pedidos terminados:
print("\nFinished sandwiches:")
for finished_sandwich in finished_sandwiches:
    print("\t" + finished_sandwich)
    
    
