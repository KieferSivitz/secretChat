from PyQt5 import QtCore, QtGui, QtWidgets
import sys, socket
from _thread import *

def __init__(self, root):
  self.server_socket = None
  self.serverStatus = 0
    
def app_version():
    msg_box("Application Version", "Null-Byte P2P Chat v1.0")

def msg_box(title, data):
    w = QtWidgets.QWidget()
    QtWidgets.QMessageBox.information(w, title, data)

def update_list(self, data):
    self.listWidget.addItem(data)
    print("\a")

def server_socket(self):
    try:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('', 6190))
        self.server_socket.listen(1)
    except socket.error as e:
        msg_box("Socket Error!", "Unable to Setup Local Socket, Port In Use")
        return

    while 1:
        conn, addr = self.server_socket.accept()

        incoming_ip = str(addr[0])
        current_chat_ip = self.lineEdit.text()

        if incoming_ip != current_chat_ip:
            conn.close()
        else: 
            data = conn.recv(4096)
            data.decode("utf-8")
            update_list(self, data)
            conn.close()

    self.server_socket.close()

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

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 346)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(340, 10, 61, 20))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 0, 241, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(410, 0, 241, 27))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 331, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 331, 201))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 210, 211, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        #############################################################
        # Executes when send message button is clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        #############################################################

        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 210, 121, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        #############################################################
        # Executes on clear log button click
        self.pushButton_4.clicked.connect(self.client_send_message)
        #############################################################

        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(330, 30, 321, 251))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setGeometry(QtCore.QRect(10, 10, 301, 241))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 27))
        self.menubar.setObjectName("menubar")
        self.menuMenu_Actions = QtWidgets.QMenu(self.menubar)
        self.menuMenu_Actions.setObjectName("menuMenu_Actions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionVersion = QtWidgets.QAction(MainWindow)
        self.actionVersion.setObjectName("actionVersion")

        ##############################################################
        # Executes when submenu item version is clicked
        self.actionVersion.triggered.connect(app_version)
        ##############################################################

        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")

        ##############################################################
        # Executes when the submenu item exit is clicked
        self.actionExit.triggered.connect(QtCore.QCoreApplication.instance().quit)
        ##############################################################

        self.menuMenu_Actions.addAction(self.actionVersion)
        self.menuMenu_Actions.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu_Actions.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Secret Chat"))
        self.label.setText(_translate("MainWindow", "IP Address:"))
        self.label_2.setText(_translate("MainWindow", "Nickname:"))
        self.pushButton_3.setText(_translate("MainWindow", "Send Message"))
        self.pushButton_4.setText(_translate("MainWindow", "Clear Logs"))
        self.menuMenu_Actions.setTitle(_translate("MainWindow", "Menu Actions"))
        self.actionVersion.setText(_translate("MainWindow", "Version"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def clear_logs(self):
        self.listWidget.clear()

    def start_server(self):
        start_new_thread(server_socket, (self,))

    def client_send_message(self):
        ip_address = self.lineEdit.text()

        nick = self.lineEdit_2.text()
        nick = nick.replace("#>", "")
        rmessage = self.textEdit.toPlainText()
        rmessage = rmessage.replace("#>", "")

        rmsg = nick + "#> " + rmessage


        try:
            #c.connect((ip_address, 6190))
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            c.connect((ip_address, 6190))
        except Exception as e:
            msg_box("Connection Refused", "The address you are trying to reach is currently unavailable")
            return

        try:
            c.send(rmsg)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except Exception as e:
            msg_box("Connection Refused", "The message cannot be sent. Endpoint not connected")

        c.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

