# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secretChat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys, socket
from thread import *
    
def app_version():
    msg_box("Application Version", "Null-Byte P2P Chat v1.0")

def msg_box(title, data):
    w = QtGui.QWidget()
    QtGui.QMessageBox.information(w, title, data)

def update_list(self, data):
    self.listWidget.addItem(data)
    print"\a"

def server_socket(self):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('', 6190))
        s.listen(1)
    except socket.error, e:
        msg_box("Socket Error!", "Unable to Setup Local Socket, Port In Use")
        return

    while 1:
        conn, addr = s.accept()

        incoming_ip = str(addr[0])
        current_chat_ip = self.lineEdit.text()

        if incoming_ip != current_chat_ip:
            conn.close()
        else: 
            data = conn.recv(4096)
            update_list(self, data)
            conn.close()

        s.close()

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        self.start_server()

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(655, 346)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 61, 20))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 0, 241, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 0, 241, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 331, 251))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.textEdit = QtGui.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 331, 201))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 210, 211, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        #############################################################
        # Executes when send message button is clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        #############################################################

        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 210, 121, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))

        #############################################################
        # Executes on clear log button click
        self.pushButton_4.clicked.connect(self.client_send_message)
        #############################################################

        self.frame_3 = QtGui.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 30, 321, 251))
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName(_fromUtf8("frame_3"))
        self.listWidget = QtGui.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 301, 241))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 27))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMenu_Actions = QtGui.QMenu(self.menubar)
        self.menuMenu_Actions.setObjectName(_fromUtf8("menuMenu_Actions"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtGui.QAction(MainWindow)
        self.actionVersion.setObjectName(_fromUtf8("actionVersion"))

        ##############################################################
        # Executes when submenu item version is clicked
        self.actionVersion.triggered.connect(app_version)
        ##############################################################

        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))

        ##############################################################
        # Executes when the submenu item exit is clicked
        #self.actionExit.triggered.connect(qApp.quit)
        ##############################################################

        self.menuMenu_Actions.addAction(self.actionVersion)
        self.menuMenu_Actions.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu_Actions.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "IP Address:", None))
        self.label_2.setText(_translate("MainWindow", "Nickname:", None))
        self.pushButton_3.setText(_translate("MainWindow", "Send Message", None))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Logs", None))
        self.menuMenu_Actions.setTitle(_translate("MainWindow", "Menu Actions", None))
        self.actionVersion.setText(_translate("MainWindow", "Version", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))

    def clear_logs(self):
        self.listWidget.clear()

    def start_server(self):
        start_new_thread(server_socket, (self,))
        msg_box("Success", "Server Started Successfully")

    def client_send_message(self):
        ip_address = self.lineEdit.text()

        nick = self.lineEdit_2.text()
        nick = nick.replace("#>", "")
        rmessage = self.textEdit.toPlainText()
        rmessage = rmessage.replace("#>", "")

        rmsg = nick + "#> " + rmessage

        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            c.connect((ip_address, 6190))
        except Exception, e:
            msg_box("Connection Refused", "The address you are trying to reach is currently unavailable")
            return

        try:
            c.send(rmsg)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except Exception, e:
            msg_box("Connection Refused", "The message cannot be sent. Endpoint not connected")

        c.close()

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

