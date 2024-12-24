from turtle import *
import colorsys
import time

speed(0)  
bgcolor("black") 


h = 0 
penup()
goto(0, 0)
pendown()
pensize(3)  

for _ in range(100):  
    color(colorsys.hsv_to_rgb(h, 1, 1))  
    h += 0.005  

    penup()
    goto(-100, 50)
    pendown()
    write("2", font=("Arial", 150, "bold"), align="center")
    time.sleep(0.1)
    clear()

    penup()
    goto(0, 50)
    pendown()
    write("0", font=("Arial", 150, "bold"), align="center")
    time.sleep(0.1)
    clear()

    penup()
    goto(100, 50)
    pendown()
    write("2", font=("Arial", 150, "bold"), align="center")
    time.sleep(0.1)
    clear()

    penup()
    goto(200, 50)
    pendown()
    write("5", font=("Arial", 150, "bold"), align="center")
    time.sleep(0.1)
    clear()

done()