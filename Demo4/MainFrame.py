# coding=gbk
__author__ = 'generated by py-ui4win'

import string, os, time
import threading
import ctypes

from PyUI import *
from MsgBox import *
from PyFrameBase import *
import UICommon
from CommonUtil import CommonUtils
from PyWin32Utils import PyWin32Util
def PyThreadPythonExecute(PyClassInstance, ):
    try:
        PyClassInstance.StartAnimation()
        PyClassInstance.ExecutePython()
    except Exception, e:
        PyLog().LogText(str(e))
    PyClassInstance.StopAnimation()
    PyLog().LogText('PyThreadExecute exit')


class MainFrame(PyFrameBase):
    def __init__(self):
        super(MainFrame, self).__init__()
        self.clsName = self.__class__.__name__
        self.skinFileName = self.__class__.__name__ + '.xml'

    # 不要改动
    def GetSkinFile(self):
        return self.skinFileName

    # 不要改动
    def GetWindowClassName(self):
        return self.clsName

    # 退出处理
    def OnExit(self, sendor, wParam, lParam):
        self.ExitApp()

    # 准备显示前的处理
    def OnPrepare(self, sendor, wParam, lParam):
        self.minbtn = self.PyFindButton("minbtn")
        self.maxbtn = self.PyFindButton("maxbtn")
        self.restorebtn = self.PyFindButton("restorebtn")
        self.closebtn = self.PyFindButton("closebtn")
        self.btnOpenLog = self.PyFindButton("btnOpenLog")
        self.btnClearLog = self.PyFindButton("btnClearLog")
        self.btnExcute = self.PyFindButton("btnExcute")
        self.OU_home = self.PyFindOption("OU_home")
        self.OU_back = self.PyFindOption("OU_back")
        self.OU_forward = self.PyFindOption("OU_forward")
        self.OU_genPwd3 = self.PyFindOption("OU_genPwd3")
        self.OU_genPwd4 = self.PyFindOption("OU_genPwd4")
        self.OU_genPwd5 = self.PyFindOption("OU_genPwd5")
        self.OU_genPwd6 = self.PyFindOption("OU_genPwd6")
        self.OU_enableProxy = self.PyFindOption("OU_enableProxy")
        self.OU_disableProxy = self.PyFindOption("OU_disableProxy")
        self.txtDiagnose = self.PyFindRichEdit("txtDiagnose")
        self.AnimationJuhua1 = self.PyFindAnimation("AnimationJuhua1")
        self.HLU_caption = self.PyFindHorizontalLayout("HLU_caption")
        self.DriverDiagnoseTab = self.PyFindVerticalLayout("DriverDiagnoseTab")
        self.TLU_client = self.PyFindTabLayout("TLU_client")

    # 界面事件处理
    def OnNotify(self, sendor, sType, wParam, lParam):
        # 用户点击事件
        if sType == DUI_MSGTYPE_CLICK:
            if sendor == "minbtn":
                pass
            elif sendor == "maxbtn":
                pass
            elif sendor == "restorebtn":
                pass
            elif sendor == "closebtn":
                pass
            elif sendor == "btnOpenLog":
                if os.path.isfile(PyWin32Util.GetExeDirectory() + '\\applog.ini'):
                    #用ctypes会导致程序崩溃
                    #shell32 = ctypes.windll.LoadLibrary("shell32.dll");
                    #shell32.ShellExecuteA(None,'open', 'notepad',PyWin32Util.GetExeDirectory() + '\\applog.ini','',1);
                    PyWin32Util.ShellExcute(0, 'open', PyWin32Util.GetExeDirectory() + '\\applog.ini', '', '', 1)
                else:
                    UICommon.ShowMessageBox(self.GetHWnd(), '错误', '日志文件不存在')

            elif sendor == "btnClearLog":
                self.txtDiagnose.SetText('')
                if os.path.isfile(PyWin32Util.GetExeDirectory() + '\\applog.ini'):
                    os.remove(PyWin32Util.GetExeDirectory() + '\\applog.ini')

            elif sendor == "btnExcute":
                t = threading.Thread(target=PyThreadPythonExecute,args=(self,))
                t.start()
                #self.ExecutePython()
            elif sendor == "OU_home":
                pass
            elif sendor == "OU_back":
                pass
            elif sendor == "OU_forward":
                pass
            elif sendor == "OU_genPwd3":
                pass
            elif sendor == "OU_genPwd4":
                pass
            elif sendor == "OU_genPwd5":
                pass
            elif sendor == "OU_genPwd6":
                pass
            elif sendor == "OU_enableProxy":
                pass
            elif sendor == "OU_disableProxy":
                pass

        # 用户选择事件
        if sType == DUI_MSGTYPE_ITEMSELECT:
            pass

    def StopAnimation(self):
        self.AnimationJuhua1.StopAnimation()

    def StartAnimation(self):
        self.AnimationJuhua1.StartAnimation()

    def AppendAndLog(self, line):
        PyLog().LogText( line)
        msg = self.txtDiagnose.GetText()
        self.txtDiagnose.SetText(msg + '\n' + line)

    def ShowAndLog(self, line):
        PyLog().LogText( line)
        self.txtDiagnose.SetText(line)

    def ExecutePython(self,):
        CommonUtils.ReverseToExePath()
        ISOTIMEFORMAT='%Y-%m-%d %X'
        self.ShowAndLog(time.strftime( ISOTIMEFORMAT, time.localtime() ))

        i = 0
        while i < 20:
            self.AppendAndLog('等待了%d秒' % i)
            time.sleep(1)
            i = i + 1

        self.AppendAndLog('成功')
