def num_check(question):
    error = "Please enter a number that is more than zero"

    while True:
        try:
            response = float(input(question))

            if response > 0:
                return response

            else:
                print(error)
                print()

        except ValueError:
            print(error)

print()
print("**** Area Perimeter Calculator ****")
print()

keep_going = ""
while keep_going == "":

    width = num_check("Width: ")
    print("width", width)

    height = num_check("Height: ")

    area = width * height

    perimeter = 2 * (width + height)

    print(f"Perimeter: {perimeter:.2f} units")
    print(f"Area: {area:.2f} square units")
    print()

    keep_going = input("Press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")


