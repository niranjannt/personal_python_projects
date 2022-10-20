import math
from trianglesolver import solve, degree
triangle_type=input("What is the type of triangle. Type N for AAS. Type L for SSS. Type R for ASA.")
if triangle_type=="L":
    a=input("What is the first side?")
    b=input("What is the second side?")
    c=input("What is the third side?")
    a,b,c,A,B,C = solve(float(a), float(b), float(c))
    print("Angle B is:"+" " + str(round(B / degree))+" "+"degrees"+" " +"Angle A is:"+" " +str(round(A/degree))+" "+"degrees"+" " +"Angle C is:"+" " +str(round(C/degree))+" " +"degrees"+" ")

if triangle_type=="R":
    d=input("What is the first angle?")
    e=input("What is the second side?")
    f=input("What is the third angle?")
    a,b,c,A,B,C = solve(A=int(d)*degree, b=int(e), C=int(f)*degree)
    print("Angle B is:"+" " + str(round(math.degrees(B)))+" "+"degrees"+" " +"Side A is:"+" " +str(round(a, 2))+" " +" " +"Side C is:"+" " +str(round(c,2)))

if triangle_type=="N":
    g=input("What is the first angle?")
    h=input("What is the first side?")
    i=input("What is the second side?")
    a,b,c,A,B,C = solve(A=float(g)*degree, b=float(h), c=float(i))
    print("Side A is:" + " " + str(round(a, 2))+ " " + "Angle B is:" + " "+ str(round(math.degrees(B)))+" " +"degrees"+" " +"Angle C is:"+ " "+ str(round(math.degrees(C)))+" "+"degrees")
