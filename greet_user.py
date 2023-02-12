# Using functions to work with lists

def greet_users(names):
    # Print a greeting to each name in a list
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['jason', 'eric', 'cindy', 'ahsoka', 'anakin']
greet_users(usernames)
