from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QTextEdit, QCheckBox, QComboBox, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QFont
import sys

from database import DataBase


# asosiy oyna start

class MainWin(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register Window")
        self.setGeometry(550, 70, 600, 900)
        self.setFixedSize(800, 900)
        self.db = DataBase()
        self.widgets()
        self.show()

    def font(self, ob, x, y):
        ob.setFont(QFont("Consolas", 24))
        ob.move(x, y)

    def widgets(self):
        self.message_box = QMessageBox(self)
        self.message_box.setText("Bunday foydaluvchi yoq")
        # login uchun label va ledit
        self.login_label = QLabel("Login:", self)
        self.font(self.login_label, 150, 200)
        self.login_ledit = QLineEdit(self)
        self.font(self.login_ledit, 300, 200)
        self.login_ledit.setPlaceholderText("     login")

        # parol uchun label va ledit
        self.parol_label = QLabel("Parol:", self)
        self.font(self.parol_label, 150, 300)
        self.parol_ledit = QLineEdit(self)
        self.parol_ledit.setEchoMode(QLineEdit.Password)
        self.font(self.parol_ledit, 300, 300)
        self.parol_ledit.setPlaceholderText("     parol")

        # parolni korinishi uchun
        self.showpassword_label = QLabel("show", self)
        self.showpassword_label.move(648, 295)
        self.showpassword = QCheckBox(self)
        self.showpassword.move(650, 315)
        self.showpassword.setStyleSheet('''
                                                QCheckBox::indicator
                                                {
                                                width : 30px;
                                                height : 30px;
                                                }
                                                ''')
        self.showpassword.toggled.connect(self.showit_or_hideit)

        # sendMessage va signUp uchun button
        self.btn_sendMessage = QPushButton("Send message", self)
        self.font(self.btn_sendMessage, 175, 400)
        self.btn_sendMessage.setStyleSheet('''QPushButton {
                                            padding: 10px;
                                            border: 2px solid #ffe;
                                            border-radius: 20px;
                                            background-color: rgb(10, 60, 68);
                                            color: #fff;
                                            }
                                            QPushButton:pressed {
                                            background-color: rgb(8, 50, 50);
                                            }
                                            ''')
        self.btn_sendMessage.clicked.connect(self.run_sendMessage)

        self.btn_signUp = QPushButton("Sign Up", self)
        self.font(self.btn_signUp, 475, 400)
        self.btn_signUp.setStyleSheet('''QPushButton {
                                            padding: 10px;
                                            border: 2px solid #ffe;
                                            border-radius: 20px;
                                            background-color: rgb(10, 60, 68);
                                            color: #fff;
                                            }
                                            QPushButton:pressed {
                                            background-color: #3daa73;
                                            }
                                            ''')
        self.btn_signUp.clicked.connect(self.run_signUp)

        # qowimca funksiyalar
    def showit_or_hideit(self):
        if self.showpassword.isChecked():
            self.parol_ledit.setEchoMode(QLineEdit.Normal)
        else:
            self.parol_ledit.setEchoMode(QLineEdit.Password)

        # btn bosilsa oynaga otish
        # sendMessage ga
    def run_sendMessage(self):
        my_login = self.login_ledit.text()
        lst = self.db.select()
        k = 1
        for i in lst:
            if self.login_ledit.text() in i and self.parol_ledit.text() in i:
                self.sendMessage = SendMessage(my_login)
                self.sendMessage.show()
                self.close()
                k = 1
                break
            else:
                k = 0

        if k != 1:
            self.message_box.show()
            self.login_ledit.clear()
            self.parol_ledit.clear()

        # signUp ga
    def run_signUp(self):
        self.signUp = SignUp()
        self.signUp.show()
        self.close()

# asosiy oyna end

#########################################################################################

# signUp oyna start

class SignUp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SignUp Window')
        self.setGeometry(550, 70, 600, 900)
        self.setFixedSize(800, 900)
        # database
        self.db = DataBase()
        self.widgets()
        self.show()

    def font(self, ob, x, y):
        ob.setFont(QFont("Consolas", 24))
        ob.move(x, y)

    def widgets(self):
        # Qmessage box
        self.messagebox = QMessageBox(self)
        self.messagebox.setText("Iltimos ma'lumotlarni toliq kiriting")

        # to back button
        self.btn_toback = QPushButton("<==", self)
        self.btn_toback.setStyleSheet('''QPushButton{
                                border: 1px solid #fff;
                                background-color: rgb(10, 60, 68);
                                padding: 10px;
                                border-radius: 19px;
                                color: #fff;
                                }''')
        self.btn_toback.clicked.connect(self.toback)

        # login uchun label va ledit
        self.login_label = QLabel("Login:", self)
        self.font(self.login_label, 150, 200)
        self.login_ledit = QLineEdit(self)
        self.font(self.login_ledit, 300, 200)
        self.login_ledit.setPlaceholderText("     login")

        # parol uchun label va ledit
        self.parol_label = QLabel("Parol:", self)
        self.font(self.parol_label, 150, 300)
        self.parol_ledit = QLineEdit(self)
        self.font(self.parol_ledit, 300, 300)
        self.parol_ledit.setPlaceholderText("     parol")


        # sign up (ro'yxatga olish uchun button)
        self.btn_signUp = QPushButton('Register', self)
        self.font(self.btn_signUp, 320, 400)
        self.btn_signUp.setStyleSheet('''QPushButton {
                                        padding: 10px;
                                        border: 2px solid #ffe;
                                        border-radius: 20px;
                                        background-color: rgb(10, 60, 68);
                                        color: #fff;
                                        }
                                        QPushButton:pressed {
                                        background-color: rgb(8, 50, 50);
                                        }
                                        ''')
        x = self.login_ledit.text()
        y = self.parol_ledit.text()
        self.btn_signUp.clicked.connect(self.mainWin)

    def mainWin(self):
        # malumotni database ga saqlawmiz
        if self.login_ledit.text() != "" and self.parol_ledit.text() != "":
            self.db.insert(self.login_ledit.text(), self.parol_ledit.text())
            self.mainWin = MainWin()
            self.mainWin.show()
            self.close()
            self.db.con.close()
        else:
            self.messagebox.show()

    # qowimca funksiyalar
    def toback(self):
        self.mainWin = MainWin()
        self.mainWin.show()
        self.close()

# signup oyna end


#########################################################################################


# SendMessage oyna start

class SendMessage(QWidget):
    def __init__(self,my_login):
        super().__init__()

        self.my_login = my_login
        self.setWindowTitle("Send Message")
        self.setGeometry(550, 70, 600, 900)
        self.setFixedSize(800, 900)
        self.db = DataBase()
        self.widgets()
        self.show()

    def font(self, ob, x, y):
        ob.setFont(QFont("Consolas", 24))
        ob.move(x, y)

    def widgets(self):

        # message box
        self.message_box = QMessageBox(self)
        self.message_box.setText("Habar yozmagansiz!")

        # xabar yozish uchun text line edit
        self.write_message = QTextEdit(self)
        self.write_message.setPlaceholderText("Write something.....")
        self.write_message.setGeometry(50, 50, 700, 600)
        self.font(self.write_message, 50, 50)

        # label comboboxni oldidagi
        self.for_who = QLabel("For Who?",self)
        self.font(self.for_who, 180, 705)

        # user tanlash uchun combo box
        self.user_combobox = QComboBox(self)
        self.user_combobox.setGeometry(280, 700, 200, 50)
        self.font(self.user_combobox, 350, 700)
        lst = self.db.select()
        for i in lst:
            if i[0] != self.my_login:
                self.user_combobox.addItem(i[0])



        # sendMessage va watchMessage uchun button
        self.btn_sendMessage = QPushButton("Send Message", self)
        self.font(self.btn_sendMessage, 75, 800)
        self.btn_sendMessage.setStyleSheet('''QPushButton {
                                                    padding: 10px;
                                                    border: 2px solid #ffe;
                                                    border-radius: 20px;
                                                    background-color: rgb(10, 60, 68);
                                                    color: #fff;
                                                    }
                                                    QPushButton:pressed {
                                                    background-color: #3daa73;
                                                    }
                                                    ''')
        self.btn_sendMessage.clicked.connect(self.send_message)

        self.btn_watchMessage = QPushButton("Watch messages", self)
        self.font(self.btn_watchMessage, 425, 800)
        self.btn_watchMessage.setStyleSheet('''QPushButton {
                                                    padding: 10px;
                                                    border: 2px solid #ffe;
                                                    border-radius: 20px;
                                                    background-color: rgb(10, 60, 68);
                                                    color: #fff;
                                                    }
                                                    QPushButton:pressed {
                                                    background-color: #3daa73;
                                                    }
                                                    ''')
        self.btn_watchMessage.clicked.connect(self.watch_message)

        self.btn_back = QPushButton("<==", self)
        self.btn_back.setStyleSheet('''QPushButton{
                                border: 1px solid #fff;
                                background-color: rgb(10, 60, 68);
                                padding: 10px;
                                border-radius: 19px;
                                color: #fff;
                                }''')
        self.btn_back.move(0, 0)
        self.btn_back.clicked.connect(self.toback)

## buttonlar uchin funksiyalar
#
## yozgan xabarni databasega joylashtirish
    def send_message(self):
        from_login = self.my_login
        for_login = self.user_combobox.currentText()
        message = self.write_message.toPlainText()
        if message != "":
            self.db.insert_message(from_login, for_login, message)
            self.write_message.clear()
        else:
            self.message_box.show()

## watch message oynasiga o'tish
    def watch_message(self):
        print('hi')
        self.watchMessage = WatchMessage(self.my_login)
        self.watchMessage.show()
        self.close()

    def toback(self):
        self.mainWin = MainWin()
        self.mainWin.show()
        self.close()

# SendMessage oyna end

#########################################################################################

# watchMessage oyna start

class WatchMessage(QWidget):
    def __init__(self, my_login):
        super().__init__()

        self.my_login = my_login
        self.setWindowTitle("Send Message")
        self.setGeometry(550, 70, 600, 900)
        self.setFixedSize(800, 900)
        self.db = DataBase()
        self.widgets()
        self.show()

    def font(self, ob, x, y):
        ob.setFont(QFont("Consolas", 24))
        ob.move(x, y)

    def widgets(self):

        # habarlarni korish uchun jadval
        self.table = QTableWidget(100, 2, self)
        self.table.setFont(QFont("Consoles", 20))
        self.table.setGeometry(50, 100, 700, 600)
        self.table.setHorizontalHeaderLabels(['FROM', 'MESSAGES'])
        self.table.setColumnWidth(1, 100)
        messages = self.db.select_my_messages()
        # jadvalni malumotlar b-n toldirish uchun
        self.table.setRowCount(len(self.db.select_my_messages()))
        row = 0
        for i in range(len(messages)):
            if messages[i][0] != self.my_login:
                self.table.setItem(row, 0, QTableWidgetItem(str(messages[i][0])))
                self.table.setItem(row, 1, QTableWidgetItem(str(messages[i][1])))
                row += 1


        # back uchun button
        self.btn_toback = QPushButton("<==", self)
        self.btn_toback.setStyleSheet('''QPushButton{
                                        border: 1px solid #fff;
                                        background-color: rgb(10, 60, 68);
                                        padding: 10px;
                                        border-radius: 19px;
                                        color: #fff;
                                        }''')
        self.btn_toback.clicked.connect(self.toback)



### buttonlar uchun funksiyalar
    #
    # orqaga qaytish(sendMessage ga)
    def toback(self):
        self.sendMessage = SendMessage(self.my_login)
        self.sendMessage.show()
        self.close()

# watchMessage oyna start






app = QApplication(sys.argv)
win = MainWin()
sys.exit(app.exec_())