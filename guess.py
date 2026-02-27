import random
number = random.randint(1,10)
# print(""number)
n = 1
while n <= 10 :
    guess = int(input("Guess a number between 1 to 10:  "))

    if guess == number:
        print("You Won!")
        break
    else:
        print("Fahhhh")
    n = n + 1

