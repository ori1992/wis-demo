# OrI Berman

import random

print("Lets start the game!")
start_range = int(input("lowest random number you would like to encounter:"))
end_range = int(input("highest random number you would like to encounter:"))
number_of_attempts = int(input("how many attempts would you like:"))
operator = int(input("what operator would you like to excrexis:\n for '+' dail 1\n for '-' dial 2 \n for '*' dial 3\n for '/' dial 4\n"))
a = random.randrange(start_range, end_range)
b = random.randrange(start_range, end_range)

if operator == 1: 
    for _ in range(0, number_of_attempts):
        result = input(f"How much is {a} + {b}? ")
        if a + b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")

elif operator == 2: 
    for _ in range(0, number_of_attempts):
        result = input(f"How much is {a} - {b}? ")
        if a - b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")

elif operator == 3: 
    for _ in range(0, number_of_attempts):
        result = input(f"How much is {a} * {b}? ")
        if a * b == int(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")

elif operator == 4: 
    dec = int(input("how precise would you like to be after the decimal point:"))
    da = float(a)
    db = float(b)
    ans = round(da/db, dec)
    for _ in range(0, number_of_attempts):
        result = input(f"How much is {a} / {b}? ")
        if ans == float(result):
            print(f"Indeed {result} is the correct number")
            break
        else:
            print("Incorrect")

print("done")
