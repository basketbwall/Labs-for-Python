Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#partd
import random

horses = eval(input("Enter number of horses:"))
horsenames = []
distances = [0] * horses
seconds = [0] * horses
numhorses = [0] * horses


while max(distances) <= 10560: #runs until 1 or more reach finish line distance
  for x in range(len(numhorses)): #for every element in numhorses, update the distance of each
    distances[x] += random.randrange(4,41) #random num miles each horse travels
    seconds[x] += 1 #counter to
    horsenames.append(x + 1)
    
for x in range(len(distances)):
  print("Horse:", horsenames[x], seconds[x], "Seconds", distances[x], "Feet")
  
print("Horse:", horsenames[distances.index(max(distances))], "Is the winner!")
