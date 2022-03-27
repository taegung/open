import turtle
import random

myturtle,tX,tY,tColor,tSize,tShape=[None]*6
newplayerTurtles=[]
playerTurtles=[]
swidth,sheight=500,500

##2019038059 윤태경##
turtle.setup(width=swidth+50,height=sheight+50)
turtle.screensize(swidth,sheight)

for i in range(0,5):
    myturtle=turtle.Turtle('turtle')
    tX=random.randrange(-swidth/2, swidth/2)
    tY = random.randrange(-sheight/2, sheight/2)
    r = random.random()
    g = random.random()
    b = random.random()
    tSize=random.randrange(1,100)/10
    playerTurtles.append([myturtle, tX, tY, r, g, b,tSize])
    
soredTurtles=sorted(playerTurtles,key=lambda x:x[6])
angle=random.randrange(0,360)
for index,tList in enumerate(soredTurtles[0:]):
    myturtle.right(angle)
    myturtle=tList[0]
    
    myturtle.color((tList[3],tList[4],tList[5]))
    myturtle.pencolor((tList[3],tList[4],tList[5]))
    myturtle.turtlesize(tList[6])
    myturtle.penup()
    if index==0:
        myturtle.goto(tList[1],tList[2])
        continue
    else:
        myturtle.goto(soredTurtles[index-1][1], soredTurtles[index-1][2])
        myturtle.pendown()
        myturtle.goto(soredTurtles[index][1], soredTurtles[index][2])
turtle.done()
    
    





