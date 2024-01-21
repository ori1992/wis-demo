import random

AA = random.randrange(1,20)
b = random.randrange(1,20)

for seq in range (1,3):
    result = input(f"how much is {AA} + {b}?")
    if AA+b == int(result):
        print(f"indeed {result} is the correct answer")
        break
    else:
        print("incorrect")
        
print("Done")