import tkinter as tk

wd=tk.Tk()
wd.title('Hitung Luas')
wd.geometry('400x200')

frame=tk.Frame(master=wd)
lb_panjang=tk.Label(master=frame, text='Panjang')
lb_panjang.grid(row=0,column=0)
ent_panjang=tk.Entry(master=frame)
ent_panjang.grid(row=0,column=1)

lb_lebar=tk.Label(master=frame,text='Lebar')
lb_lebar.grid(row=1,column=0)
ent_lebar=tk.Entry(master=frame)
ent_lebar.grid(row=1,column=1)

frame.pack()

def hitung():
    p=float(ent_panjang.get())
    l=float(ent_lebar.get())
    lb_hasil['text']=p*l
    
btn=tk.Button(text='Hitung Luas',command=hitung)
btn.pack()

lb_hasil=tk.Label(text=0)
lb_hasil.pack()

def enter_frame(event):
    cur_pos['text']=f'({event.x}, {event.y})'
    
frame.bind('<Motion>',enter_frame)

cur_pos=tk.Label(text='0,0')
cur_pos.pack()


wd.mainloop()
