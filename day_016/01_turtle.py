from turtle import Turtle, Screen
import os
os.system("Xvfb :1 -screen 0 720x720x16 &")
os.environ['DISPLAY'] = ":1.0 "

# Construct new object from Turtle class
timmy = Turtle()
print(timmy)
my_screen = Screen()
print(my_screen.canvheight())