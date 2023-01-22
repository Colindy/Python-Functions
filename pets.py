
def describe_pet(animal_type='dog', pet_name='buddy'):
    #Display information about a pet
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type} is named {pet_name.title()}.")

# These are positional arguments.  Based on position
describe_pet('cat', 'Benny')
describe_pet('cat', 'princess')

# These are Keyword Arguments.  Based on the keyword
describe_pet(animal_type="cat", pet_name="benny")
describe_pet(pet_name="Princess", animal_type="cat")

# With this one, I changed the arguments on the function above
# to show a 'default value' in the pet name argument.
describe_pet(animal_type='cat', pet_name='benny')
# Note that this only works because you declare the argument.
# If not, both would over-write the first argument.
describe_pet(pet_name='dufus')
describe_pet(animal_type='feret')