import sys
import os
import threading
import  datetime
import pyttsx3
from PyQt5 import QtWidgets
import Times.Time as Times
class ExamleApp(QtWidgets.QMainWindow,Times.Ui_MainWindow):
    def __init__(self):
        self.engine = pyttsx3.init()
        super().__init__()
        self.setupUi(self)
        self.lcdNumber.setDigitCount(8)
        threading.Thread(target=self.clock, args=()).start()
        self.pushButton.clicked.connect(self.click0)
 #       self.lcdNumber.clicked.connect(self.click1)
    def clock(self):
        while True:
            now = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
            self.lcdNumber.display(now)

    def click0(self):
        threading.Thread(target=self.sound0, args=()).start()

    def sound0(self):
        now = str(datetime.datetime.now().hour) + ':' + str(datetime.datetime.now().minute) + ':' + str(datetime.datetime.now().second)
        self.engine.say(now)
        self.engine.runAndWait()




app = QtWidgets.QApplication(sys.argv)
window = ExamleApp()
window.show()
app.exec_()