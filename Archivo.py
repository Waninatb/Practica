from tkinter import CENTER
import turtle 
import time
pen = turtle.Turtle() 
  
def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 
  
def heart(): 
  
    pen.fillcolor('red') 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120)
    curve() 
    pen.forward(112)    
    pen.end_fill() 
  
def txt(): 
  
    pen.up() 
    pen.setpos(-48, 95) 
    pen.down() 
    pen.color('White') 
    pen.write("Widinson y Naty",align="left" , font=("Arial Black", 13, "bold")) 
  
heart() 
  
txt() 
time.sleep(20)  
pen.ht() 