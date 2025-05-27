# Band Name Generator Project

# Create a welcome message and store it in a variable.
welcome_message = '\nWelcome to the Band Name Generator!\n' \
    'Not sure what to call your Band? Well, then this will help!\n'
# Print the welcome message
print(welcome_message)

# Get the user's city name and pet name and print them
city_name = input('What is the name of the city you grew up in?\n ')
pet_name = input("What is your pet's name?\n ")

# Concatenate the 2 inputs into a single string
band_name = f'Your band name could be:\n{city_name} {pet_name}'

# print the band name
print(band_name)