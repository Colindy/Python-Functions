# Here I just wanted to put a bunch of different
# functions together to create a simple calculator

def add(a, b):
    total = a + b
    return total

def sub(a, b):
    total = a - b
    return total

def multi(a, b):
    total = a * b
    return total

def div(a, b):
    total = a / b
    return total

print("Hello there!  A simple calculator for you!")
print("Enter 'q' at any time to quit the program.")

while True:
    num1 = input("Give me your first number: ")
    if num1.lower() == 'q':
        break
    else:
        num1 = int(num1)
    num2 = input("Give me your second number: ")
    if num2.lower() == 'q':
        break
    else:
        num2 = int(num2)
    print("Now, what do you want to do with them?")
    out = input("Add, Subtract, Multiply, or Divide?: ")
    if out.lower() == 'q':
        break
    elif out.lower() == 'add':
        output = add(num1, num2)
        print(output)
    elif out.lower() == 'subtract':
        output = sub(num1, num2)
        print(output)
    elif out.lower() == 'multiply':
        output = multi(num1, num2)
        print(output)
    elif out.lower() == 'divide':
        output = div(num1, num2)
        print(output)
    else:
        print("I'm not sure what to do with that input")
        print("Exiting program")
        break
