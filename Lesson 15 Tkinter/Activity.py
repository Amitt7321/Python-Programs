from tkinter import *

window = Tk()
window.title('My Profile Card')
window.geometry('400x380')

title = Label(window, text='My Profile Card', fg='white', bg='Burlywood', width=40)
title.grid(row=0, column=0, columnspan=2, padx=10 ,pady=10)

name_label = Label(window, text='Name: ', fg='lightblue', bg='blue')
name_label.grid(row=1, column=0, padx=10 ,pady=5)

name_entry= Entry (window, fg='Purple', bg='Pink', width=25)
name_entry.grid(row=1, column=1, padx=10 ,pady=5)

hobby_label = Label(window, text='Hobby: ', fg='lightgreen', bg='Green')
hobby_label.grid(row=2, column=0, padx=10 ,pady=5)

hobby_entry= Entry (window, fg='orange', bg='yellow', width=25)
hobby_entry.grid(row=2, column=1, padx=10 ,pady=5)

about_frame = Frame(window, relief=RAISED, borderwidth=3)
about_frame.grid(row=3, column=0, columnspan=2, padx=10 ,pady=5)

about_label=Label(about_frame, text='About Me: ')
about_label.pack()

about_text = Text(about_frame, fg='black', bg='white',width=40, height=4)
about_text.pack()

submit=Button(window, text='Show My Card', bg='brown', fg='white', width=20)
submit.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()