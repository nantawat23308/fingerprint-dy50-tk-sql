import mysql.connector
cnx=mysql.connector.connect(user='person1',password='123456789',host='localhost',database='fingerprint')       # connect to MySql database
cur=cnx.cursor()

import tkinter  as tk 
from tkinter import * 
my_w = tk.Tk()
my_w.geometry("400x250") 



cur.execute("SELECT * FROM fingerprint")
i=0 
for fingerprint in cur: 
    for j in range(len(fingerprint)):
        e = Entry(my_w, width=10, fg='blue') 
        e.grid(row=i, column=j) 
        e.insert(END, fingerprint[j])
    i=i+1
my_w.mainloop()