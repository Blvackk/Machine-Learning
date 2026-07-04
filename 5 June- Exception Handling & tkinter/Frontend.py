import tkinter as tk

## Create the main application window

root = tk.Tk()
root.title("Simple Tkinter Application")
root.geometry("400x300")  #set window size

#Function to print "hello world" when button is clicked
def say_hello():
    print("Hello, World!")


#create a button and attach the say_hello function to it
hello_button = tk.Button(root, text="Click Me!", command=say_hello) 
hello_button.pack(pady=20)  # Add some padding around the button

# Start the Tkinter event loop
root.mainloop()