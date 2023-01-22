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
