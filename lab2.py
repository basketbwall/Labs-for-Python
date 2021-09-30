Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
#step a create the lists

ids = []
scores = []
grades =[]

#step b take in inputs and add them to list
id = eval(input("Enter an id or press 0 to stop:"))
while id != 0:
  ids.append(id)
  score = eval(input("Enter a score:"))
  if 100.0 >= score >= 0.0:
    scores.append(score)
    id = eval(input("Enter an id or press 0 to stop:"))
  else:
    print("That's not a valid score")
else:
  print("Grades shall now be assigned.")

#step c take the average
average = sum(scores) / float(len(scores))

#step d assign grades
for score in scores:
  if score > average + 10:
    grades.append("A")
  elif score > average + 5  and score <= average + 10:
    grades.append("B")
  elif score > average - 5 and score <= average + 5:
    grades.append("C")
  elif score > average - 10 and score <= average - 5:
    grades.append("D")
  else:
    grades.append("F")

#step e print result
for i in range(len(scores)):
  print("Id:", ids[i], "Score:", scores[i], "Grade:", grades[i])
  i = i - 1
