import turtle
import math 

########### Your Code here ##############
# You should only have functions here
# If you have anything outside of a function, 
# then you do not fully understand functions
# and should review how they work or ask for help

def drawSineCurve(turtle):
	turtle.up()
	turtle.goto(0,0)
	turtle.down()
	for i in range(-360,361):
		y= math.sin(math.radians(i))
		turtle.goto(i,y)


def setupWindow(window_screen):
	window_screen.setworldcoordinates(-360, -1,360, 1)
	window_screen.bgcolor("yellow")

def setupAxis(axis_object):
	axis_object.up()	
	axis_object.goto(-360,0)
	axis_object.down()
	axis_object.goto(360,0)
	axis_object.goto(0,0)
	axis_object.goto(0,1)
	axis_object.goto(0,-1)


def drawCosineCurve(manny):
	manny.up()
	manny.goto(-360,math.cos(math.radians(-360)))
	manny.down()
	for j in range(-360,361):
		y= math.cos(math.radians(j))
		manny.goto(j,y)

def drawTangentCurve(sid):
	sid.up()	
	sid.goto(0,0)
	sid.down()
	for k in range(-360,361):
		y= math.tan(math.radians(k))
		sid.goto(k,y)

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    
    
    wn.exitonclick()
main()
