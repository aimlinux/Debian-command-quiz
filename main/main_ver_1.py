import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 
import time
import random as rand
import sys




BUTTON_OPUTIONS = {
    "expand" : "True",
    "fill" : "tk.NONE",
    
}



#アプリケーション（GUI）クラス
class Application(tk.Frame):
    DEBUG_LOG = True
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()
        
    def create_widgets(self):
        
        global pw_main, fm_main
        
        
        #self.create_toolbar()
        
        
        #メインウィンドウ作成
        pw_main = tk.PanedWindow(self.master, bg="blue", orient="vertical")
        pw_main.pack(expand=True, fill=tk.BOTH, side="left")
        
        #メインフレーム作成
        fm_main = tk.Frame(pw_main, bd=15, bg="aqua", relief="ridge")
        pw_main.add(fm_main)
        
        
    # -------- メインフレームのオブジェクト作成 --------

        global main_bg, title_font, main_font
        main_bg = "aqua"
        title_font = "Arial"
        main_font = "Arial"
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_main, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text="ボタン1", bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text="ボタン2", bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text="ボタン3", bg="#fff")
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text="ボタン4", bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        space_label = tk.Label(fm_main, text="", bg="red", height=2)
        space_label.pack(side=tk.TOP)
    
        title_label = tk.Label(fm_main, text=" ~~~ DebianQuiz ~~~ ", bg=main_bg, font=(title_font, 30), height=2)
        title_label.pack(side=tk.TOP)
        
        space_label = tk.Label(fm_main, text="", bg="red", height=7)
        space_label.pack(side=tk.TOP)
    
        start_button = tk.Button(fm_main, text=" 初級 ", font=(main_font, 20), width=30)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" 中級 ", font=(main_font, 20), width=30)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" 上級 ", font=(main_font, 20), width=30)
        start_button.pack(side=tk.TOP, pady=10)
        
        

        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""


    
    def create_toolbar(self):
        
        #メインウィンドウ作成
        pw_main = tk.PanedWindow(self.master, bg="#fff", orient="vertical")
        pw_main.pack(fill=tk.BOTH)
        
        #メインフレーム作成
        fm_main = tk.Frame(pw_main, bd=15, bg="#fff", relief="ridge")
        pw_main.add(fm_main)
        
        
        pw_toolbar = tk.PanedWindow(self.master, orient="vertical")
        pw_toolbar.pack(side="top", fill="x")
        
        fm_toolbar = tk.Frame(pw_toolbar, bg="#fff")
        pw_toolbar.add(fm_toolbar)
        
        
        # ボタンを作成してツールバーに配置
        button1 = tk.Button(fm_toolbar, text="ボタン1", bg="#fff")
        button1.pack(side="left", padx=2, pady=2)

        button2 = tk.Button(fm_toolbar, text="ボタン2", bg="#fff")
        button2.pack(side="left", padx=2, pady=2)
        
        
        
# 実行
main_window = tk.Tk()       

#画面の幅と高さを取得
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

myapp = Application(master=main_window)
myapp.master.title("DebianQuiz") # メインウィンドウの名前
myapp.master.geometry("1200x720") # ウィンドウの幅と高さピクセル単位で指定（width x height）
#myapp.master.attributes('-fullscreen', True) # フルスクリーン（終了ボタンがなくなるので非推奨）
myapp.mainloop()