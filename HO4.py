import tkinter as tk

root = tk.Tk()
root.title("Profile Builder")
root.geometry("500x500")
root.resizable(True,True)
root.configure(bg="white")


La1 = tk.Label(root, text = "Profile Builder", foreground="Black")
La1.place(x=230,y=20)

user_entry = tk.Entry()
user_entry.place(x=20,y=50)

First = tk.Label(root, text = "First Name")
First.place(x=20, y= 60)

m_entry = tk.Entry()
m_entry.place(x=200, y = 50)

Middle = tk.Label(root, text = "Middle Name")
Middle.place(x=200, y = 60)

l_entry = tk.Entry()
l_entry.place(x=380, y= 50)

Last = tk.Label(root, text = "Last Name")
Last.place(x= 380, y = 60)

year_entry = tk.Entry()
year_entry.place(x=20,y=140)

year = tk.Label(root, text = "Birth Year")
year.place(x= 20, y= 150)

gender = tk.Label(root, text = "Gender")
gender.place(x= 20, y=200)

lala = tk.Radiobutton("Male", "Female")
lala.place()

root.mainloop()

