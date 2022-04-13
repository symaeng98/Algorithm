import turtle
import random

##함수 선언 부분##
def ScreenLeftClick(x,y):
    global r,g,b
    global angle
    turtle.penup()
    turtle.goto(x,y)
    r= random.random()
    g= random.random()
    b= random.random()
    angle= random.randrange(0,360)
    turtle.right(angle)
    turtle.color(r,g,b)
    tSize=random.randrange(1,10)
    turtle.shapesize(tSize)
    turtle.stamp()

##변수 선언 부분##
r,g,b= 0.0,0.0,0.0

##메인 코드 부분##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.onscreenclick(ScreenLeftClick,1)
    
turtle.done()
