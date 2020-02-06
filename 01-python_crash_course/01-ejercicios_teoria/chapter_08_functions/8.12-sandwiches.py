def order_sandwich(*ingredients):
    print("\nSandwich ordered:")
    for ingredient in ingredients:
        print("- " + ingredient)
        
order_sandwich('sausage')
order_sandwich('bacon', 'salmon')
order_sandwich('beef steak', 'pineapple', 'cheese')
