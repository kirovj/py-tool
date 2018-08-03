# encoding: utf-8
'''
@author: Jeremiah
@file: GUI.py
@time: 2018/6/27 18:31
@desc:
'''
import TransGoogle as trans
import Utils as ut
import GUI_XPath
import GUI_JSONPath
import hashlib
import json
from tkinter import *
from Crontab import getCrontab
from ParseJS import Py4js

LOG_LINE_NUM = 0

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    # 设置窗口
    def set_init_window(self):
        self.init_window_name.title("PyTool-v1.4   by：Jeremiah")              # 窗口名
        # self.init_window_name.geometry('320x160+10+10')                      # 290 160为窗口大小，+10 +10 定义窗口弹出时的默认展示位置
        self.init_window_name.geometry('1068x681+200+70')
        # self.init_window_name["bg"] = "lightblue"                            # 窗口背景色，其他背景色见：blog.csdn.net/chl0000/article/details/7657887
        # self.init_window_name.attributes("-alpha",0.8)                       # 虚化，值越小虚化程度越高
        # 标签
        # self.init_data_label = Label(self.init_window_name, text="待处理数据")
        # self.init_data_label.grid(row=0, column=0)
        # self.result_data_label = Label(self.init_window_name, text="输出结果")
        # self.result_data_label.grid(row=0, column=12)
        # self.log_label = Label(self.init_window_name, text="日志")
        # self.log_label.grid(row=12, column=0)
        # 文本框
        self.init_data_Text = Text(self.init_window_name, width=67, height=35)  # 原始数据录入框
        self.init_data_Text.grid(row=1, column=0, rowspan=10, columnspan=10)
        self.result_data_Text = Text(self.init_window_name, width=70, height=49)  # 处理结果展示
        self.result_data_Text.grid(row=1, column=12, rowspan=15, columnspan=10)
        self.log_data_Text = Text(self.init_window_name, width=66, height=9)  # 日志框
        self.log_data_Text.grid(row=13, column=0, columnspan=10)
        # 滚动条
        self.result_data_scrollbar_y = Scrollbar(self.init_window_name)  # 创建纵向滚动条
        self.result_data_scrollbar_y.config(command=self.result_data_Text.yview)  # 将创建的滚动条通过command参数绑定到需要拖动的Text上
        self.result_data_Text.config(yscrollcommand=self.result_data_scrollbar_y.set)  # Text反向绑定滚动条
        self.result_data_scrollbar_y.grid(row=1, column=23, rowspan=15, sticky='NS')

        # 按钮
        # 清空输入数据按钮
        self.clearInitData_button = Button(self.init_window_name, text="待处理数据", width=10,
                                           bg=self.init_window_name["bg"], relief="ridge", activebackground="GhostWhite", command=self.clearInitData)
        self.clearInitData_button.grid(row=0, column=0, sticky="w")

        # 清空输出数据按钮
        self.clearResultData_button = Button(self.init_window_name, text="输出结果", width=10,
                                             bg=self.init_window_name["bg"], relief="ridge", activebackground="GhostWhite", command=self.clearResultData)
        self.clearResultData_button.grid(row=0, column=12, sticky="w")

        # 清空日志
        self.clearLog_button = Button(self.init_window_name, text="日志", width=10,
                                      bg=self.init_window_name["bg"], relief="ridge", activebackground="GhostWhite", command=self.clearLog)
        self.clearLog_button.grid(row=12, column=0, sticky="w")


        # 读取文件
        # self.loadFile_button = Button(self.init_window_name, text="loadFile", bg="GhostWhite", width=10,
        #                               relief="solid", command=self.loadFile)
        # self.loadFile_button.grid(row=0, column=1, sticky="w")

        # readUpdateLog
        self.readUpdateLog_button = Button(self.init_window_name, text="更新日志", bg="WhiteSmoke", width=10,
                                           relief="solid", command=self.readUpdateLog)
        self.readUpdateLog_button.grid(row=0, column=21)

        # 字符串转MD5
        self.str2md5_button = Button(self.init_window_name, text="字符串转MD5", bg="#ADD8E6", width=10, command=self.str2md5)  # 调用内部方法  加()为直接调用
        self.str2md5_button.grid(row=1, column=11)

        # 谷歌翻译
        self.translate_button = Button(self.init_window_name, text="谷歌翻译", bg="#87CEEB", width=10, command=self.translate)
        self.translate_button.grid(row=2, column=11)

        # json格式化
        self.formatJson_button = Button(self.init_window_name, text="json格式化", bg="#00BFFF", width=10, command=self.formatJson)
        self.formatJson_button.grid(row=3, column=11)

        # urlEncode
        self.urlEncode_button = Button(self.init_window_name, text="urlEncode", bg="#1E90FF", width=10, command=self.urlEncode)
        self.urlEncode_button.grid(row=4, column=11)

        # urlDecode
        self.urlDecode_button = Button(self.init_window_name, text="urlDecode", bg="#4169E1", width=10, command=self.urlDecode)
        self.urlDecode_button.grid(row=5, column=11)

        # htmlParser
        self.htmlParser_button = Button(self.init_window_name, text="htmlParser", bg="#6495ed", width=10, command=self.htmlParser)
        self.htmlParser_button.grid(row=6, column=11)

        # Crontab
        self.Crontab_button = Button(self.init_window_name, text="Crontab", bg="darkcyan", width=10, command=self.Crontab)
        self.Crontab_button.grid(row=7, column=11)

        # 代码反格式化
        self.codeUnFormat_button = Button(self.init_window_name, text="代码反格式化", bg="#48d1cc", width=10, command=self.codeUnFormat)
        self.codeUnFormat_button.grid(row=8, column=11)

        # 头信息格式化
        self.formatHeaders_button = Button(self.init_window_name, text="头信息格式化", bg="#00ff7f", width=10, command=self.formatHeaders)
        self.formatHeaders_button.grid(row=9, column=11)

        # XPath
        self.XPath_button = Button(self.init_window_name, text="XPath", bg="#32cd32", width=10, command=self.XPathGUI)
        self.XPath_button.grid(row=10, column=11)

        # JSONPath
        self.JSONPath_button = Button(self.init_window_name, text="JSONPath", bg="#adff2f", width=10, command=self.JSONPathGUI)
        self.JSONPath_button.grid(row=11, column=11)

    def JSONPathGUI(self):
        try:
            GUI_JSONPath.main()
        except:
            self.writeLog("ERROR:JSONPath测试界面启动失败")

    def XPathGUI(self):
        try:
            GUI_XPath.main()
        except:
            self.writeLog("ERROR:XPath测试界面启动失败")

    def formatHeaders(self):
        src = self.init_data_Text.get(1.0, END)
        if src:
            try:
                result = ut.formatHeaders(src).replace('\'\',','')
                if result and result != '\n\n':
                    self.result_data_Text.delete(1.0, END)
                    self.result_data_Text.insert(1.0, result)
                    self.writeLog("INFO:头信息格式化 success")
            except:
                self.writeLog("ERROR:头信息格式化 failed")


    def readUpdateLog(self):
        try:
            result = ut.getUpdateLog()
            if result:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, result)
                self.init_data_Text.delete(1.0, END)
        except:
            self.writeLog("ERROR:查看更新日志失败，需要检查updateLog.txt文件或源代码")



    def codeUnFormat(self):
        src = self.init_data_Text.get(1.0, END)
        if src:
            try:
                result = ut.codeUnFormat(src)
                if result:
                    self.result_data_Text.delete(1.0, END)
                    self.result_data_Text.insert(1.0, result)
                    self.writeLog("INFO:代码反格式化 success")
            except:
                self.writeLog("ERROR:代码反格式化 failed")


    def congratulations(self):
        self.init_data_Text.delete(1.0, END)
        self.result_data_Text.delete(1.0, END)
        result = ut.congratulations()
        self.init_data_Text.insert(1.0, result)
        self.result_data_Text.insert(1.0, result)

    def clearInitData(self):
        self.init_data_Text.delete(1.0, END)

    def clearResultData(self):
        self.result_data_Text.delete(1.0, END)

    def clearLog(self):
        self.log_data_Text.delete(1.0, END)

    def Crontab(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            self.result_data_Text.delete(1.0, END)
            try:
                result = getCrontab(src)
                self.result_data_Text.insert(1.0, result)
                self.writeLog("INFO:Crontab success")
            except:
                self.writeLog("ERROR:Crontab failed")


    def htmlParser(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            self.result_data_Text.delete(1.0, END)
            try:
                result = ut.htmlParser(src)
                self.result_data_Text.insert(1.0, result)
                self.writeLog("INFO:htmlParse success")
            except:
                self.writeLog("ERROR:htmlParse failed")

    def urlDecode(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            self.result_data_Text.delete(1.0, END)
            try:
                result = ut.urlDecode(src)
                self.result_data_Text.insert(1.0, result)
                self.writeLog("INFO:urlDecode success")
            except:
                self.writeLog("ERROR:urlDecode failed")

    def urlEncode(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            self.result_data_Text.delete(1.0, END)
            try:
                result = ut.urlEncode(src)
                self.result_data_Text.insert(1.0, result)
                self.writeLog("INFO:urlEncode success")
            except:
                self.writeLog("ERROR:urlEncode failed")

    def formatJson(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            self.result_data_Text.delete(1.0, END)
            try:
                jsonData = json.loads(src)
                jsonData = json.dumps(jsonData, indent=4)
                self.result_data_Text.insert(1.0, jsonData)
                self.writeLog("INFO:formatJson success")
            except:
                self.writeLog("ERROR:formatJson failed")


    def translate(self):
        src = self.init_data_Text.get(1.0, END).strip().replace('\n', '')
        if src:
            js = Py4js()
            tk = js.getTK(src)
            if trans.checkLanguage(src):
                param = {'tk': tk, 'q': src, 'sl': 'en', 'tl': 'zh-CN', 'ssel': '0', 'tsel': '0'}
            else:
                param = {'tk': tk, 'q': src, 'sl': 'zh-CN', 'tl': 'en', 'ssel': '3', 'tsel': '3'}

            result = trans.parseJson(trans.getData(trans.MAIN_URL, param))
            if result == 0:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "翻译失败，返回数据错误！")
                self.writeLog("ERROR:Translate failed")
            else:
                self.result_data_Text.delete(1.0, END)
                text = result[0] + '\n'
                length = len(result)
                if length > 1:
                    for i in range(1, length):
                        r = result[i]
                        text = text + '\n{}:'.format(r[0])
                        for j in r[2]:
                            text = text + '\t{}:{}\n'.format(j[0], j[1])

                self.result_data_Text.insert(1.0, text)
                self.writeLog("INFO:Translate success")

    def str2md5(self):
        src = self.init_data_Text.get(1.0, END).strip().replace("\n", "").encode()
        if src:
            try:
                myMd5 = hashlib.md5()
                myMd5.update(src)
                myMd5_Digest = myMd5.hexdigest()
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, myMd5_Digest)
                self.writeLog("INFO:str_trans_to_md5 success")
            except:
                self.result_data_Text.delete(1.0, END)
                self.result_data_Text.insert(1.0, "ERROR:str_trans_to_md5 failed")


    # 日志动态打印
    def writeLog(self, logmsg):
        global LOG_LINE_NUM
        currentTime = ut.getCurrentTime()
        logmsg_in = str(currentTime) + " " + str(logmsg) + "\n"      # 换行
        if LOG_LINE_NUM <= 7:
            self.log_data_Text.insert(END, logmsg_in)
            LOG_LINE_NUM = LOG_LINE_NUM + 1
        else:
            self.log_data_Text.delete(1.0, 2.0)
            self.log_data_Text.insert(END, logmsg_in)


def main():
    init_window = Tk()            
    ZMJ_PORTAL = MY_GUI(init_window)
    # 设置根窗口默认属性
    ZMJ_PORTAL.set_init_window()

    init_window.mainloop()         
