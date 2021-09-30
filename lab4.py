Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 23:26:24) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> 
import math

def vert(k, n): #gives the kth vertex of n sides
    x = math.cos(2*math.pi*k/n)
    y = math.sin(2*math.pi*k/n)
    return (x, y)

def vertices(n): #appends all the vertices to a list
    verts = []
    for i in range(n):
        verts.append(vert(i, n))
    return verts

def dist(p1, p2): #calculates distance between 2 points
    distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    return distance

def perimeter(i): #calculates perimeter
    peri = 0
    for x in range(len(i) - 1): #range must be smaller to avoid list index error, the next line will access +1 of each element
        peri += dist(i[x], i[x+1]) #calculates distance of each 2 points left to right until the second last one
    peri += dist(i[-1], i[0]) #calculates the last to the first point
    return peri

def heron(p1, p2, p3): #standard heron formula
    p = (p1 + p2 + p3)/2.0
    area = (p * (p-p1) * (p-p2) * (p-p3)) ** 0.5
    return area

def area(x): #finds the area by using dist() to find side lengths first
    p1 = dist((0,0), x[0]) #first point from origin
    p2 = dist((0,0), x[1]) #second point from origin
    p3 = dist(x[0], x[1]) #first point to second point
    area = (heron(p1, p2, p3) * len(x)) 
    return area

def main():
    for z in range(3, 1004, 100): #will start at 3, increase by 100, end at 1003 since the range is 1004)
        print(z, perimeter(vertices(z)), area(vertices(z)), perimeter(vertices(z))**2/(4.0*area(vertices(z))))
main()

