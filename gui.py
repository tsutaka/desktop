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
frame1 = ttk.Frame(
    root,
    height=200,
    width=300,
    relief='sunken',
    borderwidth=5)
frame1.grid()

# フレームにラベルを追加
label_day0 = ttk.Label(frame1, text='day0 ')
label_day1 = ttk.Label(frame1, text='day1 ')
label_day2 = ttk.Label(frame1, text='day2 ')
label_day3 = ttk.Label(frame1, text='day3 ')
label_day4 = ttk.Label(frame1, text='day4 ')
label_day5 = ttk.Label(frame1, text='day5 ')
label_day6 = ttk.Label(frame1, text='day6 ')
# フレームにテキストボックスを追加
entry1 = ttk.Entry(frame1, textvariable=t)
# フレームにボタンを追加（処理を関連付け）
button1 = ttk.Button(frame1, text='OK', command=testprint)

# 各要素のグリッド位置を指定
frame1.grid(row=0,column=0,sticky=(N,E,S,W))
label_day0.grid(row=1,column=1,sticky=W)
label_day1.grid(row=1,column=2,sticky=W)
label_day2.grid(row=1,column=3,sticky=W)
label_day3.grid(row=1,column=4,sticky=W)
label_day4.grid(row=1,column=5,sticky=W)
label_day5.grid(row=1,column=6,sticky=W)
label_day6.grid(row=1,column=7,sticky=W)
entry1.grid(row=2,column=2,sticky=W)
button1.grid(row=3,column=3,sticky=W)

# 全子要素にパディングを設定
for child in frame1.winfo_children():
    child.grid_configure(padx=5, pady=5)

root.mainloop()
