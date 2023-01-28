# Making a function return a value

def get_formated_name(fname, lname, mname=''):
    """Return a formated name"""
    if mname:
        full_name=f"{fname} {mname} {lname}"
    else:
        full_name = f"{fname} {lname}"
    return full_name.title()

badass = get_formated_name('ahsoka', 'tano')
print(badass)
musician = get_formated_name('james', 'keenan', 'herbert')
print(musician)

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name == 'q':
        break
    l_name = input("Last Name: ")
    if l_name == 'q':
        break

    formatted_name = get_formated_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")
