import random
print('Sys: I am thinking of a number!')
Number = random.randint(1,15)
attempts=0
while True:
    Guess = int(input("Guess a number: "))
    attempts+=1
    if Guess==Number:
        print(f'congrats! you have guessed the number in {attempts} attempts')
        break
    elif Guess<Number:
        print('Sys:Try for a higher number')
    else:
        print('Sys:Try for a lower number')