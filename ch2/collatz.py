def collatz(number):
    if number%2 == 0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
user_value = input("Please type a valid integer: ")
try:
    number = int(user_value)
    while(number != 1): 
        number = collatz(number)
except ValueError:
    print("Sorry old chap {} isn't a valid integer, try again eh?!?".format(user_value))
