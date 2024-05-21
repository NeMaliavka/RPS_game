from tkinter import *
import random as rdm
def btn_click(choise):
        global drow, win, lose
        comp_choise = rdm.randint(1, 3)

        if choise == comp_choise:
            drow += 1
            lbl.configure(text="Ничья")
        elif choise == 1 and comp_choise == 2 \
                or choise == 2 and comp_choise == 3 \
                or choise == 3 and comp_choise == 1:
            win += 1
            lbl.configure(text="Победа")
        else:
            lose += 1
            lbl.configure(text="Проигрыш")

        lbl2.config(text=f"Побед: {win}\nПроигрышей:"
                              f" {lose}\nНичей: {drow}")

        del comp_choise
                    
root = Tk()
root.geometry("430x160+200+200")
root.geometry("430x160")
root.title("Камень, ножницы, бумага")
root.resizable(False, False)
root["bg"] = "white"
btn = Button(root, text="Камень", font=("Times New Roman", 15),
        command=lambda x=1: btn_click(x))
btn2 = Button(root, text="Ножницы", font=("Times New Roman", 15),
        command=lambda x=2: btn_click(x))
btn3 = Button(root, text="Бумага", font=("Times New Roman", 15),
        command=lambda x=3: btn_click(x))

btn.place(x=10, y=100, width=120, height=50)
btn2.place(x=155, y=100, width=120, height=50)
btn3.place(x=300, y=100, width=120, height=50)

lbl = Label(root, text="Начало игры!", bg="#FFF", font=("Times New Roman", 21, "bold"))
lbl.place(x=150, y=25)

win = drow = lose = 0

lbl2 = Label(root, justify="left", font=("Times New Roman", 13),
                         text=f"Побед: {win}\nПроигрышей:"
                              f" {lose}\nНичей: {drow}",
                         bg="#FFF")
lbl2.place(x=5, y=5)

   

#if __name__ == '__main__':

#app.pack()
root.mainloop()
