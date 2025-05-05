import sys
import time
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication,\
    QWidget


class mainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupUi()
    
    def initUI(self):
        self.ui = uic.loadUi(r"项目\项目8--桌面宠物编辑器--完工\mainWin.ui")
        self.ui.setWindowTitle("桌面宠物编辑器v1.0.0")
        #print(self.ui.__dict__)

        self.mainDataLi = []
        """
        importList = list(self.ui.__dict__.items())[3:]
        for i in importList:
            print("self."+i[0]+" = self.ui."+i[0])
            eval("self."+i[0]+" = self.ui."+i[0])
        """

        #菜单组件导入
        self.PageButton1 = self.ui.PageButton1
        self.PageButton2 = self.ui.PageButton2
        self.PageButton3 = self.ui.PageButton3
        self.PageButton4 = self.ui.PageButton4
        self.newButton = self.ui.newFileButton
        self.openButton = self.ui.openFileButton
        self.saveButton = self.ui.saveFileButton
        self.aboutButton = self.ui.aboutButton
        self.stackWidget = self.ui.stackedWidget
        self.newFileButton = self.ui.newFileButton
        self.openFileButton = self.ui.openFileButton
        self.saveFileButton = self.ui.saveFileButton
        self.aboutButton = self.ui.aboutButton

        #宠物图像data导入
        self.startGif = self.ui.startGif
        self.normalGifFile = self.ui.normalGifFile
        self.clickGif = self.ui.clickGif
        self.startWindowSize = self.ui.startWindowSize
        self.petSize = self.ui.petSize
        self.petSize_click = self.ui.petSize_click
        self.mainDataLi.extend([self.startGif,self.normalGifFile,self.clickGif,self.startWindowSize,self.petSize,self.petSize_click])

        #宠物操作data导入
        self.dialoglist = self.ui.dialoglist
        self.clickTalk = self.ui.clickTalk
        self.changeGifTime_ms = self.ui.changeGifTime_ms
        self.changeTalkTime_ms = self.ui.changeTalkTime_ms
        self.isRandomPosition = self.ui.isRandomPosition
        self.isPetFollowMouse = self.ui.isPetFollowMouse
        self.clickShape = self.ui.clickShape
        self.mainDataLi.extend([self.dialoglist,self.clickTalk,self.changeGifTime_ms,self.changeTalkTime_ms,self.isRandomPosition,self.isPetFollowMouse,self.clickShape])

        #菜单data导入
        self.pallIcon = self.ui.pallIcon
        self.pallQuitIcon = self.ui.pallQuitIcon
        self.pallQuitName = self.ui.pallQuitName
        self.pallShowIcon = self.ui.pallShowIcon
        self.pallShowName = self.ui.pallShowName
        self.quitName = self.ui.quitName
        self.hideName = self.ui.hideName
        self.encodeSt = self.ui.encodeSt
        self.mainDataLi.extend([self.pallIcon,self.pallQuitIcon,self.pallQuitName,self.pallShowIcon,self.pallShowName,self.quitName,self.hideName,self.encodeSt])

        #页面data导入
        self.isStaysOnTopHint = self.ui.isStaysOnTopHint
        self.isAutoFillBackground = self.ui.isAutoFillBackground
        self.showTransparency = self.ui.showTransparency
        self.hideTransparency = self.ui.hideTransparency
        self.talkLableStyleSheet = self.ui.talkLableStyleSheet
        self.talkLableStyleSheet_click = self.ui.talkLableStyleSheet_click
        self.mainDataLi.extend([self.isStaysOnTopHint,self.isAutoFillBackground,self.showTransparency,self.hideTransparency,self.talkLableStyleSheet,self.talkLableStyleSheet_click])

        #额外数据添加
        self.CkShapeList = ["QtCore.Qt.ArrowCursor","QtCore.Qt.SizeAllCursor","QtCore.Qt.OpenHandCursor"]
        self.clickShape.addItem("箭头 ArrowCursor")
        self.clickShape.addItem("四角方向 SizeAllCursor")
        self.clickShape.addItem("张手 OpenHandCursor")

        #for i in self.mainDataLi:
        #    print(str(type(i)))
        #    pass

    def DataImport(self):
        f = open("项目\项目8--桌面宠物编辑器--完工\config.txt")
        self.configDict = eval(f.read())
        f.close()

        self.startGif.setText(self.configDict["startGif"])
        self.normalGifFile.setText(self.configDict["normalGifFile"])
        self.clickGif.setText(self.configDict["clickGif"])
        self.startWindowSize.setText(self.configDict["startWindowSize"])
        self.petSize.setText(self.configDict["petSize"])
        self.petSize_click.setText(self.configDict["petSize_click"])

        self.dialoglist.setText(self.configDict["dialoglist"])
        self.clickTalk.setText(self.configDict["clickTalk"])
        self.changeGifTime_ms.setText(self.configDict["changeGifTime_ms"])
        self.changeTalkTime_ms.setText(self.configDict["changeTalkTime_ms"])
        self.isRandomPosition.setChecked(self.configDict["isRandomPosition"])
        self.isPetFollowMouse.setChecked(self.configDict["isPetFollowMouse"])
        self.clickShape.setCurrentIndex(self.configDict["clickShape"][1])

        self.pallIcon.setText(self.configDict["pallIcon"])
        self.pallQuitIcon.setText(self.configDict["pallQuitIcon"])
        self.pallQuitName.setText(self.configDict["pallQuitName"])
        self.pallShowIcon.setText(self.configDict["pallShowIcon"])
        self.pallShowName.setText(self.configDict["pallShowName"])
        self.quitName.setText(self.configDict["quitName"])
        self.hideName.setText(self.configDict["hideName"])
        self.encodeSt.setText(self.configDict["encodeSt"])

        self.isStaysOnTopHint.setChecked(self.configDict["isStaysOnTopHint"])
        self.isAutoFillBackground.setChecked(self.configDict["isAutoFillBackground"])
        self.showTransparency.setValue(self.configDict["showTransparency"])
        self.hideTransparency.setValue(self.configDict["hideTransparency"])
        self.talkLableStyleSheet.setPlainText(self.configDict["talkLableStyleSheet"])
        self.talkLableStyleSheet_click.setPlainText(self.configDict["talkLableStyleSheet_click"])

    def setupUi(self):
        #左侧控制键切换页面
        self.PageButton1.clicked.connect(lambda:self.disPlayPage(0))
        self.PageButton2.clicked.connect(lambda:self.disPlayPage(1))
        self.PageButton3.clicked.connect(lambda:self.disPlayPage(2))
        self.PageButton4.clicked.connect(lambda:self.disPlayPage(3))

        #文件处理
        self.newButton.clicked.connect(lambda:self.newFile())
        self.openButton.clicked.connect(lambda:self.openFile())
        self.saveButton.clicked.connect(lambda:self.saveFile())
        self.aboutButton.clicked.connect(lambda:self.disPlayPage(4))

    def disPlayPage(self,pageNb):
        self.stackWidget.setCurrentIndex(pageNb)

    def saveFile(self):
        f = open("config.txt","w")
        rtdict = {}
        
        for i in self.mainDataLi:
            if "QLineEdit" in str(type(i)):
                rtdict[i.objectName()] = i.text()
            elif "QCheckBox" in str(type(i)):
                rtdict[i.objectName()] = i.isChecked()
            elif "QComboBox" in str(type(i)):
                rtdict[i.objectName()] = (self.CkShapeList[i.currentIndex()],i.currentIndex())
            elif "QDoubleSpinBox" in str(type(i)):
                rtdict[i.objectName()] = i.value()
            elif "QTextEdit" in str(type(i)):
                rtdict[i.objectName()] = i.toPlainText()
        f.write(str(rtdict))
        f.close()
        self.success()
        
        

    def newFile(self):  #TODO
        pass

    def openFile(self): #TODO
        pass

    def success(self):
        self.ui.setWindowTitle("保存成功！")
        time.sleep(2)
        self.ui.setWindowTitle("桌面宠物编辑器v1.0.0")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWin = mainWindow()
    mainWin.DataImport()
    mainWin.ui.show()

    sys.exit(app.exec_())
