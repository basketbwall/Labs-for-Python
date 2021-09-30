Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
#partc
import random
travel = []
races = []

for i in range(1000):
  while sum(travel) < 10560:
    travel.append(random.randrange(4,41))
  races.append(len(travel)) #puts time it took to complete each race in list
  travel.clear() #clears list to do a new race

average = sum(races)//1000 #takes the average of the 1,000 races

print(average, "is the average number of seconds")
