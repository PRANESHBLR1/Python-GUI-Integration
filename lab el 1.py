from tkinter import *

def calculate_values():
    global max_height_feet  # Declare max_height_feet as a global variable
    try:
        velocity = float(b_input.get())
        player_height = float(pHeight_input.get())
        
        # Define acceleration (assuming it's gravity, approximately 9.8 m/s^2)
        a = 16
        
        time = velocity / (2 * a)
        max_height_meters = a * (time ** 2) + velocity * time + player_height
        
        # Conversion factor: 1 meter = 3.28084 feet
        max_height_feet = max_height_meters * 3.28084
        
        x1.config(text=f"Time: {time:.2f} seconds")
        y1.config(text=f"Max Height: {max_height_meters:.2f} meters ")
        
        # Enable the "Show in Feet" button
        show_in_feet_button.config(state=NORMAL)
    except ValueError:
        x1.config(text="Invalid input. Please enter numeric values.")
        y1.config(text="")
        # Disable the "Show in Feet" button if there's an error
        show_in_feet_button.config(state=DISABLED)

def show_in_feet():
    try:
        # Create a new window to display max height in feet
        feet_window = Toplevel(root)
        feet_window.title("Max Height in Feet")
        
        max_height_feet_label = Label(feet_window, text=f"Max Height: {max_height_feet:.2f} feet")
        max_height_feet_label.pack(padx=20, pady=20)
    except NameError:
        # Handle the case where max_height_feet is not defined
        max_height_feet_label = Label(feet_window, text="Please calculate first.")
        max_height_feet_label.pack(padx=20, pady=20)

root = Tk()
root.title("Basketball")
root.minsize(500, 500)
root.configure(background="orange")

text_label = Label(root, text="BASKETBALL HEIGHT AND TIME CALCULATOR")
text_label.pack()
text_label.config(font=("veranda", 24))

b = Label(root, text="Enter the velocity of the ball in m/s")
b.pack()
b.config(font=("veranda", 24))
b_input = Entry(root, width=50)
b_input.pack(ipady=6, pady=(1, 15))

a = 16  # acceleration due to gravity

pHeight = Label(root, text="Enter the player height(in feet)")
pHeight.pack(ipady=6, pady=(1, 15))
pHeight.config(font=("veranda", 24))
pHeight_input = Entry(root, width=50)
pHeight_input.pack(ipady=6, pady=(1, 15))

calc_button = Button(root, text="Calculate", command=calculate_values)
calc_button.pack()

x = Label(root, text="Time :")
x.pack()
x1 = Label(root, text="")
x1.pack()

y = Label(root, text="Max Height :")
y.pack()
y1 = Label(root, text="")
y1.pack()

show_in_feet_button = Button(root, text="Show in Feet", command=show_in_feet, state=DISABLED)
show_in_feet_button.pack()
photo=PhotoImage(file="C:\\Pranesh\\1st year BE\\python\\el\\lebron james.png")
# Create a Label Widget to display the text or Image
label = Label(root, image = photo)
label.pack()

root.mainloop()

