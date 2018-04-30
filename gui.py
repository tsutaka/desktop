from tkinter import *
from tkinter import ttk

def testprint():
    print('Hello, %s!' % t.get())

# GUIの初期化
root = Tk()
# グローバル変数の文字列変数の宣言
t = StringVar()

# タイトルの設定
root.title('DeskAI')
# フレームの作成
# frame1 = ttk.Frame(root)
# frame1['height'] = 200
# frame1['width'] = 300
# frame1['relief'] = 'sunken'
# frame1['borderwidth'] = 5
# frame1.grid()
frame1 = ttk.Frame(
    root,
    height=200,
    width=300,
    relief='sunken',
    borderwidth=5)
frame1.grid()

# フレームにラベルを追加
label1 = ttk.Label(frame1, text='Your name:')
# フレームにテキストボックスを追加
entry1 = ttk.Entry(frame1, textvariable=t)
# フレームにボタンを追加（処理を関連付け）
button1 = ttk.Button(frame1, text='OK', command=testprint)

# 各要素のグリッド位置を指定
frame1.grid(row=0,column=0,sticky=(N,E,S,W))
label1.grid(row=1,column=1,sticky=E)
entry1.grid(row=1,column=2,sticky=W)
button1.grid(row=2,column=3,sticky=W)

# 全子要素にパディングを設定
for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
