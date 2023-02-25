import tkinter as tk
from customtkinter import *


class App(CTk):
    def __init__(self):
        super().__init__()
        set_appearance_mode('system')
        self.iconbitmap('icon.ico')
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)
        self.filname = None
        menuFrame = CTkFrame(master=self)
        menuFrame.pack()
        self.button_open = CTkButton(
            master=menuFrame, text="Mở file", command=self.button_open_clicked, width=150)
        self.button_open.pack(side = 'left', padx=10, pady=10)
        self.button_save = CTkButton(
            master=menuFrame, text="Lưu", command=self.button_save_clicked, width=150)
        self.button_save.pack(side = 'right', padx=10, pady=10)

        self.textbox = CTkTextbox(
            master=self, width=300, corner_radius=0)
        self.textbox.pack()
        self.textbox.insert("0.0", "")
       
        

    def button_open_clicked(self):
        dialog = tk.filedialog.askopenfiles(
            "r", filetypes=[("Text files", "*.txt")], title="Mở file")
        self.filename = dialog[0].name
        with open(self.filename, "r", encoding='utf-8') as f:
            text = f.read()
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", text)

    def button_save_clicked(self):
        text = self.textbox.get("0.0", "end")
        try:
            with open(self.filename, "w", encoding='utf-8') as f:
                f.write(text)
            dialog = CTkInputDialog(text="Lưu thành công", title="Thông báo")
            dialog.mainloop()
        except:

            # tạo dialog thông báo
            dialog = CTkInputDialog(text="Lưu không thành công", title="Thông báo")
            dialog.mainloop()


app = App()
app.mainloop()