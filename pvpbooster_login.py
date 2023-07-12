from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser, sys, pvpbooster_menu

version = '1.0'
debug_info = True

class PushButton(QtWidgets.QPushButton):
    def __init__(self, parent, bg1, bg2, c1, c2):
        self.background_1 = bg1
        self.background_2 = bg2
        self.color_1 = c1
        self.color_2 = c2
        super().__init__(parent)
        self._animation = QtCore.QVariantAnimation(
            startValue=QtGui.QColor(self.background_2),
            endValue=QtGui.QColor(self.background_1),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._update_stylesheet(QtGui.QColor(self.background_1), QtGui.QColor(self.background_2))
        self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

    def _on_value_changed(self, color):
        foreground = (
            QtGui.QColor(self.color_1)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(self.color_2)
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background, foreground):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            color: %s;
            text-align: center;
            text-decoration: none;
            border: 1px solid %s;
            outline: 0;
        }
        """
            % (background.name(), foreground.name(), foreground.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(370, 420)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
        self.centralwidget.setStyleSheet("background-color: none;")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 350, 400))
        self.widget.setStyleSheet("QWidget {\n"
        "    background-color: rgb(30, 30 ,30);\n"
        "    border-radius: 20px;\n"
        "}")
        self.widget.setObjectName("widget")
        self.window_bar_frame = QtWidgets.QFrame(self.widget)
        self.window_bar_frame.setGeometry(QtCore.QRect(0, 0, 350, 35))
        self.window_bar_frame.setStyleSheet("QFrame {\n"
        "    background-color: rgb(0, 0, 0);\n"
        "    border-top-left-radius: 15px;\n"
        "    border-top-right-radius: 15px;\n"
        "    border-bottom-left-radius: 0px;\n"
        "    border-bottom-right-radius: 0px;\n"
        "    border-bottom: 1px solid rgb(40, 40, 40);\n"
        "}")
        self.window_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.window_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.window_bar_frame.setObjectName("window_bar_frame")
        self.window_bar_pvp_label = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_pvp_label.setGeometry(QtCore.QRect(20, 7, 25, 20))
        self.window_bar_pvp_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    color: white;\n"
        "    font: 11pt \"Bahnschrift SemiBold\";\n"
        "}")
        self.window_bar_pvp_label.setAlignment(QtCore.Qt.AlignCenter)
        self.window_bar_pvp_label.setObjectName("window_bar_pvp_label")
        self.window_bar_booster_label = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_booster_label.setGeometry(QtCore.QRect(45, 7, 50, 20))
        self.window_bar_booster_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    color: rgb(0, 255, 0);\n"
        "    font: 11pt \"Bahnschrift SemiBold\";\n"
        "}")
        self.window_bar_booster_label.setAlignment(QtCore.Qt.AlignCenter)
        self.window_bar_booster_label.setObjectName("window_bar_booster_label")
        self.window_bar_pvpbooster_przedzial_label = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_pvpbooster_przedzial_label.setGeometry(QtCore.QRect(110, 6, 1, 23))
        self.window_bar_pvpbooster_przedzial_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    background: rgb(30, 30, 30);\n"
        "}")
        self.window_bar_pvpbooster_przedzial_label.setText("")
        self.window_bar_pvpbooster_przedzial_label.setObjectName("window_bar_pvpbooster_przedzial_label")
        self.window_bar_witaj_label = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_witaj_label.setGeometry(QtCore.QRect(125, 7, 61, 20))
        self.window_bar_witaj_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    border-radius: none;\n"
        "    color: white;\n"
        "    font: 12pt \"Bahnschrift SemiBold\";\n"
        "}")
        self.window_bar_witaj_label.setObjectName("window_bar_witaj_label")
        self.window_bar_minimize_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
        self.window_bar_minimize_pushbutton.setGeometry(QtCore.QRect(280, 8, 20, 20))
        self.window_bar_minimize_pushbutton.setStyleSheet("QPushButton {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "    image: url(img/subtract.png);\n"
        "}")
        self.window_bar_minimize_pushbutton.setText("")
        self.window_bar_minimize_pushbutton.clicked.connect(lambda: self.showMinimized())
        self.window_bar_minimize_pushbutton.setObjectName("window_bar_minimize_pushbutton")
        self.window_bar_close_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
        self.window_bar_close_pushbutton.setGeometry(QtCore.QRect(310, 8, 20, 20))
        self.window_bar_close_pushbutton.setStyleSheet("QPushButton {\n"
        "    border: none;\n"
        "    background-color: none;\n"
        "    image: url(img/close.png);\n"
        "}")
        self.window_bar_close_pushbutton.setText("")
        self.window_bar_close_pushbutton.clicked.connect(lambda: self.close())
        #self.window_bar_close_pushbutton.clicked.connect(lambda: self.closeEvent(quit))
        self.window_bar_close_pushbutton.setObjectName("window_bar_close_pushbutton")
        self.window_bar_pvpbooster_przedzial_label_2 = QtWidgets.QLabel(self.window_bar_frame)
        self.window_bar_pvpbooster_przedzial_label_2.setGeometry(QtCore.QRect(265, 6, 1, 23))
        self.window_bar_pvpbooster_przedzial_label_2.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    background: rgb(30, 30, 30);\n"
        "}")
        self.window_bar_pvpbooster_przedzial_label_2.setText("")
        self.window_bar_pvpbooster_przedzial_label_2.setObjectName("window_bar_pvpbooster_przedzial_label_2")
        self.window_bar_pvpbooster_site_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
        self.window_bar_pvpbooster_site_pushbutton.setGeometry(QtCore.QRect(200, 8, 20, 20))
        self.window_bar_pvpbooster_site_pushbutton.setStyleSheet("QPushButton {\n"
        "    border-radius: 5px;\n"
        "    background-color: none;\n"
        "    image: url(img/website.png);\n"
        "}")
        self.window_bar_pvpbooster_site_pushbutton.setText("")
        self.window_bar_pvpbooster_site_pushbutton.clicked.connect(lambda: webbrowser.open('https://pvpbooster.pl', new=2))
        self.window_bar_pvpbooster_site_pushbutton.setObjectName("window_bar_pvpbooster_site_pushbutton")
        self.window_bar_discord_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
        self.window_bar_discord_pushbutton.setGeometry(QtCore.QRect(230, 8, 20, 20))
        self.window_bar_discord_pushbutton.setStyleSheet("QPushButton {\n"
        "    border-radius: 5px;\n"
        "    background-color: none;\n"
        "    image: url(img/discord.png);\n"
        "}")
        self.window_bar_discord_pushbutton.setText("")
        self.window_bar_discord_pushbutton.clicked.connect(lambda: webbrowser.open('https://discord.gg/sW5TmXPH74', new=2))
        self.window_bar_discord_pushbutton.setObjectName("window_bar_discord_pushbutton")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 35, 350, 365))
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.login_frame = QtWidgets.QFrame(self.login_page)
        self.login_frame.setGeometry(QtCore.QRect(50, 70, 250, 250))
        self.login_frame.setStyleSheet("QFrame {\n"
        "    background-color: rgb(40, 40, 40);\n"
        "    border: 2px solid rgb(20, 20, 20);\n"
        "    border-radius: 20px;\n"
        "}\n"
        "QLineEdit {\n"
        "    color: rgb(120, 255, 120);\n"
        "    border: 1px solid black;\n"
        "    border-radius: 10px;\n"
        "    padding: 1px 2px 2px 3px;\n"
        "}\n"
        "QPushButton {\n"
        "    color: rgb(120, 255, 120);\n"
        "    border: 1px solid black;\n"
        "    border-radius: 10px;\n"
        "}")
        self.login_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
        self.login_frame.setObjectName("login_frame")
        self.login_username_lineedit = QtWidgets.QLineEdit(self.login_frame)
        self.login_username_lineedit.setGeometry(QtCore.QRect(50, 30, 150, 25))
        self.login_username_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.login_username_lineedit.setObjectName("login_username_lineedit")
        self.login_password_lineedit = QtWidgets.QLineEdit(self.login_frame)
        self.login_password_lineedit.setGeometry(QtCore.QRect(50, 70, 150, 25))
        self.login_password_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.login_password_lineedit.setObjectName("login_password_lineedit")
        #self.login_submit_pushbutton = QtWidgets.QPushButton(self.login_frame)
        self.login_submit_pushbutton = PushButton(self.login_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78")
        self.login_submit_pushbutton.setGeometry(QtCore.QRect(30, 200, 80, 30))
        self.login_submit_pushbutton.clicked.connect(lambda: start())
        self.login_submit_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.login_submit_pushbutton.setObjectName("login_submit_pushbutton")
        #self.login_register_pushbutton = QtWidgets.QPushButton(self.login_frame)
        self.login_register_pushbutton = PushButton(self.login_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78")
        self.login_register_pushbutton.setGeometry(QtCore.QRect(140, 200, 80, 30))
        self.login_register_pushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.login_register_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.login_register_pushbutton.setObjectName("login_register_pushbutton")
        self.login_logowanie_label = QtWidgets.QLabel(self.login_page)
        self.login_logowanie_label.setGeometry(QtCore.QRect(130, 25, 90, 20))
        self.login_logowanie_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    border-radius: none;\n"
        "    color: white;\n"
        "    background-color: none;\n"
        "    font: 12pt \"Bahnschrift SemiBold\";\n"
        "}")
        self.login_logowanie_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
        self.login_logowanie_label.setObjectName("login_logowanie_label")
        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.register_frame = QtWidgets.QFrame(self.register_page)
        self.register_frame.setGeometry(QtCore.QRect(50, 70, 250, 250))
        self.register_frame.setStyleSheet("QFrame {\n"
        "    background-color: rgb(40, 40, 40);\n"
        "    border: 2px solid rgb(20, 20, 20);\n"
        "    border-radius: 20px;\n"
        "}\n"
        "QLineEdit {\n"
        "    color: rgb(120, 255, 120);\n"
        "    border: 1px solid black;\n"
        "    border-radius: 10px;\n"
        "    padding: 1px 2px 2px 3px;\n"
        "}\n"
        "QPushButton {\n"
        "    color: rgb(120, 255, 120);\n"
        "    border: 1px solid black;\n"
        "    border-radius: 10px;\n"
        "}")
        self.register_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
        self.register_frame.setObjectName("register_frame")
        self.register_email_lineedit = QtWidgets.QLineEdit(self.register_frame)
        self.register_email_lineedit.setGeometry(QtCore.QRect(50, 30, 150, 25))
        self.register_email_lineedit.setStyleSheet("QLineEdit {\n"
        "    border: 1px solid black;\n"
        "    border-radius: 10px;\n"
        "}")
        self.register_email_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_email_lineedit.setObjectName("register_email_lineedit")
        self.register_username_lineedit = QtWidgets.QLineEdit(self.register_frame)
        self.register_username_lineedit.setGeometry(QtCore.QRect(50, 70, 150, 25))
        self.register_username_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_username_lineedit.setObjectName("register_username_lineedit")
        #self.register_submit_pushbutton = QtWidgets.QPushButton(self.register_frame)
        self.register_submit_pushbutton = PushButton(self.register_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78")
        self.register_submit_pushbutton.setGeometry(QtCore.QRect(30, 200, 80, 30))
        self.register_submit_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_submit_pushbutton.setObjectName("register_submit_pushbutton")
        self.register_password_lineedit = QtWidgets.QLineEdit(self.register_frame)
        self.register_password_lineedit.setGeometry(QtCore.QRect(50, 110, 150, 25))
        self.register_password_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_password_lineedit.setObjectName("register_password_lineedit")
        self.register_key_lineedit = QtWidgets.QLineEdit(self.register_frame)
        self.register_key_lineedit.setGeometry(QtCore.QRect(50, 150, 150, 25))
        self.register_key_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_key_lineedit.setObjectName("register_key_lineedit")
        self.register_login_pushbutton = PushButton(self.register_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78")
        self.register_login_pushbutton.setGeometry(QtCore.QRect(140, 200, 80, 30))
        self.register_login_pushbutton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.register_login_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
        self.register_login_pushbutton.setObjectName("register_login_pushbutton")
        self.register_rejestracja_label = QtWidgets.QLabel(self.register_page)
        self.register_rejestracja_label.setGeometry(QtCore.QRect(130, 25, 90, 20))
        self.register_rejestracja_label.setStyleSheet("QLabel {\n"
        "    border: none;\n"
        "    border-radius: none;\n"
        "    color: white;\n"
        "    background-color: none;\n"
        "    font: 12pt \"Bahnschrift SemiBold\";\n"
        "}")
        self.register_rejestracja_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
        self.register_rejestracja_label.setObjectName("register_rejestracja_label")
        self.stackedWidget.addWidget(self.register_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.window_bar_pvp_label.setText(_translate("MainWindow", "pvp"))
        self.window_bar_booster_label.setText(_translate("MainWindow", "booster"))
        self.window_bar_witaj_label.setText(_translate("MainWindow", "Witaj!"))
        self.login_username_lineedit.setPlaceholderText(_translate("MainWindow", "username"))
        self.login_password_lineedit.setPlaceholderText(_translate("MainWindow", "password"))
        self.login_submit_pushbutton.setText(_translate("MainWindow", "Zaloguj"))
        self.login_register_pushbutton.setText(_translate("MainWindow", "Rejestracja"))
        self.login_logowanie_label.setText(_translate("MainWindow", "Logowanie"))
        self.register_email_lineedit.setPlaceholderText(_translate("MainWindow", "email"))
        self.register_username_lineedit.setPlaceholderText(_translate("MainWindow", "username"))
        self.register_submit_pushbutton.setText(_translate("MainWindow", "Zarejestruj"))
        self.register_password_lineedit.setPlaceholderText(_translate("MainWindow", "password"))
        self.register_key_lineedit.setPlaceholderText(_translate("MainWindow", "key"))
        self.register_login_pushbutton.setText(_translate("MainWindow", "Logowanie"))
        self.register_rejestracja_label.setText(_translate("MainWindow", "Rejestracja"))

class MoveWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.offset = None
        self.window_bar_frame.installEventFilter(self)

    def eventFilter(self, source, event):
        if source == self.window_bar_frame:
            if event.type() == QtCore.QEvent.MouseButtonPress:
                self.offset = event.pos()
            elif event.type() == QtCore.QEvent.MouseMove and self.offset is not None:
                self.move(self.pos() - self.offset + event.pos())
                return True
            elif event.type() == QtCore.QEvent.MouseButtonRelease:
                self.offset = None
        return super().eventFilter(source, event)

def start():
    w.close()
    w2 = pvpbooster_menu.MoveWindow()
    pvpbooster_menu.main_window = w2
    w2.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    w = MoveWindow()
    w.show()
    sys.exit(app.exec_())
