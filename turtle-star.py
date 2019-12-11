# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 15:41:54 2019

@author: 可欣
"""

# coding=utf-8
import turtle
import time
 
turtle.pensize(5)
turtle.pencolor("yellow")
turtle.fillcolor("red")
 # 返回或设置画笔填充颜色(设置后海龟箭头内部填充也是这个颜色)
turtle.begin_fill()
for _ in range(5):
  turtle.forward(200)
  turtle.right(144)
turtle.end_fill()
time.sleep(2)
 
turtle.penup()
turtle.goto(-150,-120)
turtle.color("purple")
turtle.write("画好啦", font=('Arial', 40, 'normal'))
 
turtle.mainloop()
