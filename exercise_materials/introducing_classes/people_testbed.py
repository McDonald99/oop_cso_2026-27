from people import Person

person_one = Person()

print(f"Person's name: {person_one.f_name} {person_one.l_name}")

if person_one.left_handed == True:
    print(f"Person's name: {person_one.f_name} {person_one.l_name}")

else:
    print(f"Person's name: {person_one.f_name.upper()} {person_one.l_name.upper()}")


person_two = Person()

person_two.f_name = input("Enter your first name: ")
person_two.l_name = input("Enter your last name: ")
person_two.age = input("Enter your age: ")
person_two.left_handed = input("Are you left-handed? (y/Y for yes, any other key for no): ")

if person_two.left_handed.lower() == "y":
    person_two.left_handed = True
else:
    person_two.left_handed = False

if person_two.left_handed:
    print(f"Person's name: {person_two.f_name} {person_two.l_name}")

else:
    print(f"Person's name: {person_two.f_name.upper()} {person_two.l_name.upper()}")