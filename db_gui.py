import tkinter as tk
from tkinter import ttk


def set_up_window():

    def ok_btn_cmd():
        print("Ok clicked")

    root = tk.Tk()
    root.title("Donor Database GUI")
    root.geometry("800x800")

    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0)
    name_label = ttk.Label(root, text="Name:")
    name_label.grid(column=0, row=1)

    name_entry = ttk.Entry(root, text="Enter name here")
    name_entry.grid(column=1, row=1)

    id_label = ttk.Label(root, text="Id:")
    id_label.grid(column=0, row=2)
    id_entry = ttk.Entry(root)
    id_entry.grid(column=1, row=2)

    ok_button = ttk.Button(root, text="Ok", command=ok_btn_cmd)
    ok_button.grid(column=1, row=6)
    cancel_button = ttk.Button(root, text="Cancel")
    cancel_button.grid(column=2, row=6)



    # print("Before main loop")
    # Should be last thing in function that should be in GUI
    root.mainloop()
    # print("After main loop")


if __name__ == "__main__":
    set_up_window()
    print("End")