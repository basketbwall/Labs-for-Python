Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
a = "5 golden rings"
b = "4 calling birds"
c = "3 French hens"
d = "2 tutle doves"
e = "1 partridge in a pear tree."

x = eval(input("Enter a number between 1 and 5:"))

if x == 5:
  print(a)
elif x == 4:
  print(b)
elif x == 3:
  print(c)
elif x == 2:
  print(d)
elif x == 1:
  print(e)

