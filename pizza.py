def make_pizza(size, *toppings):
    """Summarize the pizza we are making"""
    print(f"\nMaking a {size}-inch pizza with the following items:")
    for topping in toppings:
        print(f"- {topping}")
