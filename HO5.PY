import tkinter as tk

window = tk.Tk()
window.title("EXAMINATION")
window.geometry("300x500")
window.resizable(True,True)




def w1():
    label1 = tk.Label("window", text="Welcome!", font="20, Arial, Bold", anchor="center" )
    label1.grid(colunm="1", row="0")
    
    button1 = tk.Button(window, text="Click Me", font="20, Arial, Bold", anchor="center")
    button1.grid(column="0",row="1",columnspan=2)
    

    button2= tk.Button(window, text="Login",font="20, Arial, Bold", anchor="center")
    button2.grid(column="0", row="2", columnspan="2")
    
def 



    
    
    
        
window.mainloop()
