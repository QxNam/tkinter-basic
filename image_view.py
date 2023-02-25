import tkinter as tk
import customtkinter
from PIL import Image, ImageTk
import numpy as np

class Frame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.paths = ["all.png"]
        self.path = self.paths[0]
        self.w = 800
        self.h = 500
        self.master.geometry(f"{self.w+30}x{self.h+100}")
        self.master.maxsize(self.w+30, self.h+100)
        self.master.minsize(self.w+30, self.h+100)
        self.load = customtkinter.CTkButton(
            master=self, text="add image", command=self.add_image_to_list)
        self.load.pack()

        self.img = Image.open(self.path)
        scale = np.array(self.img.size)/max(self.img.size)*self.h
        self.img = self.img.resize(tuple(scale.astype(int)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(master=self, image=self.img, justify="center", width=self.w, height=self.h)
        self.label.pack()

        control_frame = customtkinter.CTkFrame(master=self)
        control_frame.pack()

        self.prev = customtkinter.CTkButton(
            master=control_frame, text="<<", command=self.prev_image, width=30)
        self.prev.grid(row=0, column=0, padx=10, pady=10)
        self.next = customtkinter.CTkButton(
            master=control_frame, text=">>", command=self.next_image, width=30)
        self.next.grid(row=0, column=3, padx=10, pady=10)

        self.num = tk.StringVar()
        self.update_num()
        self.num_of_image = customtkinter.CTkLabel(
            master=control_frame, textvariable=self.num, font=("Arial", 20, "bold"), bg_color="transparent")
        self.num_of_image.grid(row=0, column=1, columnspan=2)

    def update_num(self):
        self.num.set(f"{self.paths.index(self.path) + 1}/{len(self.paths)}")

    def load_image(self, path):
        self.img = Image.open(path)
        scale = np.array(self.img.size)/max(self.img.size)*self.h
        self.img = self.img.resize(tuple(scale.astype(int)), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label.configure(image=self.img)
        self.update_num()

    def next_image(self):
        if self.paths.index(self.path) == len(self.paths) - 1:
            self.path = self.paths[0]

        else:
            self.path = self.paths[self.paths.index(self.path) + 1]
        self.load_image(self.path)

    def prev_image(self):
        if self.paths.index(self.path) == 0:
            self.path = self.paths[-1]
        else:
            self.path = self.paths[self.paths.index(self.path) - 1]
        self.load_image(self.path)

    def add_image_to_list(self):
        dialog = tk.filedialog.askopenfiles(
            "r", title="Mở file")
        filename = dialog[0].name
        if filename not in self.paths:
            self.paths.append(filename)
            self.path = self.paths[-1]
            self.load_image(self.path)
        else:
            tk.messagebox.showerror(
                title="Error!", message="Image already exists!", parent=self)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Show Image")
        self.iconbitmap('icon.ico')

        self.frame = Frame(master=self)
        self.frame.grid(row=1, column=0, sticky="nsew", columnspan=4,
                        padx=10, pady=10)


app = App()
app.mainloop()