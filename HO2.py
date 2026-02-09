import tkinter as HO

window =HO. Tk()
window.title("<-John Paul A. Roces->")
window.geometry("600x600")
window.resizable(False,True)
window.configure(bg="white")

label = HO.Label(window, text="Student Profile", font=("Arial",23), fg="black", anchor="center" )
label.pack()
labe2 = HO.Label(window, text="Name--> John Paul A. Roces", font=("Arial",14), fg="black", anchor="center")
labe2.pack(side="left", pady=1, expand=True)
labe3 = HO.Label(window, text="Age--> 18 Years Old", font=("Arial",14), fg="black", anchor="center")
labe3.pack(side="left", pady=2)
labe4 = HO.Label(window, text="Birthday--> March 1, 2007", font=("Arial",14), fg="black", anchor="center")
labe4.pack(side="left", pady=3)
labe5 = HO.Label(window, text="Motto", font=("Arial",14), fg="black", anchor="center")
labe5.pack(side="left", pady=4)
labe6 = HO.Label(window, text="Motto", font=("Arial",14), fg="black", anchor="center")
labe6.pack()



window.mainloop()
