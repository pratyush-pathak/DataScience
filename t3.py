from turtle import *
speed('fastest')
colors = ['red','yellow','blue','green']
pensize(2)
i = 0
while True:
 
  # print(i%4, colors[i%4])
     pencolor(colors[i%4])
     fd(i*2)
     lt(60)
     i += 1
mainloop()

