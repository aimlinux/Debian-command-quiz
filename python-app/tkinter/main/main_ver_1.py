import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 
import time
import random as rand
import sys



#グローバル変数定義
main_bg = "aqua"
title_font = "Arial"
main_font = "Arial"

button_1 = "ファイル"
button_2 = "メニュー"
button_3 = "タイトルへ戻る"
button_4 = "オプション"


# ウィンドウが生成されたフラグを取得するため（各ウィンドウが開いたときTrue、閉じたときFalseへ）
count_main = False
count_beginner = False
count_intermediate = False
count_advanced = False



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
        
        global pw_main, fm_main, fm_toolbar
        
        
        #メインウィンドウ作成
        pw_main = tk.PanedWindow(self.master, bg="blue", orient="vertical")
        pw_main.pack(expand=True, fill=tk.BOTH, side="left")
        
        #メインフレーム作成
        fm_main = tk.Frame(pw_main, bd=15, bg="aqua", relief="ridge")
        pw_main.add(fm_main)
        
        global count_main
        count_main = True
    # -------- メインフレームのオブジェクト作成 --------
    
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_main, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        
        space_label = tk.Label(fm_main, text="", bg=main_bg, height=2)
        space_label.pack(side=tk.TOP)

        title_label = tk.Label(fm_main, text=" ~~~ DebianQuiz ~~~ ", bg=main_bg, font=(title_font, 30), height=2)
        title_label.pack(side=tk.TOP)
        
        space_label = tk.Label(fm_main, text="", bg=main_bg, height=7)
        space_label.pack(side=tk.TOP)
    
        start_button = tk.Button(fm_main, text=" 初級 ", font=(main_font, 20), width=30, command=self.create_beginner)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" 中級 ", font=(main_font, 20), width=30, command=self.create_intermediate)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" 上級 ", font=(main_font, 20), width=30, command=self.create_advanced)
        start_button.pack(side=tk.TOP, pady=10)
        
        

        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""


    
    #初級偏
    def create_beginner(self):
        
        global fm_beginner, pw_beginner
        pw_main.destroy()
        
        pw_beginner = tk.PanedWindow(self.master, bg="blue", orient="vertical")
        pw_beginner.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_beginner = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_beginner.add(fm_beginner)
                
        global count_beginner, count_main
        count_beginner = True
        count_main = False
    # -------- メインフレームのオブジェクト作成 --------
    
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_beginner, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
    
    
    #中級偏
    def create_intermediate(self):
        
        global fm_intermediate, pw_intermediate
        pw_main.destroy()
        
        pw_intermediate = tk.PanedWindow(self.master, bg="red", orient="vertical")
        pw_intermediate.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_intermediate = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_intermediate.add(fm_intermediate)
                
        global count_intermediate, count_main
        count_intermediate = True
        count_main = False
    # -------- メインフレームのオブジェクト作成 --------
    
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_intermediate, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        
    
    #上級編
    def create_advanced(self):
        
        global fm_advanced, pw_advanced
        pw_main.destroy()
        
        pw_advanced = tk.PanedWindow(self.master, bg="pink", orient="vertical")
        pw_advanced.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_advanced = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_advanced.add(fm_advanced)
                
        global count_advanced, count_main
        count_advanced = True
        count_main = False
    # -------- メインフレームのオブジェクト作成 --------
    
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_advanced, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
    
    
    
    def return_title(self):
        
        if count_main == True:
            pw_main.destroy()
        elif count_beginner == True:
            pw_beginner.destroy()
        elif count_intermediate == True:
            pw_intermediate.destroy()
        elif count_advanced == True:
            pw_advanced.destroy()
        else:
            print("Error")
        
        print(str(count_main) + " : " + str(count_beginner) + " : " + str(count_intermediate) + " : " + str(count_advanced))
        
        count_main = False
        count_beginner = False
        count_intermediate = False
        count_advanced = False
        
        self.create_widgets()
        
        
        return 0
    
    
        
        
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