# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)

        # Main Routine goes here


# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":
    # call your number checker function three times to get the
    # width, length and cost_per_m of the fencing

    width = num_check("Width: ")
    height = num_check("Height: ")
    cost_per_meter = num_check("Cost: ")

    area = width * height

    perimeter = 2 * (width + height)

    price = (perimeter * cost_per_meter)

    print(f"Perimeter: {perimeter:.2f} meters")
    print(f"area: {area:.2f} meters")
    print(f"Price: {price:.2f} dollars")
    print()

    # Calculate the cost of the fencing (perimeter x cost_per_m)

    # Output the perimeter and cost of the fencing

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the Fencing cost calculator")
print()
