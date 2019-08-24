import random
import string

print("How many random email & password combos would you like?")

amount = int(input("Insert amount here:"))

for i in range(amount):
    names = open("names_and_things.txt").read().splitlines()

    random_name = random.choice(names).strip()

    numbers = random.randint(49, 293238)

    email = random_name + str(numbers) + "@gmail.com"

    characters = string.ascii_letters + string.digits + "$@#%&^*()"

    password = "".join(random.choice(characters)for i in range(15))

    print(email,password)

