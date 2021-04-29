import turtle
import sys,time,os
import math

os.system("clear")


turtle.title("Kruz Calculator")
loadWindow = turtle.Screen()
turtle.bgcolor("black")
turtle.bgpic("ic.png")
turtle.color("white")
turtle.ht()



turtle.write("""
Note: Press 0 To Stop The Kruzcalculator \n\

Please Choose What You Want To Do \n\

1      ' Addition' \n\
2      'Subtraction' \n\
3        'Multiply' \n\
4         'Devide' \n\

............. \n\
Coded by Kruz ::::::::::::::: :::::::::::::: ::: \n\
............. \n\

""" ,align="center", font=("Courier New", 12, "bold"))

ask = int(input("What Would You Like To Do: ? "))



if ask == 1:
    turtle.clear()
    turtle.write("You Want to add ", align="center", font=("Courier New", 30, "bold"))
    time.sleep(1)
    askk = turtle.numinput("Add","Kruz says's Enter the Adding Number You Want to add ",minval=0, maxval=10000)
    asks = turtle.numinput("Add","Kruz says's Enter the Second Number You Want to add ",minval=0, maxval=10000)
    turtle.clear()
    turtle.write("Your Anser is ",align="right",font=("Courier New", 20, "bold"))
    turtle.write(askk + asks ,align="left", font=("Courier New", 20, "bold"))
    time.sleep(1)
    os.system("clear")
    os.system("python3 kru-Gui-cal.py")
elif ask == 2:
    turtle.clear()
    turtle.write("You Want to Subtract ", align="center", font=("Courier New", 30, "bold"))
    time.sleep(1)
    subb = turtle.numinput("Subtraction","Kruz says's Enter the Number You Want to Subtract ? ")
    subbb = turtle.numinput("Subtraction","Kruz says's Enter the Number The Second Number ? ")
    subtracting = subb - subbb
    turtle.clear()
    turtle.write("Your Anser is ",align="right",font=("Courier New", 20, "bold"))
    turtle.write(subb - subbb ,align="left", font=("Courier New", 20, "bold"))
    tutle.up()
    time.sleep(1)
    os.system("clear")
    os.system("python3 kru-Gui-cal.py")
elif ask == 3:
    turtle.clear()
    turtle.write("You Want to Multiply ", align="center", font=("Courier New", 30, "bold"))
    time.sleep(1)
    mul = turtle.numinput("Multiply","Kruz says's Enter the Number You Want to Multiply ")
    mull = turtle.numinput("Multiply","Kruz says's Enter the Number The Second Number")
    turtle.clear()
    turtle.write("Your Anser is ",align="right",font=("Courier New", 20, "bold"))
    turtle.write(mul * mull ,align="left", font=("Courier New", 20, "bold"))
    time.sleep(1)
    os.system("clear")
    os.system("python3 kru-Gui-cal.py")
elif ask == 4:
    turtle.clear()
    turtle.write("You Want to Devide ", align="center", font=("Courier New", 30, "bold"))
    time.sleep(1)
    div = turtle.numinput("Multiply","Kruz says's Enter the Number You Want to Devide")
    divv = turtle.numinput("Multiply","Kruz says's Enter the Number The Second Number")
    turtle.clear()
    turtle.write("Your Anser is ",align="right",font=("Courier New", 20, "bold"))
    turtle.write(div // divv ,align="left", font=("Courier New", 20, "bold"))
    time.sleep(1)
    os.system("clear")
    os.system("python3 kru-Gui-cal.py")
elif ask == 0:
    print("Bye ...!!")
    exit()
else:
    turtle.write("choose 1 bro  ", align="center", font=("Courier New", 30, "bold"))
    time.sleep(3)
    os.system("clear")
    os.system("python3 kru-Gui-cal.py")
