def make_pizza(*toppings):
    """Summarize the pizza we are making"""
    print("\nMaking a pizza with the following items:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('sausage', 'mushroom', 'extra cheese')
