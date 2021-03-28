name = input("Name of volunteer? ")
age = int(input("Age? "))
type = input("Type of volunteer ('F/P/E/T'): ")
type = type.lower()
while check != False:
    if type == "f" or type == "p" or type == "e" or type == "t":
        check = False
    elif type != "f" or type != "p" or type != "e" or type != "t":
        print("Invalid type! Please enter again!")
        type = input("Type of volunteer ('F/P/E/T'): ")

hourCont = int(input("Contribution hour? "))
while hourCont <= 0:
    print("Invalid value! Please enter again!")
    hourCont = int(input("Contribution hour? "))

newGroup.addVolunteer(volunteer(name, age, type, hourCont))
print("... Volunteer has been added successfully.")