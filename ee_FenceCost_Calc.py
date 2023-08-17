def num_check(question):

    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            response = float(input(question))

            if response > 0:
                return response


            else:
                print("Please enter a number that is more than zero")
                print()


        except ValueError:
            print(error)

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    length = num_check("Length: ")
    meter = num_check("cost per meter: ")

    perimeter = 2* (width + length)
    cost = perimeter * meter

    print("The perimeter of your fence is {} ".format(perimeter))
    print("The cost over all will be {} dabloons".format(cost))

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using this calculator")



