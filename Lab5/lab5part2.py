Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
import random

def guess(x): #plays x many games of guess, doesn't need user input
    times = 0
    avg = []
    while times != x:
        low = 1
        high = 100
        finished = False
        count = 1
        answer = random.randrange(1, 101)
        while finished == False:
            guess = int((low+high)/2)
            print(guess)
            if guess > answer:
                print("too big")
                high = guess
                guess = int((low+high)/2)
                count += 1
            elif guess < answer:
                print("too small")
                low = guess + 1
                guess = int((low+high)/2)
                count += 1
            elif guess == answer:
                print("just right,", guess, "is the correct number", count, "tries.")
                finished = True
                avg.append(count)
        times += 1
    print("")
    print('The average number of guesses for', x, 'games is', sum(avg)/x)
    print('here are the list of averages', avg)


     
