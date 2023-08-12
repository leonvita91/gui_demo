import sys
from PyQt6.uic import loadUi
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QWidget



# Control everything on Welcome Screen
class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        loadUi('welcomescreen.ui',self)
        # if this btn clicked it will exec the func gotobtn
        self.login.clicked.connect(self.gotobtn_login)

    # go to the next screen 
    def gotobtn_login(self):
        login = LoginScreen()
        # add the LoginScreen class as widget
        widget.addWidget(login)
        # if the func exec it will move to the next index
        # which is LoginScreen class
        widget.setCurrentIndex(widget.currentIndex() + 1)

# Control everything in LoginScreen class
class LoginScreen(WelcomeScreen,QDialog):
    def __init__(self):
        super(LoginScreen,self).__init__()
        # load the UI of login Screen
        loadUi('login.ui',self)
        # hide the password field
        # this is works with pyqt6 not like pyqt5.
        self.passwordField.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        # clicked buttons
        # login btn
        self.btn_login2.clicked.connect(self.loginfunction)
        # if this clicked it will exec the goback func
        self.back_btn.clicked.connect(self.goback)

    def loginfunction(self,QtWidgets):
        username = self.usernameField.text()
        password = self.passwordField.text()
        if len(username)==0 or len(password)==0:
            self.error_message_1.setText('Empty Field !!')
        elif username == 'leon' and password == '12345':
            print('login seccessfully !!')
            #clear the messages
            self.error_message_1.setText('')
            self.error_message_2.setText('')
        else:
            self.error_message_2.setText('Invalid Username Or Password !!')
            self.error_message_1.setText('')
    # go back func
    def goback(self):
        logout = WelcomeScreen()
        # add the WelcomeScreen func as widget
        widget.addWidget(logout)
        # if this clicked it will take you to the back Screen which is WelcomeScreen
        widget.setCurrentIndex(widget.currentIndex() - 1)


# Main Section
app = QApplication(sys.argv)
welcome = WelcomeScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(750)
widget.setFixedHeight(600)
widget.show()

try:
    sys.exit(app.exec())
except:
    print("Exiting")