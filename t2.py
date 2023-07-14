from turtle import *

speed('fastest')
pencolor('yellow')
bgcolor('#303030')
pensize(2)

i=250
while i>0:
    fd(i)
    lt(90)
    i -= 4
    dot(5, 'red')
    write(i, font=('Calibri', 10, 'bold'))
mainloop()