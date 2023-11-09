import sys

number = int(sys.argv[1])

for i in range(1, number + 1):  # loop between 1 and number
    if number % i == 0: # check if remainder is 0
        print(i, end=" ")
print()