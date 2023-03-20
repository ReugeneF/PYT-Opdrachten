import random

player_one = input ("Hey, Whats your name?: ")
num1 = int(input("(smallest number first) Number between: "))
num2 = int(input("And: "))
if num2 < num1:
    print("Program unable to process, Try again with your glasses on this time.")
    exit()
elif num2 < 0:
    print("Program unable to process, Try again with your glasses on this time.")
    exit()
elif num1 < 0:
    print("Program unable to process, Try again with your glasses on this time.")
    exit()

randomizer = random.sample(range(num1, num2),2)
randomnum = random.choice(randomizer)

print("okay! " + player_one + " Guess a number between the numbers: " + str(num1) + " and " + str(num2))


tries = 0

while tries < 5:
    guess = int(input())
    tries += 1
    if guess < randomnum:
        print("Your guess is too low")
    if guess > randomnum:
        print("Your guess is too high")
    if tries > 5:
        print("Too many tries, Game over.")
        break
    if guess == randomnum:
        break

if guess == randomnum:
    print("You guessed the correct number, Congratz!")
else:
    print("You did not guess the correct number, Game over.")






