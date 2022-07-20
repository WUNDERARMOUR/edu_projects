from tkinter import *
from speedtest_cli import *

def test():
    download=Speedtest().download()
    upload=Speedtest().upload()
    download_speed=round(download/(10**6),2)
    upload_speed=round(upload/(10**6),2)
    download_label.config(text="Скорость входящая:\n"+str(download_speed)+"Мб/с")
    upload_label.config(text="Скорость исходящая:\n"+str(upload_speed)+"Мб/с")

app = Tk()
app.title("Скорость вашего интернета")
app.geometry("600x600")
button=Button(app,text="Нажмите, чтоб замерить скорость интернета",font=40,command=test)
button.pack(side=BOTTOM,pady=40)
download_label=Label(app,text="Скорость входящая:\n-",font=35)
download_label.pack(pady=(50,0))
upload_label=Label(app,text="Скорость исходящая:\n-",font=35)
upload_label.pack(pady=(10,0))

app.mainloop()