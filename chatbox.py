from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit,QLabel,QComboBox
from PyQt5.QtGui import QFont
import sys,sqlite3

class FirstWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100,100,300,200)
        self.ok=QPushButton("OK",self)
        self.font(self.ok,120,120)
        self.second=OlderChild()
        self.ok.clicked.connect(self.run)
        self.login=QLabel("Login",self)
        self.font(self.login,50,30)
        self.parol=QLabel("Parol",self)
        self.font(self.parol,50,80)
        self.loginb=QLineEdit(self)
        self.font(self.loginb,150,30)
        self.parolb=QLineEdit(self)
        self.font(self.parolb,150,80)
        self.error=QLabel("",self)
        self.font(self.error,113,160)
        #self.DataBase()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",12))
        obj.move(x,y)
    def run(self):
        if ((self.loginb.text()=="admin" and self.parolb.text()=="1122")) or ((self.loginb.text()=="user" and self.parolb.text()=="3344")):
            if self.error!="":
                self.error.clear()
                self.second.show()
            else:
                self.second.show()
        elif self.loginb.text()=="" and self.parolb.text()=="":
            self.error.setText("Unknown user")
            self.error.adjustSize()
        else:
            self.error.setText("Unknown user")
            self.error.adjustSize()
class OlderChild(QWidget):
    def __init__(self):
        super().__init__()
        self.con=sqlite3.connect("ChatBox.db")
        self.k=self.con.cursor()
        self.k.execute("CREATE TABLE IF NOT EXISTS chat(login TEXT, parol TEXT, chat_text TEXT)")
        self.setWindowTitle("Wassup",self)
        self.setGeometry(400,400,400,200)
        self.setWindowTitle("SecondWindow")
        self.back=QPushButton("Back",self)
        self.font(self.back,160,150)
        self.back.clicked.connect(self.run)
        self.person=QLabel("",self)
        self.font(self.person,50,0)
        self.iin=QLineEdit(self)
        self.iin.setPlaceholderText("in...")
        self.font(self.iin,50,20)
        self.out=QLineEdit(self)
        self.out.setPlaceholderText("out...")
        self.font(self.out,200,20)
        self.send=QPushButton("Send",self)
        self.font(self.send,160,110)
        self.send.clicked.connect(self.run2)
        self.select=QComboBox(self)
        self.font(self.select,163,70)
        self.select.addItems(["","admin","user"])
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",12))
        obj.move(x,y)
    def run(self):
        self.close()
    def run2(self):
        if self.select.currentText()=="admin":
            if self.out.text()!="":
                self.person.setText("admin's last message")
                self.person.adjustSize()
                a=self.out.text()
                self.k.execute("SELECT * FROM chat WHERE login='admin'")
                for times in self.k.fetchall():
                    self.iin.setText(times[2])
                self.k.execute("UPDATE chat SET login=?, parol=?, chat_text=? WHERE login=?",('admin','1122',a,'admin'))
                self.out.clear()
                self.con.commit()
            else:
                self.person.setText("admin's last message")
                self.person.adjustSize()
                self.k.execute("SELECT * FROM chat WHERE login='admin'")
                for times in self.k.fetchall():
                    self.iin.setText(times[2])
                self.con.commit()
        elif self.select.currentText()=="user":
            if self.out.text()!="":
                a=self.out.text()
                self.person.setText("user's last message")
                self.person.adjustSize()
                self.k.execute("SELECT * FROM chat WHERE login='user'")
                for times in self.k.fetchall():
                    self.iin.setText(times[2])
                self.k.execute("UPDATE chat SET login=?, parol=?, chat_text=? WHERE login=?",('user','3344',a,'user'))
                self.out.clear()
                self.con.commit()
            else:
                self.person.setText("user's last message")
                self.person.adjustSize()
                self.k.execute("SELECT * FROM chat WHERE login='user'")
                for times in self.k.fetchall():
                    self.iin.setText(times[2])
                self.con.commit()
app=QApplication(sys.argv)
a=FirstWindow()
a.show()
b=OlderChild()
app.exit(app.exec_())
b.con.close()
