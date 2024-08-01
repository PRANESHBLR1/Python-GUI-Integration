import tkinter as tk
from tkinter import ttk, messagebox
import csv

class EmployeeDatabaseGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Employee Database")

        # Set background color to blue
        self.master.configure(bg='blue')

        # Employee data columns
        self.columns = ["ID", "Name", "Position", "Salary"]

        # Create a list to store employee data
        self.employee_data = []

        # Load data from file if available
        self.load_data()

        # Create a frame
        self.frame = ttk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Create and place a heading label
        self.heading_label = tk.Label(self.frame, text="Employee Database", font=("Helvetica", 16, "bold"))
        self.heading_label.pack(pady=10)

        # Create Treeview for displaying employee data
        self.tree = ttk.Treeview(self.frame, columns=self.columns, show="headings")

        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        self.tree.pack()

        # Create buttons for adding, displaying, searching, and deleting data
        add_button = ttk.Button(self.frame, text="Add Employee", command=self.add_employee)
        add_button.pack(side=tk.LEFT, padx=5)

        search_button = ttk.Button(self.frame, text="Search Employee", command=self.search_employee)
        search_button.pack(side=tk.LEFT, padx=5)

        delete_button = ttk.Button(self.frame, text="Delete Employee", command=self.delete_employee)
        delete_button.pack(side=tk.LEFT, padx=5)

        display_button = ttk.Button(self.frame, text="Save and Display Data", command=self.display_data)
        display_button.pack(side=tk.LEFT, padx=5)

    def add_employee(self):
        # Create a new window for adding employee details
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Employee")

        # Entry widgets for employee details
        id_label = tk.Label(add_window, text="ID:")
        id_label.grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(add_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        name_label = tk.Label(add_window, text="Name:")
        name_label.grid(row=1, column=0, padx=5, pady=5)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=1, column=1, padx=5, pady=5)

        position_label = tk.Label(add_window, text="Position:")
        position_label.grid(row=2, column=0, padx=5, pady=5)
        position_entry = tk.Entry(add_window)
        position_entry.grid(row=2, column=1, padx=5, pady=5)

        salary_label = tk.Label(add_window, text="Salary:")
        salary_label.grid(row=3, column=0, padx=5, pady=5)
        salary_entry = tk.Entry(add_window)
        salary_entry.grid(row=3, column=1, padx=5, pady=5)

        # Button to add employee data to the list
        add_button = tk.Button(add_window, text="Add", command=lambda: self.add_employee_data(
            id_entry.get(), name_entry.get(), position_entry.get(), salary_entry.get(), add_window))
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

    def add_employee_data(self, emp_id, name, position, salary, add_window):
        # Validate input
        if not emp_id or not name or not position or not salary:
            messagebox.showerror("Error", "Please fill in all fields")
            return

        # Check for duplicate ID
        if any(emp['ID'] == emp_id for emp in self.employee_data):
            messagebox.showerror("Error", "Employee with this ID already exists")
            return

        # Add employee data to the list
        new_data = {"ID": emp_id, "Name": name, "Position": position, "Salary": salary}
        self.employee_data.append(new_data)

        # Update Treeview
        self.update_treeview()

        # Close the add employee window
        add_window.destroy()

    def update_treeview(self):
        # Clear existing data in Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert updated data into Treeview
        for row in self.employee_data:
            self.tree.insert("", "end", values=[row[col] for col in self.columns])

    def search_employee(self):
        # Create a new window for searching employee details
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Employee")

        # Entry widget for searching by ID
        id_label = tk.Label(search_window, text="Employee ID:")
        id_label.grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(search_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to search for employee
        search_button = tk.Button(search_window, text="Search", command=lambda: self.display_search_result(
            id_entry.get(), search_window))
        search_button.grid(row=1, column=0, columnspan=2, pady=10)

    def display_search_result(self, emp_id, search_window):
        # Check if the employee ID exists in the database
        result = [emp for emp in self.employee_data if emp['ID'] == emp_id]

        if result:
            # Create a new window for displaying search result
            result_window = tk.Toplevel(self.master)
            result_window.title("Search Result")

            # Create Treeview for displaying search result
            result_tree = ttk.Treeview(result_window, columns=self.columns, show="headings")

            for col in self.columns:
                result_tree.heading(col, text=col)
                result_tree.column(col, width=100)

            result_tree.pack()

            # Insert data into Treeview
            for row in result:
                result_tree.insert("", "end", values=[row[col] for col in self.columns])
        else:
            messagebox.showinfo("Info", "No employee found with the given ID.")

        # Close the search window
        search_window.destroy()

    def delete_employee(self):
        # Create a new window for deleting employee
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Employee")

        # Entry widget for entering the ID of the employee to be deleted
        id_label = tk.Label(delete_window, text="Employee ID:")
        id_label.grid(row=0, column=0, padx=5, pady=5)
        id_entry = tk.Entry(delete_window)
        id_entry.grid(row=0, column=1, padx=5, pady=5)

        # Button to delete employee
        delete_button = tk.Button(delete_window, text="Delete", command=lambda: self.delete_employee_data(
            id_entry.get(), delete_window))
        delete_button.grid(row=1, column=0, columnspan=2, pady=10)

    def delete_employee_data(self, emp_id, delete_window):
        # Check if the employee ID exists in the database
        index_to_delete = None
        for i, emp in enumerate(self.employee_data):
            if emp['ID'] == emp_id:
                index_to_delete = i
                break

        if index_to_delete is not None:
            # Confirm deletion with a messagebox
            confirm = messagebox.askyesno("Confirm Deletion", f"Do you want to delete employee with ID {emp_id}?")
            if confirm:
                # Delete the employee
                del self.employee_data[index_to_delete]

                # Update Treeview
                self.update_treeview()

                # Inform user about the deletion
                messagebox.showinfo("Info", f"Employee with ID {emp_id} deleted successfully.")
        else:
            messagebox.showinfo("Info", "No employee found with the given ID.")

        # Close the delete window
        delete_window.destroy()

    def display_data(self):
        # Create a new window for displaying all employee data
        display_window = tk.Toplevel(self.master)
        display_window.title("Employee Data")

        # Create Treeview for displaying employee data
        display_tree = ttk.Treeview(display_window, columns=self.columns, show="headings")

        for col in self.columns:
            display_tree.heading(col, text=col)
            display_tree.column(col, width=100)

        display_tree.pack()

        # Insert data into Treeview
        for row in self.employee_data:
            display_tree.insert("", "end", values=[row[col] for col in self.columns])

    def save_data(self):
        # Save employee data to a CSV file
        file_path = "employee_data.csv"
        with open(file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.columns)
            writer.writeheader()
            writer.writerows(self.employee_data)

    def load_data(self):
        # Load employee data from a CSV file if available
        file_path = "employee_data.csv"
        try:
            with open(file_path, mode='r') as file:
                reader = csv.DictReader(file)
                self.employee_data = [row for row in reader]

        except FileNotFoundError:
            # If the file is not found, initialize an empty list
            self.employee_data = []

if __name__ == "__main__":
    root = tk.Tk()
    app = EmployeeDatabaseGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.save_data)  # Save data on window close
    root.mainloop()
