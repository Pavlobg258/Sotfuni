


numbers = input("Enter a list of numbers separated by spaces: ").split()

numeric_numbers = []
non_numeric_elements = []

for num in numbers: # checks if its a nmber orno
    if num.isdigit():
        numeric_numbers.append(int(num))
    else:
        non_numeric_elements.append(num)

if numeric_numbers: # compares it for the biggest
    maximum = numeric_numbers[0]

    for num in numeric_numbers:
        if num > maximum:
            maximum = num

    print("The maximum number is:", maximum)

if non_numeric_elements:
    print("Non-numeric elements in the list:", non_numeric_elements)
    print("You're a cheating guy, no , APICEOF SHIFT for adding non-numeric strings!")


