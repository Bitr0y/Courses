from tkinter import *


class Block:
    lis = ['+', '-', '*', '/']

    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.g = Entry(master, width=20)
        self.b = Button(master, text=self.lis[0], width=5)
        self.j = Button(master, text=self.lis[1], width=5)
        self.k = Button(master, text=self.lis[2], width=5)
        self.u = Button(master, text=self.lis[3], width=5)
        self.b['command'] = self.sum
        self.j['command'] = self.minus
        self.k['command'] = self.umnozhenie
        self.u['command'] = self.delenie
        self.l = Label(master, bg='black', fg='white', width=20)
        self.e.pack(expand = 1, fill = BOTH)
        self.g.pack(expand = 1, fill = BOTH)
        self.b.pack(expand = 1, fill = BOTH)
        self.j.pack(expand = 1, fill = BOTH)
        self.k.pack(expand = 1, fill = BOTH)
        self.u.pack(expand = 1, fill = BOTH)
        self.l.pack(expand = 1, fill = BOTH)

    def proverka(self, numb1, numb2, t):
        try:
            a = float(numb1)
            b = float(numb2)
            c = eval('%f %s %f' % (a, self.lis[t], b))
            self.l['text'] = '%.2f %s %.2f = %.2f' % (a, self.lis[t], b, c)
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
first_block = Block(root)
root.mainloop()
