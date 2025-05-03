from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMainWindow, QWidget, QMessageBox
from pickle import load,dump
from datetime import date
from PyQt6.QtCore import QTimer,Qt
from random import randint
from PyQt6.QtGui import QFont


import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# Your PyQt6 code here



input("Press Enter to exit...")
enr=dict(year=int,
         month=int,
         day=int,
         web=str)
def remplir():
    
    f= open("C:\Windows\System32\drivers\etc\hosts", "a")
    f1=open("text.txt","r")
    ch=f1.readline();
    while (ch!=""):
        
        f.write("127.0.0.1	"+ch+"\n")
        ch=f1.readline();
    f.close()
    f1.close()


def is_string_in_file( ):
    with open("C:\Windows\System32\drivers\etc\hosts", "r") as file:
        for line in file:
            if "tukif.com" in line:
                return True
    return False

# Example usage

if is_string_in_file()==False:
    
    remplir()
def word():
    t=['سبحان الله', 'الحمد لله', " لا إله إلا الله", 'الله أكبر', 'ولا حول ولا قوة إلا بالله']
    return t[randint(0,4)]
    
def update():
    from datetime import date
    f2=open("temp.dat","rb")
    t=[]
    while True:
        try:
            g=load(f2)
            t.append(g)
        except:
            break;
    d=date.today()
    for i in t:
        if over(d,i)==True:
            supp(i["web"]);
            t.remove(i);
    f2=open("temp.dat","wb")
    for i in t:
        dump(i,f2);
            

    
def over(d,e):
    if(d.year>e["year"]):
        return True
    if d.year==e["year"] and d.month>e["month"]:
        return True
    if d.year==e["year"] and d.month==e["month"] and d.day>e["day"]:
        return True;
    return False;

    
def supp(c):
    with open("C:\Windows\System32\drivers\etc\hosts", 'r') as file:
        lines = file.readlines()
        # Remove lines with the desired content
        
        ch=str(c)
        lines = [line for line in lines if line.find(ch)==-1]
        with open("C:\Windows\System32\drivers\etc\hosts", 'w') as file:
            file.writelines(lines)
def permant(v1,v2):
    f=open("C:\Windows\System32\drivers\etc\hosts","a");
    f.write("\n"+"127.0.0.1	"+v1+"\n");
    f.write("\n"+"127.0.0.1	"+v2+"\n");


def temp(v1,v2):
    
    f2=open("temp.dat","ab");
    permant(v1,v2)
    t=form.d.date()
    e=dict(enr)
    e["year"]=t.year()
    e["month"]=t.month()
    e["day"]=t.day()
    e["web"]=v1;
    dump(e,f2)    
def show_error_message(ch):
    error_message = ch
    message_box = QMessageBox()
    message_box.setIcon(QMessageBox.Icon.Critical)
    message_box.setWindowTitle("Error")
    message_box.setText(error_message)
    message_box.exec()       
 
def info():
    
    ch=form.l.text()
    if ch=="":
        show_error_message("empty text not allowed")
    else:
        if ch.find("www.")==-1:
            ch1="www."+ch
        else:
            ch1=ch.replace("www.","");
        if form.r1.isChecked()==form.r2.isChecked()==False:
            show_error_message("you have to choose an option (permantly or temporary)")
        else:
            if form.r1.isChecked():
                permant(ch,ch1);
            else:
                temp(ch,ch1)
                



if __name__ == '__main__':

    Form, Window = uic.loadUiType("CH-blocker.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)
    form.b.clicked.connect(info)
    label = QLabel("بسم الله الرحمان الرحيم", window)
    label.setGeometry(150, 20, 200, 30)
    font = QFont("Arial", 20)
    label.setFont(font)
    timer = QTimer()
    timer.setInterval(10000)
    def update_text():
        label.setText(word())

    #connect the QTimer's timeout signal to the update_text function
    timer.timeout.connect(update_text)

    timer.start()
    form.b1.clicked.connect(update)
    window.show()


    app.exec()
    print("press enter to exit")
