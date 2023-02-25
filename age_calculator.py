from customtkinter import *
from tkcalendar import Calendar, DateEntry
import datetime

class App():
    # hàm khởi tạo
    def __init__(self, master):
        self.master = master
        self.show_text = StringVar()
        self.birthday = datetime.date.today()
        self.given_day = datetime.date.today()
        self.createWidgets()

    # hàm xử lý sự kiện khi nhấn nút
    def button_clicked(self):
        # tính độ chênh lệch thời gian
        delta = self.given_day - self.birthday
        # tính số ngày
        days = delta.days
        # tính số tuổi
        years = days // 365
        # tính số tháng
        months = (days % 365) // 30
        # tính số ngày
        days = days % 365 % 30
        # hiển thị kết quả
        self.show_text.set(f'{days} Day(s), {months} Month(s), {years} Year(s)')
        
    def createWidgets(self):
        set_appearance_mode("light")
        self.show_text.set(f'{0} Day(s), {0} Month(s), {0} Year(s)')
        # thiết lập kích thước cửa sổ
        self.master.geometry('500x400')
        root.maxsize(500, 400)
        root.minsize(500, 400)
        # thiết lập tiêu đề
        self.master.title('Age Calculator')
        # Thiết lập icon
        self.master.iconbitmap('icon.ico')
        # thiết lập màu nền
        # self.master.config(bg='light gray')

        # Tạo khung chứa các thành phần
        # frame_name = CTkFrame(self.master, fg_color='light gray')
        # frame_name.pack()
        CTkLabel(self.master, text='Age Calculator', font=('Arial', 23, 'bold','italic', 'underline'), text_color='green').pack(padx = 20, pady = 20)

        def set_birthday(event):
            self.birthday = birth_day.get_date()

        # tạo khung nhận ngày tháng năm sinh
        frame_date = CTkFrame(self.master, fg_color='light gray')
        frame_date.pack(padx=20, pady=20)
        CTkLabel(frame_date, text='Date of birth', font=('Arial', 18)).grid(row=0, column=0, padx=10, pady=10)
        birth_day = DateEntry(frame_date, width=20, background='darkblue',
                        foreground='white', date_pattern='dd/mm/yyyy', font=('Arial', 12))
        birth_day.set_date(datetime.date.today())
        birth_day.grid(row=1, column=0, padx=10, pady=10)
        birth_day.bind("<<DateEntrySelected>>", set_birthday)
        

        def set_given_day(event):
            self.given_day = given_day.get_date()
        CTkLabel(frame_date, text='Given Date', font=('Arial', 18)).grid(row=0, column=1, padx=10, pady=10)
        given_day = DateEntry(frame_date, width=20, background='darkblue',
                        foreground='white', date_pattern='dd/mm/yyyy', font=('Arial', 12))
        given_day.set_date(datetime.date.today())
        given_day.grid(row=1, column=1, padx=10, pady=10)
        given_day.bind("<<DateEntrySelected>>", set_given_day)

        # tạo nút calculate
        CTkButton(self.master, text='Calculate', font=('Arial', 23), text_color='green', fg_color='light green', command=lambda : self.button_clicked()).pack(padx=20, pady=10)

        # tạo khung hiển thị kết quả
        frame_result = CTkFrame(self.master, border_width=2, border_color='black')
        frame_result.pack(padx=20, pady=20)
        CTkLabel(frame_result, textvariable=self.show_text, font=('Arial', 23), width=300).pack(padx=10, pady=10)


root = CTk()
app = App(root)
root.mainloop()