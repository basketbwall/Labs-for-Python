Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
list = ['1 partridge in a pear tree','2 turtle doves','3 french hens','4 callin$

y = eval(input('enter a number between 1 and 5:'))

x = y - 1

while -1 < x < 6:
  print(list[x])
  x = x - 1
