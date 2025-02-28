# print numbers 1 through 50
# print out "bruh" if the number is divisible by 5
# print out "momento" if the number is divisible by 7
# print out "bruh momento" if a number is divisible by both

my_numbers = range(1,51)
# for each number in the my_numbers list, print out that number
for x in my_numbers:
    if(x % 5 == 0 and x % 7 == 0):
        print("bruh momento")
    elif(x % 5 == 0):
        print("bruh")
    elif(x % 7 == 0):
        print("momento")
    else:
        print(x)