#11. Write a program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

for x in range(1500, 2700):
    if x % 5 == 0 and x % 7 == 0:
        print (str(x))

