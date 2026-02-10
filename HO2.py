import tkinter as HO

window = HO.Tk()
window.title("<-John Paul A. Roces->")
window.geometry("600x600")
window.resizable(False, True)
window.configure(bg="white")


label = HO.Label(window, text="Student Profile", font=("Arial", 23, "bold"), fg="black", bg="white")
label.pack(pady=20)

labe2 = HO.Label(window, text="Name : John Paul A. Roces", font=("Arial", 14), fg="black", bg="white")
labe2.pack(anchor="w", padx=40, pady=5)

labe3 = HO.Label(window, text="Age : 18 years old", font=("Arial", 14), fg="black", bg="white" )
labe3.pack(anchor="w", padx=40, pady=5)

labe4 = HO.Label(window, text="Birthday : March 1, 2007", font=("Arial", 14), fg="black", bg="white")
labe4.pack(anchor="w", padx=40, pady=5)

labe5 = HO.Label(window, text="Motto :", font=("Arial", 14), fg="black", bg="white")
labe5.pack(anchor="w", padx=40, pady=10)

labe6 = HO.Label(window, text="Peace makes me who I am", font=("Arial", 14, "italic"), fg="black", bg="white")
labe6.pack(anchor="w", padx=60)

window.mainloop()
