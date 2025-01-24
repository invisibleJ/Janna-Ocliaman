import tkinter as tk

def show_data():
   
    last_name = entry_last_name.get()
    first_name = entry_first_name.get()
    job = entry_job.get()
    country = entry_country.get()
    print(f"Last Name: {last_name}, First Name: {first_name}, Job: {job}, Country: {country}")

def quit_app():
    root.quit()

root = tk.Tk()
root.title("tk #2")

label_last_name = tk.Label(root, text="Last Name")
label_last_name.grid(row=0, column=0, sticky="w", padx=10, pady=5)

label_first_name = tk.Label(root, text="First Name")
label_first_name.grid(row=1, column=0, sticky="w", padx=10, pady=5)

label_job = tk.Label(root, text="Job")
label_job.grid(row=2, column=0, sticky="w", padx=10, pady=5)

root.mainloop()

