import time
from tkinter import ttk
import tkinter


#ボタンクリック時に実行する関数
def button_clicked():
    p.start(5)          #プログレスバー開始
    for i in range(6):
        time.sleep(1)   #1秒待機
        b["text"] = i   #秒数表示
    p.stop()            #プログレスバー停止


root = tkinter.Tk()

#プログレスバー
p = ttk.Progressbar(
    root,
    mode="indeterminate",
    )
p.pack()

#ボタン
b = tkinter.Button(
    root,
    width=15,
    text="start",
    command=button_clicked,
    )
b.pack()


root.mainloop()