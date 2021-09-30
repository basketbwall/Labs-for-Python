Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
def guess(): #plays 1 game of guess that requires user input
    low = 1
    high = 100
    finished = False
    count = 1
    while finished == False:
        guess = int((low+high)/2)
        print(guess)
        decision = input("Too big? >, Too small? <, Just right? = :")
        if decision == ">":
            print("too big")
            high = guess
            guess = int((low+high)/2)
            count += 1
        elif decision == "<":
            print("too small")
            low = guess + 1
            guess = int((low+high)/2)
            count += 1
        elif decision == "=":
            print("just right,", guess, "is the correct number", count, "tries.")
            finished = True
