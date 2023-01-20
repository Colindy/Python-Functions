prompt = "What's your name? "


def greet_user(username):
    # Display a simple greeting
    if username.title() == "Emily":
        print("Hello, Dumbass.  Jk, we <3 you!")
    else:
        print (f"Hello, {username}!")

greet_user(input(prompt))
