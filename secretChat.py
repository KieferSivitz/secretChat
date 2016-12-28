from PyQt5 import QtCore, QtGui, QtWidgets
import sys, socket
from _thread import *    
try: 
    import ssl
except ImportError:
    msg_box("Import Error", "Unable to import SSL, your communications will not be secure")

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

def deal_with_client(connstream):
    data = connstream.recv(2048)
    print(data)
    while(data):
        print("test27")
        data = data.decode(encoding="utf-8")
        print("test29")
        update_list(self, data)
        print("test31")
        connstream.close()    
        print("test33")
        data = connstream.recv(4096)
        print("test35")


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
        #context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        #context.set_ciphers("ADH-AES256-SHA")
        #context.load_dh_params("dhparam.pem")
        connstream = ssl.wrap_socket(conn, 
                                    server_side="True", 
                                    certfile="server.crt", 
                                    keyfile="private.pem")

        #incoming_ip = str(addr[0])
        #current_chat_ip = self.lineEdit.text()

        try:
            deal_with_client(connstream)
        finally:
            connstream.shutdown(socket.SHUT_RDWR)
            connstream.close()

    self.server_socket.close()


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
        MainWindow.resize(655, 420)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 651, 31))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 0, 71, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(340, -1, 71, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(90, 0, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 0, 231, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 290, 561, 31))
        self.textEdit.setObjectName("textEdit")

        ############################################################
        # Sends message on enter pressed
        self.textEdit.returnPressed.connect(self.client_send_message)
        ############################################################

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 30, 651, 251))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(0, 10, 651, 241))
        self.listWidget.setObjectName("listWidget")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(570, 330, 81, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        #############################################################
        # Executes on clear log button click
        self.pushButton_4.clicked.connect(self.clear_logs)
        #############################################################

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 290, 81, 31))
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")

        #############################################################
        # Executes when send message button is clicked
        self.pushButton_3.clicked.connect(self.client_send_message)
        #############################################################

        
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
        self.pushButton_4.setText(_translate("MainWindow", "Clear Logs"))
        self.pushButton_3.setText(_translate("MainWindow", "Send"))
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
        nick = nick.replace(":", "")
        rmessage = self.textEdit.text()
        rmessage = rmessage.replace(":", "")

        rmsg = nick + ": " + rmessage
        encodedMessage = bytes(rmsg, encoding='utf-8')


        try:
            # Create Context and socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            wrappedSocket = ssl.wrap_socket(sock, 
                                            ca_certs="server.csr",
                                            cert_reqs=ssl.CERT_REQUIRED)
            wrappedSocket.connect((ip_address, 6190))
            print("217")

            print(repr(wrappedSocket.getpeername()))
            print(wrappedSocket.cipher())
            print(pprint.pformat(wrappedSocket.getpeercert()))
            
        except Exception as e:
            msg_box("Connection Refused", "The address you are trying to reach is currently unavailable")
            return

        try:
            #wrappedSocket.send(encodedMessage)
            wrappedSocket.write(encodedMessage)
            self.listWidget.addItem(rmsg)
            self.textEdit.setText("")
        except Exception as e:
            msg_box("Connection Refused", "The message cannot be sent. Endpoint not connected")

        wrappedSocket.close()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

