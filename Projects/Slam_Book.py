from tkinter import *
import tkinter.scrolledtext as st
from tkinter import messagebox as mb
def final_data():
	a=ent_name.get()
	file=open(a+".txt","w+")
	file.write(final.get("1.0","end-1c"))
	file.close()
	mb.showinfo("Added Successfully","DIARY WRITTEN SUCCESSFULLY")
	preview.destroy()
	win_add_entry.destroy()
	root.destroy()
	#end=Tk()
	#end.title("Added Successfully")
	#end.geometry("500x200")
	#Label(end,text = "DIARY WRITTEN SUCCESSFULLY",font = ("Aerial Bold", 20, "bold"),foreground = "green").pack()
	#end.mainloop()

def add_data():
	global final
	global preview
	a=ent_name.get()
	file=open(a+".txt","a+")
	import datetime
	x = datetime.datetime.now()
	date=x.strftime("%d %b %Y")
	time=x.strftime("%I:%M %p")
	file.write(date)
	file.write("\n")
	file.write(time)
	file.write("\n")
	file.write("*"*20)
	file.write("\n")
	name=ent_name.get()
	file.write(name)
	file.write("\n")
	file.write("*"*20)
	file.write("\n")
	nickname=ent_nicname_add.get()
	meet=ent_meet_add.get("1.0","end-1c")
	inc=ent_inc_add.get("1.0","end-1c")
	Learnt=ent_learnt_add.get("1.0","end-1c")
	advice=ent_advice_add.get("1.0","end-1c")
	wishes=ent_wishes_add.get("1.0","end-1c")
	quote=ent_quote_add.get("1.0","end-1c")
	mobileno=ent_mobileno_add.get()
	fb=ent_fb_add.get()
	ins=ent_ins_add.get()
	diary="hii "+nickname+",Did you remember where we meet first? . We meet "+meet+" and our friendship gets stonger and stonger from that day. even we have collect and create so many memories in jnv but the most interesting and funny was that incident when "+inc+".also i learn many things from you like "+Learnt+".A friend is who tells you the truth in a way that you never hurts so, here is some advice for you "+advice+".I hope "+wishes+" as some says that "+quote+" enjoy each and every moment of your life be happy be nice and most important be funny."
	file.write(diary)
	file.write("\n")
	contact="Contact details:"
	file.write(contact)
	file.write("\n")
	details="Phone number:"+mobileno+"\nfacebook:"+fb+"\ninstagram:"+ins
	file.write(details)
	file.write("\n")
	file.write("\n")
	file.close()

	file=open(a+".txt","r+")
	readall=file.read()
	file.close()
	preview=Tk()
	preview.title("Finally Written Diary")
	preview.geometry("900x700")
	window=LabelFrame(preview, text = "Diary Written:",font = ("Product Sans", 15, "bold"), fg = "red")
	window.pack(padx = 10, pady = 10, ipadx = 30, ipady = 30)
	window2=Frame(preview)
	window2.pack(padx = 10, pady = 10, ipadx = 30, ipady = 30)
	final=Text(window,font = ("Product Sans", 12),wrap="word",padx=30,pady=30)
	final.insert('1.0',readall)
	final.pack()
	submit_bttn=Button(window2, text = "Submit", width = 12,font = ("Product Sans", 15),command = final_data)
	submit_bttn.pack(padx = 3, pady = 3)
	preview.mainloop()

def clr_employee():
	ent_nicname_add.delete(0, END)
	ent_meet_add.delete(0, END)
	ent_inc_add.delete(0, END)
	ent_learnt_add.delete(0, END)
	ent_advice_add.delete(0, END)
	ent_wishes_add.delete(0, END)
	ent_quote_add.delete(0,END)
	ent_mobileno_add.delete(0,END)
	ent_fb_add.delete(0,END)
	ent_ins_add.delete(0,END)
	
def add_entry_win():
	global ent_nicname_add
	global ent_meet_add
	global ent_inc_add
	global ent_advice_add
	global ent_learnt_add
	global ent_wishes_add
	global ent_quote_add
	global ent_mobileno_add
	global ent_fb_add
	global ent_ins_add
	global win_add_employee
	global win_add_entry

	win_add_entry = Tk()
	win_add_entry.title("Diary Writting")
	win_add_entry.geometry("900x700")
	win_add_entry.option_add('*Font','MiClock\ ExtraLight 8')
	Label(win_add_entry, text = "Fill all the details in reference of VAIBHAV",font = ("Product Sans", 17, "bold"), fg = "#ff6a00").pack()
	
	frm_ent_data = LabelFrame(win_add_entry, text = "Enter Details",font = ("Product Sans", 15))
	frm_ent_data.pack(padx = 2, pady = 2, ipadx = 3, ipady = 3)
	
	frm_buttons = Frame(win_add_entry)
	frm_buttons.pack(padx = 2, pady = 2, ipadx = 3, ipady = 3)
	
	lbl_nicname_add = Label(frm_ent_data, text = "Enter Nickname: ",font = ("Product Sans", 15))
	lbl_nicname_add.grid(row = 0, column = 0, padx = 3, pady = 3)
	ent_nicname_add = Entry(frm_ent_data,font = ("Product Sans", 15))
	ent_nicname_add.grid(row = 0, column = 1, padx = 3, pady = 3)
	
	lbl_meet_add = Label(frm_ent_data, text = "Enter When We First Meet: ",font = ("Product Sans", 15))
	lbl_meet_add.grid(row = 1, column = 0, padx = 3, pady = 3)
	ent_meet_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_meet_add.grid(row = 1, column = 1, padx = 3, pady = 3)
	
	lbl_inc_add = Label(frm_ent_data, text = "Enter Some Incidence with Me: ",font = ("Product Sans", 15))
	lbl_inc_add.grid(row = 2, column = 0, padx = 1, pady = 1)
	ent_inc_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_inc_add.grid(row = 2, column = 1, padx = 3, pady = 3)
	
	
	lbl_learnt_add = Label(frm_ent_data, text = "Enter Something Learnt From Me: ",font = ("Product Sans", 15))
	lbl_learnt_add.grid(row = 3, column = 0, padx = 3, pady = 3)
	ent_learnt_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_learnt_add.grid(row = 3, column = 1, padx = 3, pady = 3)

	lbl_advice_add = Label(frm_ent_data, text = "Enter Some Advice For Me: ",font = ("Product Sans", 15))
	lbl_advice_add.grid(row = 4, column = 0, padx = 3, pady = 3)
	ent_advice_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_advice_add.grid(row = 4, column = 1, padx = 3, pady = 3)
	
	lbl_wishes_add = Label(frm_ent_data, text = "Any Wishies: ",font = ("Product Sans", 15))
	lbl_wishes_add.grid(row = 5, column = 0, padx = 3, pady = 3)
	ent_wishes_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_wishes_add.grid(row = 5, column = 1, padx = 3, pady = 3)
	
	lbl_quote_add = Label(frm_ent_data, text = "Any Quote : ",font = ("Product Sans", 15))
	lbl_quote_add.grid(row = 6, column = 0, padx = 3, pady = 3)
	ent_quote_add = Text(frm_ent_data,font = ("Product Sans", 15),height="2",width="15",wrap="word")
	ent_quote_add.grid(row = 6, column = 1, padx = 3, pady = 3)
	
	lbl_contact_add = Label(frm_ent_data, text = "Contact Details: ",font = ("Product Sans", 15))
	lbl_contact_add.grid(row = 7, column = 0, padx = 3, pady = 3)
	
	lbl_mobileno_add = Label(frm_ent_data, text = "Mobile No.: ",font = ("Product Sans", 15))
	lbl_mobileno_add.grid(row = 8, column = 0, padx = 3, pady = 3)
	ent_mobileno_add = Entry(frm_ent_data,font = ("Product Sans", 15))
	ent_mobileno_add.grid(row = 8, column = 1, padx = 3, pady = 3)
	
	lbl_fb_add = Label(frm_ent_data, text = "Facebook: ",font = ("Product Sans", 15))
	lbl_fb_add.grid(row = 9, column = 0, padx = 3, pady = 3)
	ent_fb_add = Entry(frm_ent_data,font = ("Product Sans", 15))
	ent_fb_add.grid(row = 9, column = 1, padx = 3, pady = 3)
	
	lbl_ins_add = Label(frm_ent_data, text = "Instagram: ",font = ("Product Sans", 15))
	lbl_ins_add.grid(row = 10, column = 0, padx = 3, pady = 3)
	ent_ins_add = Entry(frm_ent_data,font = ("Product Sans", 15))
	ent_ins_add.grid(row = 10, column = 1, padx = 3, pady = 3)
	
	#lbl_quote_add = Label(frm_ent_data, text = "Finally written diary: ",font = ("Product Sans", 10))
	#lbl_quote_add.grid(row = 11, column = 0, padx = 10, pady = 10)

	#ent_quote_add = Entry(frm_ent_data,font = ("Product Sans", 10))
	#ent_qoute_add.grid(row = 7, column = 1, padx = 10, pady = 10)
	
	btn_clear_add = Button(frm_buttons,text = "Clear", width = 20,command = clr_employee,font = ("Product Sans", 15))
	btn_clear_add.grid(row = 0, column = 0, padx = 10, pady = 1)
	
	btn_submit_add = Button(frm_buttons, text = "Preview", width = 20,font = ("Product Sans", 15),command = add_data)
	btn_submit_add.grid(row = 0, column = 1, padx = 10, pady = 1)
	
	win_add_entry.mainloop()

root=Tk()
root.title("WELCOME TO VAIBHAV'S PROGRAME")
root.geometry("500x200")
Label(root, text = "WRITE DIARY", font = ("LEMON MILK", 20, "bold"), foreground = "royalblue").pack()
frm_main = Frame(root)
frm_main.pack()
lbl_name_add=Label(frm_main,text="Enter Your Name:",font = ("Product Sans", 15))
lbl_name_add.grid(row = 0, column = 0 ,padx = 3, pady = 3)
ent_name=Entry(frm_main,font = ("Product Sans", 15))
ent_name.grid(row = 0, column = 1 ,padx = 3, pady = 3)
frm_start=Frame(root)
frm_start.pack()#(pady = 30)
btn_start = Button(frm_start, text = "START", width = 12, bd = 3,font = ("Product Sans", 15),command = add_entry_win) 
btn_start.pack()
root.mainloop()