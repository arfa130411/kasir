from tkinter import *
 
window = Tk()
window.title("Kalkulator Kasir")
window.geometry('512x512')
 
lbl = Label(window, text="Masukan Nilai Pertama : ",anchor="e",width=20)
lbl.grid(column=0, row=0)
 
nilai1 = Entry(window,width=10)
nilai1.grid(column=1,row=0)
 
 
lbl2 = Label(window, text="Masukan Nilai Kedua : ",anchor="e",width=20)
lbl2.grid(column=0, row=1)
 
nilai2 = Entry(window,width=10)
nilai2.grid(column=1,row=1)
 
lbl3 = Label(window, text="Hasil : ",anchor="e",width=20)
lbl3.grid(column=0, row=2)
 
hasil = Label(window, text="0",anchor="w",width=70)
hasil.grid(column=1, row=2)
 
def tambah():
    hasil.configure(text=(int(nilai1.get())+int(nilai2.get())))
 
def kurang():
    hasil.configure(text=(int(nilai1.get())-int(nilai2.get())))
 
def kali():
    hasil.configure(text=(int(nilai1.get())*int(nilai2.get())))
 
def bagi():
    hasil.configure(text=(int(nilai1.get())/int(nilai2.get())))
 
 
btn = Button(window, text="Tambah", command=tambah)
btn.grid(column=0, row=3)
 
btn = Button(window, text="Kurang", command=kurang)
btn.grid(column=1, row=3)
 
btn = Button(window, text="Kali", command=kali)
btn.grid(column=0, row=4)
 
btn = Button(window, text="Bagi", command=bagi)
btn.grid(column=1, row=4)
 
 
window.mainloop()
