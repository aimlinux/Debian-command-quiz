import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

# Styleオブジェクトを作成
style = ttk.Style()

# Buttonウィジェットのスタイルを設定
style.configure('Transparent.TButton', background='')

# スタイルに透明設定を追加
style.map('Transparent.TButton', background=[('', '')])

# Buttonウィジェットを作成
button = ttk.Button(root, text="透明なボタン", style='Transparent.TButton')
button.pack()

root.mainloop()