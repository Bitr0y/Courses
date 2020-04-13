from tkinter import *


class Block:
    lis = ['+', '-', '*', '/']

    def __init__(self, master):
        self.f_top = Frame()
        self.f_bot = Frame()
        self.e = Entry(master, width=20)
        self.g = Entry(master, width=20)
        self.but_sum = Button(self.f_top, text=self.lis[0], width=5)
        self.but_minus = Button(self.f_top, text=self.lis[1], width=5)
        self.but_umnoz = Button(self.f_bot, text=self.lis[2], width=5)
        self.but_delen = Button(self.f_bot, text=self.lis[3], width=5)
        self.but_sum['command'] = self.sum
        self.but_minus['command'] = self.minus
        self.but_umnoz['command'] = self.umnozhenie
        self.but_delen['command'] = self.delenie
        self.l = Label(master, bg='white', fg='black', width=20)
        self.e.pack(pady = 3)
        self.g.pack(pady = 3)
        self.f_top.pack(pady = 3)
        self.f_bot.pack(pady = 3)
        self.but_sum.pack(side = LEFT)
        self.but_minus.pack(side = LEFT)
        self.but_umnoz.pack(side = LEFT)
        self.but_delen.pack(side = LEFT)
        self.l.pack(pady = 3)

    def proverka(self, numb1, numb2, t):
        try:
            a = float(numb1)
            b = float(numb2)
            c = eval('%f %s %f' % (a, self.lis[t], b))
            self.l['text'] = '%.2f %s %.2f = %.2f' % (a, self.lis[t], b, c)
            self.e.delete(0, END)
            self.g.delete(0, END)
        except ValueError:
            self.l['text'] = 'Ошибка'

    def sum(self):
        s = self.e.get()
        g = self.g.get()
        self.proverka(s, g, 0)

    def minus(self):
        s = self.e.get()
        g = self.g.get()
        self.proverka(s, g, 1)

    def umnozhenie(self):
        s = self.e.get()
        g = self.g.get()
        self.proverka(s, g, 2)

    def delenie(self):
        s = self.e.get()
        g = self.g.get()
        self.proverka(s, g, 3)


root = Tk()
root.minsize(width = 300, height = 100)
first_block = Block(root)
root.mainloop()
