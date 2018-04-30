from tkinter import *
from tkinter import ttk

def testprint():
    print('Hello, %s!' % t.get())

# GUIの初期化
root = Tk()
# タイトル
root.title('DeskAI')
# フレームの作成
frame1 = ttk.Frame(root)
# フレームにラベルを追加
label1 = ttk.Label(frame1, text='Your name:')
# グローバル変数の文字列変数の宣言
t = StringVar()

entry1 = ttk.Entry(frame1, textvariable=t)
button1 = ttk.Button(frame1, text='OK', command=testprint)

frame1.grid(row=0,column=0,sticky=(N,E,S,W))
label1.grid(row=1,column=1,sticky=E)
entry1.grid(row=1,column=2,sticky=W)
button1.grid(row=2,column=2,sticky=W)

for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
