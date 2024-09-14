import tkinter as tk
from tkinter import messagebox
import random

def popup():
    x = random.randint(100, 700)  # 随机X坐标
    y = random.randint(100, 500)  # 随机Y坐标
    root.geometry(f"+{x}+{y}")    # 移动窗口到随机位置
    result = messagebox.askquestion("你要叫我爸吗？")  # 显示“是”或“不是”
    
    if result == 'yes':  # 用户选择 "是"
        messagebox.showinfo("哎，真乖！")  # 显示一个新消息
    else:  # 用户选择 "不是"
        messagebox.showinfo("你选择了‘不是’", "别害怕，继续吧！")  # 显示另一个消息
    
    messagebox.showinfo("惊喜！", "你不叫我爸？那就拜拜啦！哈哈哈")  # 再次显示原来的消息

root = tk.Tk()
root.withdraw()  # 隐藏主窗口

# 无限循环弹出
while True:
    popup()

root.mainloop()
