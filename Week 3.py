# Starting off
print(22/7)
print(355/113)
import math


print(9801/(2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSideS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSideS
    polygonCircumference = numSides * sideS
    pi = polygonCircumference
    return pi

print(archimedes(8))
print(archimedes(16))

for sides in range (8,100,8):
    print(sides,archimedes(sides))

# experiment with the loop above alongside the actual value of Pi.How many
# sides does it take to make the two close?

#in between two and tree

#Accumulators

acc = 0
for x in range(1,6):
    acc = acc + x

print(acc)

#compute the sum of the first 100 even numbers
acc = 2
for x in range(2,101):
    acc = acc+x
print(acc)

#compute the sum of the first 50 odd numbers
acc=2
for x in range(1,51):
    acc=acc+x
print(acc)

#compute the average of the first 100 odd numbers
acc =2
for x in range(1,101):
    acc=acc+x
print(acc/100)

# Write a function that returns the average of the first N numbers, where N is a parameter.
acc = 1
for x in range(1, 10):
    acc = acc + x
n=int(input("Input a number to compute the average of all numbers leading up to it : "))

# Write a function called factorial that computes the product of the first N numbers, where N is a parameter.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Input a number to compute the factorial : "))
print(factorial(n))


#You may assume that N will be greater than or equal to 3
#AVERAGE=83.33

# A Monte Carlo Simulation

import random

print(random.random())

# Boolean expressions
#> greater than
# >=grater than or equal to
# < less than
# <= less than or equal to
# == the same as [equal to]           # comparing 2 things use 2
#! Not equal to

dogWeight = 25
print(dogWeight != 25)
catWeight = 15

#coumpound boolean operaters
#and
#or
#not

print(dogWeight < 30 or catWeight < 20)  #False= not, Or lighten load


#Desicion Making -- Selection Statements
a=5
b=10
c=75

if a > b :
    c=45

print(c)

if a > b :
    c=45
    if b>c:


     c = 1050
    if b==a:
        c=25

print(a,b,c)


d = 55
e = 72
f = 44
ans = 0


if d>e:
    ans=12

if d==e:
    ans=50
else:
    if f>d * e:
        ans =100
    else:
        ans=75
print(ans)

def montePi(numDarts):

    inCircle = 0


    for i in range(numDarts):
          x = random.random()
          y = random.random()

          distance = math.sqrt(x**2+ y**2)


    if distance<= 1:
        inCircle = inCircle + 1

    pi = inCircle / numDarts*4
    return pi

print(montePi(42425644))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    bb = turtle.Turtle()


    scn.set1dcoordinates(-2,-2,2,2)

    bb.penup()
    bb.goto(-1,0)
    bb.pendown()
    bb.goto(1,0)

    bb.penup()
    bb.goto(0,1)
    bb.pendown()
    bb.goto(0,-1)

    inCircle=0
    bb.penup()

    for i in range(numDarts):
        x = -1. + 2..random()
        y = -1. + 2..random()

        distance = math.sqrt(x**2 + y**2)

        bb.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            bb.color("blue")
        else:
            bb.color("red")

        bb.dot()

    pi = inCircle / numDarts*4
    scn.exitonclick()
    return pi

    showMontePi(1000)







