from customtkinter import *

class App():
    # hàm khởi tạo
    def __init__(self, master):
        self.master = master
        self.show_text = StringVar()
        self.status = False
        self.history = None
        self.createWidgets()

    def split_expression(self, expression='1+1=3'):
        # hàm tách biểu thức thành 3 phần a, toán tử, b
        # trả về a, toán tử, b
        a = ''
        if expression[0] in ['-', '.']:
            a = expression[0]
            expression = expression[1:]
        opertor = ''
        b = ''
        for i in expression:
            if i in ['+', '-', '*', '/']:
                opertor = i
                break
            else:
                a += i
        for i in expression[expression.index(opertor)+1:]:
            if i == '=':
                break
            else:
                b += i
        return float(a), opertor, float(b)

    # hàm xử lý sự kiện khi nhấn nút
    def button_clicked(self, text):
        result = ''
        txt_origin = self.show_text.get()
        if txt_origin == '':
            if text in ['+', '*', '/', '=']:
                return
        else:
            if txt_origin[-1] in ['+', '-', '*', '/']:
                if text in ['*', '/']:
                    return

        if self.status == True:
            self.show_text.set(self.history)
            self.status = False

        if text == '=':
            try:
                a, opertor, b = self.split_expression(txt_origin)
                self.show_text.set(txt_origin+' = '+str(self.calc(a, b, opertor)))
                self.history = str(self.calc(a, b, opertor))
            except:
                self.show_text.set(txt_origin+' = '+'Error')
            self.status = True
        
        else:
            self.show_text.set(self.show_text.get()+text)
    

    # hàm tính toán
    def calc(self, a, b, opertor):
        res = None
        if opertor == '+':
            res = a + b
        elif opertor == '-':
            res = a - b
        elif opertor == '*':
            res = a * b
        elif opertor == '/':
            res = a / b
        if res == int(res):
            res = int(res)
        else:
            res = round(res, 2)
        return res

    def createWidgets(self):
        set_appearance_mode("dark")
        # thiết lập kích thước cửa sổ
        self.master.geometry('500x430')
        self.master.maxsize(600, 450)
        self.master.minsize(500, 430)
        # thiết lập tiêu đề
        self.master.title('Caculator')
        # Thiết lập icon
        # self.master.iconbitmap('icon.ico')

        # tạo các widget
        CTkLabel(master = self.master, text='CALCULATOR', font=('tohoma', 23)).pack(side = 'top', pady = 12)
        # tạo khung hiển thị
        frameDisplay = CTkFrame(master = self.master, width=500, height=50)
        frameDisplay.pack()
        CTkEntry(master = frameDisplay, textvariable = self.show_text, font=('tahoma', 23), state='disabled', bg_color='light cyan', width=450, height=50).pack(side = 'left', fill = 'x', expand = True)
        # tạo nút xóa 1 kí tự
        CTkButton(master = frameDisplay, text='X', font=('tahoma', 23), width=10, height=5, command=lambda: self.show_text.set(self.show_text.get()[:-1])).pack(side = 'right', padx = 5)
        # tạo khung chứa các nút bấm
        frameButton = CTkFrame(self.master, width=500, height=300, bg_color='gray')
        frameButton.pack(padx = 10, pady = 15)
        btn = ['1', '2', '3', '+', '4', '5', '6', '-', '7', '8', '9', '*', '0', '.', '=', '/']
        for i in range(4):
            for j in range(4):
                CTkButton(frameButton, text=btn[4*i+j], font=('tahoma', 27), width=100, height=40, command=lambda txt = btn[4*i+j]: self.button_clicked(txt)).grid(row=i, column=j, padx=5, pady=5)
        # tạo nút xóa trắng nội dung khung hiển thị
        CTkButton(self.master, text='Clear', font=('tahoma', 27), fg_color='#cc0000', width=80, height=50, command=lambda:self.show_text.set('')).pack()
        # tạo chữ logo
        CTkLabel(self.master, text='Made by QxNam', font=('Bell MT', 15), text_color = 'light green').pack(side = 'right', pady = 5, padx = 10)

root = CTk()
app = App(root)
root.mainloop()
