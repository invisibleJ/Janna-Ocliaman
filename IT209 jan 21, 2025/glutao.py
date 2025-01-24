import tkinter as tk

def show_data():
    last_name = entry_last_name.get()
    first_name = entry_first_name.get()
    job = entry_job.get()
    country = entry_country.get()
    print(f"Last Name: [last_name], First Name: [first_name], Job: [job], Country: [country]")

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

label_country = tk.Label(root, text="Country")
label_country.grid(row=3, column=0, sticky="w", padx=10, pady=5)

entry_last_name = tk.Entry(root)
entry_last_name.grid(row=0, column=1, padx=10, pady=5)

entry_first_name = tk.Entry(root)
entry_first_name.grid(row=1, column=1, padx=10, pady=5)

entry_job = tk.Entry(root)
entry_job.grid(row=2, column=1, padx=10, pady=5)

entry_country = tk.Entry(root)
entry_country.grid(row=3, column=1, padx=10, pady=5)

button_show = tk.Button(root, text="Show", command=show_data)
button_show.grid(row=4, column=0, padx=10, pady=10)

button_quit = tk.Button(root, text="Quit", command=quit_app)
button_quit.grid(row=4, column=1, padx=10, pady=10)

root.mainloop()
