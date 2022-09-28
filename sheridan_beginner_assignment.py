pin = "1234"

counter = 0

while counter < 3:
    pin_a = input("Please enter your PIN: ")
    if pin_a == pin:
        print ("Your account balance is: 0. Goodbye!")
        exit()
    else:
        print ("Invalid PIN.")
        counter += 1 #add 1 to counter

print ("Account locked. The police is on its way.")
