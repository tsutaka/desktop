from tkinter import *
from tkinter import ttk

# -function()
# from pythonlib.date import dunction

# -date.function()
from pythonlib import date

# pythonlib.date.function()
# import pythonlib

WEEK_DAYS = 7

def testprint():
    print('Hello, %s!' % t.get())

if __name__ == '__main__':

    # GUIの初期化
    root = Tk()
    # グローバル変数の文字列変数の宣言
    t = StringVar()

    # タイトルの設定
    root.title('DeskAI')
    frame1 = ttk.Frame(root)
    frame1.grid()

    # フレームにラベルを追加
    today = date.get_today()
    today_str = date.date_format(today)

    label_days = []
    days = []
    # 今日から一週間分のラベルを作成
    today = date.get_today()
    for cnt in range(WEEK_DAYS):
        days += [date.add_days(today, cnt)]
        day_str = date.date_format(days[cnt])
        label_days += [ttk.Label(frame1, text=day_str)]
    # フレームにテキストボックスを追加
    entry1 = ttk.Entry(frame1, textvariable=t)
    # フレームにボタンを追加（処理を関連付け）
    button1 = ttk.Button(frame1, text='OK', command=testprint)

    # 各要素のグリッド位置を指定
    frame1.grid(row=0,column=0,sticky=(N,E,S,W))
    for cnt in range(WEEK_DAYS):
        label_days[cnt].grid(row=1,column=cnt+1,sticky=W)
    entry1.grid(row=2,column=2,sticky=W)
    button1.grid(row=3,column=3,sticky=W)

    # 全子要素にパディングを設定
    for child in frame1.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
