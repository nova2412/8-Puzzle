#!/usr/bin/env python
# coding: utf-8

# In[19]:


from tkinter import *
from tkinter import messagebox
from functools import partial
#from random import randint

#messagebox.showinfo('Thông báo','Chúc mừng bạn đã hoàn thành')
#btn = Button(window, text="New")
#btn.grid(column=1, row=0)
#btn = Button(window, text="Help")
#btn.grid(column=2, row=0)
def click_mouse(value,buttons):
    if value==0:
        if (buttons[1].cget('text')=='  '):
            buttons[1].config(text= buttons[0].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[3].cget('text')=='  '):
            buttons[3].config(text= buttons[0].cget('text'))
            buttons[value].config(text = '  ')
    if value==1:
        if (buttons[0].cget('text')=='  '):
            buttons[0].config(text= buttons[1].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[2].cget('text')=='  '):
            buttons[2].config(text= buttons[1].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[4].cget('text')=='  '):
            buttons[4].config(text= buttons[1].cget('text'))
            buttons[value].config(text = '  ')
    if value==2:
        if (buttons[1].cget('text')=='  '):
            buttons[1].config(text= buttons[2].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[5].cget('text')=='  '):
            buttons[5].config(text= buttons[2].cget('text'))
            buttons[value].config(text = '  ')
    if value==3:
        if (buttons[4].cget('text')=='  '):
            buttons[4].config(text= buttons[3].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[0].cget('text')=='  '):
            buttons[0].config(text= buttons[3].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[6].cget('text')=='  '):
            buttons[6].config(text= buttons[3].cget('text'))
            buttons[value].config(text = '  ')
    if value==4:
        if (buttons[1].cget('text')=='  '):
            buttons[1].config(text= buttons[4].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[3].cget('text')=='  '):
            buttons[3].config(text= buttons[4].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[5].cget('text')=='  '):
            buttons[5].config(text= buttons[4].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[7].cget('text')=='  '):
            buttons[7].config(text= buttons[4].cget('text'))
            buttons[value].config(text = '  ')
    if value==5:
        if (buttons[2].cget('text')=='  '):
            buttons[2].config(text= buttons[5].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[4].cget('text')=='  '):
            buttons[4].config(text= buttons[5].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[8].cget('text')=='  '):
            buttons[8].config(text= buttons[5].cget('text'))
            buttons[value].config(text = '  ')
    if value==6:
        if (buttons[3].cget('text')=='  '):
            buttons[3].config(text= buttons[6].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[7].cget('text')=='  '):
            buttons[7].config(text= buttons[6].cget('text'))
            buttons[value].config(text = '  ')
    if value==7:
        if (buttons[4].cget('text')=='  '):
            buttons[4].config(text= buttons[7].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[6].cget('text')=='  '):
            buttons[6].config(text= buttons[7].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[8].cget('text')=='  '):
            buttons[8].config(text= buttons[7].cget('text'))
            buttons[value].config(text = '  ')
    if value==8:
        if (buttons[5].cget('text')=='  '):
            buttons[5].config(text= buttons[8].cget('text'))
            buttons[value].config(text = '  ')
        elif (buttons[7].cget('text')=='  '):
            buttons[7].config(text= buttons[8].cget('text'))
            buttons[value].config(text = '  ')
    win(buttons)     

def add_Button(window,numbers):
    row=0
    buttons = []
    for i in range(9):
        if i != 0 and i % 3 == 0:
                row += 1
        button = Button(window,text = numbers[i], font = ('arial', 25, 'bold'))
        button.grid(row = row, column = i % 3)
        buttons.append(button) 
    for i in range(9):
        buttons[i].config(command = partial(click_mouse, i, buttons))
def win(buttons):
    list=[]
    for i in range(9):
        list.append(buttons[i].cget('text'))
    if (list==['  ', 1, 2,3,4,5,6,7,8]):
        messagebox.showinfo('Thông báo','Chúc mừng bạn đã hoàn thành')
        
def start_game():
    window = Tk()
    numbers = [3, 1, 2, 6,'  ',8,7,5,4];
    window.title("Puzzle")
    window.geometry('300x300')
    add_Button(window,numbers)
    window.mainloop()
#if __name__ == '__main__':
start_game()





