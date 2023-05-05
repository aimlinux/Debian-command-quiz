import tkinter as tk

root = tk.Tk()

# ツールバー用のFrameを作成
toolbar = tk.Frame(root, bg="gray")

# ボタンを作成してツールバーに配置
button1 = tk.Button(toolbar, text="ボタン1")
button1.pack(side="left", padx=2, pady=2)

button2 = tk.Button(toolbar, text="ボタン2")
button2.pack(side="left", padx=2, pady=2)

# ツールバーをウィンドウに配置
toolbar.pack(side="top", fill="x")

root.mainloop()