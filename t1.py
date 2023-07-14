from turtle import *

speed('slowest')
pencolor('red')
for i in range(10,0,-1):
    fd(90)
    rt(360/10)
    dot(10, 'green')
    write(i, font=('Calibri', 20, 'bold'))

goto(100,100)
for i in range(10,0,-1):
    fd(90)
    lt(360/10)
    dot(10, 'green')
    write(i, font=('Calibri', 20, 'bold'))

mainloop()
