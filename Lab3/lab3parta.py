Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#this program appends to a list 1000 numbers and prints the average
import random

nums = []

for i in range(1000):
  nums.append(random.randrange(10,21))
  
print(sum(nums)//1000)
