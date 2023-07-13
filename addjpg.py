import tkinter as tk
from tkinter import filedialog
import shutil

def select_file():
    # 打开文件选择对话框
    file_path = filedialog.askopenfilename()

    # 指定目标文件夹路径
    target_folder = './images'

    # 复制文件到目标文件夹
    shutil.copy(file_path, target_folder)


if __name__ == '__main__':
        

    # 创建一个tkinter窗口
    window = tk.Tk()

        # 添加一个按钮，用于选择文件并复制
    button = tk.Button(window, text="注册员工", command=select_file)
    button.pack()

        # 启动窗口事件循环
    window.mainloop()