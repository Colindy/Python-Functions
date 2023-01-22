# Using a function to build a dictionary entry

def build_person(fname, lname, age=None):
    # Return a dictionary of information about a person
    person = {'first': fname, 'last': lname}
    if age:
        person['age'] = age
    return person

fulcrum = build_person('ahsoka', 'tano', age=27)
print(fulcrum)
