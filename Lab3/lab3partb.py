Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#finds the number of seconds until a horse crosses the finish line
import random
travel = [] # list that will store the distance traveled each second

while sum(travel) < 10560: #loop stops when horse has crossed 2 miles
  travel.append(random.randrange(4,41)) #horse can run at most 40ft/s
print(len(travel), 'seconds to finish the race') #prints the output
