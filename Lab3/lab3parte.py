Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#parte
import random
horsenames = [] #assigns each horse a number name

name = str(input("Enter a name or xxx to stop:"))

while name != 'xxx':
  horsenames.append(name)
  name = str(input("Enter a name or xxx to stop:"))
else:
  print("Race will now begin")
  numhorses = [0] * len(horsenames) #number of elements will be the same as # horses
  distances = [0] * len(horsenames) #each element keeps track of 1 horse's position
  seconds = [0] * len(horsenames) #akeeps track of how many seconds elapsed

while max(distances) <= 10560: #runs until 1 or more reach finish line distance
  for x in range(len(numhorses)): #for every element in numhorses, update the distance of each
    distances[x] += random.randrange(4,41) #random num miles each horse travels
    seconds[x] += 1 #counter to 
    if seconds[x] % 10 == 0: #if it isnt divisible by 10 don't print
      print("Name:", horsenames[x], seconds[x], "Seconds", distances[x], "Feet")
      
for x in range(len(distances)):
  print("Name:", horsenames[x], seconds[x], "Seconds", distances[x], "Feet")

print(horsenames[distances.index(max(distances))], "is the winner!")
# takes the largest distance inside the list "distances" and gives the position of it, that position we add 1
