# encoding: utf-8
'''
@author: Jeremiah
@contact: wuyiting@myhexin.com
@time: 2018/7/11 10:15
'''

# ==================================
# This is the GUI for JSONPath test,
# a new window for GUI.py .
# ==================================

from tkinter import *
from jsonpath import jsonpath
from json import loads
from tkinter.filedialog import askopenfilename


class GUI_JSONPath():

    def __init__(self,window_name):
        self.window_name = window_name

    def set_init_window(self):
        w = self.window_name.winfo_screenwidth()
        h = self.window_name.winfo_screenheight()
        self.window_name.title("JSONPath for PyTool   by：Jeremiah")
        self.window_name.geometry('600x530+%d+%d' % (w / 4, h / 6))
        # 标签
        self.expression_label = Label(self.window_name, text="JSONPath Expr:")
        self.expression_label.grid(row=0, column=0, sticky='w')
        self.data_label = Label(self.window_name, text="Test Text")
        self.data_label.grid(row=1, column=0, sticky='w')
        self.result_label = Label(self.window_name, text="Test Result")
        self.result_label.grid(row=3, column=0, sticky='w')
        # JSONPath语句输入框
        self.expression_entry = Entry(self.window_name, width=65)
        self.expression_entry.grid(row=0, column=1, columnspan=10)
        # json文本框、滚动条
        self.data_text = Text(self.window_name, width=82, height=18)
        self.data_text.grid(row=2, column=0, columnspan=11)
        self.data_scrollbar_y = Scrollbar(self.window_name)             # 创建纵向滚动条
        self.data_scrollbar_y.config(command=self.data_text.yview)      # 将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.data_text.config(yscrollcommand=self.data_scrollbar_y.set) # Text反向绑定滚动条
        self.data_scrollbar_y.grid(row=2, column=11, rowspan=1, sticky='NS')
        # 结果数据文本框、滚动条
        self.result_text = Text(self.window_name, width=82, height=15)
        self.result_text.grid(row=4, column=0, rowspan=1, columnspan=11)
        self.result_scrollbar_y = Scrollbar(self.window_name)
        self.result_scrollbar_y.config(command=self.result_text.yview)
        self.result_text.config(yscrollcommand=self.result_scrollbar_y.set)
        self.result_scrollbar_y.grid(row=4, column=11, rowspan=11, sticky='NS')

        # 按钮
        self.load_file = Button(self.window_name, text="Load File", bg="GhostWhite", width=10, relief="solid",
                                   command=self.load_file)
        self.load_file.grid(row=1, column=9, rowspan=1, columnspan=11)
        self.parse_button = Button(self.window_name, text="Let's get it", bg="GhostWhite", width=10, relief="solid",
                                   command=self.parse)
        self.parse_button.grid(row=3, column=9, rowspan=1, columnspan=11)

    def load_file(self):
        path = askopenfilename()
        self.file_label = Label(self.window_name, text="file: %s"%path)
        self.file_label.grid(row=1, column=1, columnspan=10, sticky='w')


    def parse(self):
        """解析"""
        self.result_text.delete(1.0, END)
        if self.file_label:
            try:
                with open(self.file_label['text'].replace('file: ', ''), 'rb') as f:
                    json_data = f.read()
            except:
                self.result_text.insert(1.0, "ERROR:读取文件失败！")
                return None
        else:
            json_data = self.data_text.get(1.0, END)
        jsonpath_expression = self.expression_entry.get()
        if jsonpath_expression and json_data:
            try:
                # json数据对象
                js_obj = loads(json_data)
                # 不使用jsonpath-rw，换成jsonpath
                result = jsonpath(js_obj, jsonpath_expression)
                if result:
                    self.result_text.insert(1.0, foreach(result))
            except:
                self.result_text.delete(1.0, END)
                self.result_text.insert(1.0, "ERROR:解析json数据失败")

def foreach(array):
    """递归遍历解析出的数据"""
    result_str = ""
    i = 1
    for element in array:
        result_str += '%d.\t' % i
        if isinstance(element, dict):
            # 字典
            length = len(element)
            a = 1
            for e in element:
                if a != length:
                    result_str += "%s:%s, " %(e, element[e])
                else:
                    result_str += "%s:%s" % (e, element[e])
                a += 1
        elif isinstance(element, list):
            # 如果还是列表，递归
            foreach(element)
        else:
            result_str += str(element)
        result_str += '\n'
        i += 1
    return result_str

'''
def output(self):
    """将结果输出"""
    self.result_text.delete(1.0, END)
    self.result_text.insert(1.0, '数据输出仍在开发中...ヾ(。￣□￣)ﾂ゜゜゜')
    # fixme..
'''

def main():
    gui = Tk()
    gui_JSONPath = GUI_JSONPath(gui)
    gui_JSONPath.set_init_window()
    gui.mainloop()

if __name__ == '__main__':
    main()