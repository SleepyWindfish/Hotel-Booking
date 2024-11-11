"""Build a Hotel booking system (like OYO) on the basis of the location chosen by the user. Rates and other details should be displayed along with star ratings out of 5. Each location may have 3-5 Hotels of each category 3-star,4-star and 5-star. The charges could comprise all taxes and all additional benefits may be displayed to the user."""

from tkinter import *
from tkinter import messagebox
import random
root=Tk()
root.title("Hotel Booking System")
#Random options
m=["Fully Booked","Half Booked","Completly Empty"]
active=random.choice(m)

def calculate():
  q=str(u.get())
  if(q=="Los Angles"):
    tx=0.095
  elif(q=="Michigan"):
    tx=0.0425
  elif(q=="Boston"):
    tx=0.057
  else:
    messagebox.showerror("Bad-Entry","Type the location exactly as shown. Upper Case matters!")
  
  slot=Label(root,text=active,bg="purple")
  slot.grid(row=7,column=1)
  if(active=="Fully Booked"):
    extra=50
    messagebox.showwarning("Full","Our Hotel is Fully Booked. Additionl $50 is required.")
    
  elif(active=="Half Booked"):
    extra=25
    messagebox.showwarning("Half","Our Hotel is filling quick. $25 is required to save a spot")
    
  elif(active=="Completly Empty"):
    extra=-20
    messagebox.showwarning("Empty","Our Hotel is Empty. If you come $20 discount")
  Hotel=str(u.get())
  
  if(Hotel=="Sheraton Gateway"):
    price=112
    
  elif(Hotel=="Omni Hotel"):
    price=90
    
  elif(Hotel=="Western Bonaventure"):
    price=85
  
  else:
    messagebox.showerror("Bad-Entry","Type the Hotel exactly as shown. Upper Case matters!")
  
  tr=int(Da.get())
  qu=(price*tr)+extra
  zu=qu*tx
  fi=qu+zu
  loca=str(l.get())
  fnam=str(ln.get())
  nam=str(na.get())
  Arr=str(Ar.get())
  yt=Label(root,text="Ticket Booked for: ",fg="red")
  ry=Label(root,text=nam,fg="red")
  yt.grid(row=14,column=1)
  ry.grid(row=14,column=2)
  que=Label(root,text=fnam,fg="red")
  que.grid(row=14,column=3)
  time=Label(root,text="Arrive In the Hotel at",fg="red")
  te=Label(root,text=Arr,fg="red")
  pir=Label(root,text="Tax: ",fg="red")
  rit=Label(root,text=tx,fg="red")
  time.grid(row=15,column=1)
  te.grid(row=15,column=2)
  pir.grid(row=16,column=1)
  rit.grid(row=16,column=2)
  xz=Label(root,text="Final cost is: ",fg="red")
  xz.grid(row=17,column=1)
  zx=Label(root,text=fi,fg="red")
  zx.grid(row=17,column=2)
    


read=Label(root,text="Los Angles, Michigan, Boston",fg="blue")

Loc=Label(root,text="Enter Location: ")
l=Entry()
name=Label(root,text="First Name: ")
na=Entry()
lname=Label(root,text="Last Name: ")
ln=Entry()
Phone=Label(root,text="Phone Number: ")
Ph=Entry()


h1=Label(root,text="Sheraton Gateway- 5 stars",fg="blue")
h1.grid(row=6,column=1)
h2=Label(root,text="Omni Hotel- 4 stars",fg="blue")
h2.grid(row=7,column=1)
h3=Label(root,text="Western Bonaventure- 3 stars",fg="blue")
h3.grid(row=8,column=1)
h4=Label(root,text="Enter your Hotel: ",bg="green")
u=Entry()
h4.grid(row=9,column=1)
u.grid(row=9,column=2)

Arrive=Label(root,text="Arrival date: ")
Ar=Entry()
Days=Label(root,text="How many Days?")
Da=Entry()
Arrive.grid(row=10,column=1)
Ar.grid(row=10,column=2)
Days.grid(row=11,column=1)
Da.grid(row=11,column=2)

final=Button(root,text="Book Hotel",bg="blue",command=calculate)
final.grid(row=12,column=1)






read.grid(row=1,column=1)
Loc.grid(row=2,column=1)
l.grid(row=2,column=2)
name.grid(row=3,column=1)
na.grid(row=3,column=2)
lname.grid(row=4,column=1)
ln.grid(row=4,column=2)
Phone.grid(row=5,column=1)
Ph.grid(row=5,column=2)

root.mainloop()