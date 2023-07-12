from PyQt5 import QtCore, QtGui, QtWidgets
import webbrowser, win32gui

debug_info = True
license_type = ''
license_expire = ''
username = ''
personal_id = 0
main_window = ''
last_clicker_status = ''

#PushButton(self.login_page, "#4CAF50", "#1e1e1e", "black", "#78ff78")
class SubmitPushButton(QtWidgets.QPushButton):
    def __init__(self, parent, bg1, bg2):
        #bg1 = background-color
        #bg2 = background-color:hover
        
        self.background_1 = bg1
        self.background_2 = bg2
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
            QtGui.QColor(self.background_1)
            if self._animation.direction() == QtCore.QAbstractAnimation.Forward
            else QtGui.QColor(self.background_2)
        )
        self._update_stylesheet(color, foreground)

    def _update_stylesheet(self, background):

        self.setStyleSheet(
            """
        QPushButton{
            background-color: %s;
            border: none;
            border-radius: 10px;
            image: url(img/done.png);
            border: 2px solid rgb(20, 20, 20);
        }
        """
            % (background.name())
        )

    def enterEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Backward)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.setDirection(QtCore.QAbstractAnimation.Forward)
        self._animation.start()
        super().leaveEvent(event)

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
            border-radius: 10px;
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
        
        def __init__(self) -> None:
            super().__init__
        
        gui_color = "green"
        shadow_color = [0, 200, 0, 200]
        windows_found = []


        def miner_komendy_listwidget(self, mode):
                if mode == "add":
                        self.items = []
                        for x in range(self.miner_ustawienia_komendy_listwidget.count()):
                                self.items.append(self.miner_ustawienia_komendy_listwidget.item(x).text())
                        if self.miner_ustawienia_komenda_lineedit.text() != "" and self.miner_ustawienia_ilosc_okrazen_spinbox.value() != 0:
                                if f"{self.miner_ustawienia_komenda_lineedit.text()} [{self.miner_ustawienia_ilosc_okrazen_spinbox.value()}]" in self.items:
                                        pass
                                else:
                                        self.miner_ustawienia_komendy_listwidget.addItem(f"{self.miner_ustawienia_komenda_lineedit.text()} [{self.miner_ustawienia_ilosc_okrazen_spinbox.value()}]")
                        self.miner_ustawienia_komenda_lineedit.setText("")
                        self.miner_ustawienia_ilosc_okrazen_spinbox.setValue(0)
                elif mode == "clear":
                        self.miner_ustawienia_komendy_listwidget.clear()

        def get_windows_name(self, hwnd, ctx ):
                window_text = win32gui.GetWindowText(hwnd)
                if win32gui.IsWindowVisible( hwnd ):
                        if "Minecraft 1" in window_text:
                                if "-" in window_text:
                                        pass
                                else:
                                        if f'{hwnd}:{window_text}' in self.windows_found:
                                                pass
                                        else:
                                                self.windows_found.append(f"{hwnd}:{window_text}")
        
        def miner_wykrywanie_okien(self):
                self.windows_found = []
                win32gui.EnumWindows(self.get_windows_name, None )
                self.miner_wykryte_okna_listwidget.clear()
                for window_name in self.windows_found:
                        self.miner_wykryte_okna_listwidget.addItem(window_name)


        def change_page_main(self):
                self.stackedWidget.setCurrentIndex(0)
                self.window_bar_status_label.setText("Strona główna")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))

        def change_page_clicker(self):
                self.stackedWidget.setCurrentIndex(1)
                self.window_bar_status_label.setText("Clicker")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                
        def change_page_miner(self):
                self.stackedWidget.setCurrentIndex(2)
                self.window_bar_status_label.setText("Miner")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                
        def change_page_premium(self):
                self.stackedWidget.setCurrentIndex(3)
                self.window_bar_status_label.setText("Premium")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                
        def change_page_ustawienia(self):
                self.stackedWidget.setCurrentIndex(4)
                self.window_bar_status_label.setText("Ustawienia")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                        
        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(980, 680)
                MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
                MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.centralwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.centralwidget.setStyleSheet("background-color: none;")
                self.widget = QtWidgets.QWidget(self.centralwidget)
                self.widget.setGeometry(QtCore.QRect(40, 40, 900, 600))
                self.widget.setStyleSheet("QWidget {\n"
                "    background-color: rgb(30, 30 ,30);\n"
                "    border-radius: 20px;\n"
                "}")
                self.widget.setObjectName("widget")
                self.stackedWidget = QtWidgets.QStackedWidget(self.widget)
                self.stackedWidget.setGeometry(QtCore.QRect(80, 35, 811, 561))
                self.stackedWidget.setStyleSheet("")
                self.stackedWidget.setObjectName("stackedWidget")
                self.main_page = QtWidgets.QWidget()
                self.main_page.setObjectName("main_page")
                self.main_witaj_nick_label = QtWidgets.QLabel(self.main_page)
                self.main_witaj_nick_label.setGeometry(QtCore.QRect(30, 20, 221, 50))
                self.main_witaj_nick_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 15pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_witaj_nick_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_witaj_nick_label.setObjectName("main_witaj_nick_label")
                self.main_online_label = QtWidgets.QLabel(self.main_page)
                self.main_online_label.setGeometry(QtCore.QRect(720, 10, 41, 30))
                self.main_online_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_online_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_online_label.setObjectName("main_online_label")
                self.main_online_count_label = QtWidgets.QLabel(self.main_page)
                self.main_online_count_label.setGeometry(QtCore.QRect(763, 10, 31, 30))
                self.main_online_count_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: rgb(0,255,0);\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_online_count_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_online_count_label.setObjectName("main_online_count_label")
                self.main_statystyki_label = QtWidgets.QLabel(self.main_page)
                self.main_statystyki_label.setGeometry(QtCore.QRect(60, 100, 81, 30))
                self.main_statystyki_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_label.setObjectName("main_statystyki_label")
                self.main_statystyki_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_frame = QtWidgets.QFrame(self.main_page)
                self.main_statystyki_frame.setGeometry(QtCore.QRect(40, 140, 470, 300))
                self.main_statystyki_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(36, 36, 36);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}\n"
                "QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 10px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.main_statystyki_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.main_statystyki_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.main_statystyki_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.main_statystyki_frame.setObjectName("main_statystyki_frame")
                self.main_statystyki_nick_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_label.setGeometry(QtCore.QRect(60, 20, 30, 20))
                self.main_statystyki_nick_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_label.setObjectName("main_statystyki_nick_label")
                self.main_statystyki_kamien_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_label.setGeometry(QtCore.QRect(160, 20, 50, 20))
                self.main_statystyki_kamien_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_label.setObjectName("main_statystyki_kamien_label")
                self.main_statystyki_kratki_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_label.setGeometry(QtCore.QRect(240, 20, 40, 20))
                self.main_statystyki_kratki_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_label.setObjectName("main_statystyki_kratki_label")
                self.main_statystyki_pieniadze_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_label.setGeometry(QtCore.QRect(320, 20, 60, 20))
                self.main_statystyki_pieniadze_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_label.setObjectName("main_statystyki_pieniadze_label")
                self.main_statystyki_kille_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_label.setGeometry(QtCore.QRect(400, 20, 30, 20))
                self.main_statystyki_kille_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_label.setObjectName("main_statystyki_kille_label")
                self.main_statystyki_top_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_label.setGeometry(QtCore.QRect(23, 20, 30, 20))
                self.main_statystyki_top_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_label.setObjectName("main_statystyki_top_label")
                self.main_statystyki_top_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_1_label.setGeometry(QtCore.QRect(25, 60, 20, 20))
                self.main_statystyki_top_1_label.setStyleSheet("QLabel {\n"
                "    color: gold;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_1_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_1_label.setObjectName("main_statystyki_top_1_label")
                self.main_statystyki_top_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_2_label.setGeometry(QtCore.QRect(25, 90, 20, 20))
                self.main_statystyki_top_2_label.setStyleSheet("QLabel {\n"
                "    color: silver;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_2_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_2_label.setObjectName("main_statystyki_top_2_label")
                self.main_statystyki_top_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_3_label.setGeometry(QtCore.QRect(25, 120, 20, 20))
                self.main_statystyki_top_3_label.setStyleSheet("QLabel {\n"
                "    color: brown;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_3_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_3_label.setObjectName("main_statystyki_top_3_label")
                self.main_statystyki_top_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_4_label.setGeometry(QtCore.QRect(25, 150, 20, 20))
                self.main_statystyki_top_4_label.setStyleSheet("QLabel {\n"
                "    color: grey;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_4_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_4_label.setObjectName("main_statystyki_top_4_label")
                self.main_statystyki_top_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_5_label.setGeometry(QtCore.QRect(25, 180, 20, 20))
                self.main_statystyki_top_5_label.setStyleSheet("QLabel {\n"
                "    color: grey;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_5_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_5_label.setObjectName("main_statystyki_top_5_label")
                self.main_statystyki_top_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_6_label.setGeometry(QtCore.QRect(25, 210, 20, 20))
                self.main_statystyki_top_6_label.setStyleSheet("QLabel {\n"
                "    color: grey;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_6_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_6_label.setObjectName("main_statystyki_top_6_label")
                self.main_statystyki_top_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_top_7_label.setGeometry(QtCore.QRect(25, 240, 20, 20))
                self.main_statystyki_top_7_label.setStyleSheet("QLabel {\n"
                "    color: grey;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_top_7_label.setAlignment(QtCore.Qt.AlignCenter)
                self.main_statystyki_top_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_top_7_label.setObjectName("main_statystyki_top_7_label")
                self.main_statystyki_nick_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_1_label.setGeometry(QtCore.QRect(60, 60, 91, 20))
                self.main_statystyki_nick_1_label.setStyleSheet("QLabel {\n"
                "    color: gold;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_1_label.setObjectName("main_statystyki_nick_1_label")
                self.main_statystyki_kamien_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_1_label.setGeometry(QtCore.QRect(160, 60, 71, 20))
                self.main_statystyki_kamien_1_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_1_label.setObjectName("main_statystyki_kamien_1_label")
                self.main_statystyki_kratki_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_1_label.setGeometry(QtCore.QRect(240, 60, 71, 20))
                self.main_statystyki_kratki_1_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_1_label.setObjectName("main_statystyki_kratki_1_label")
                self.main_statystyki_pieniadze_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_1_label.setGeometry(QtCore.QRect(320, 60, 51, 20))
                self.main_statystyki_pieniadze_1_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_1_label.setObjectName("main_statystyki_pieniadze_1_label")
                self.main_statystyki_kille_1_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_1_label.setGeometry(QtCore.QRect(400, 60, 41, 20))
                self.main_statystyki_kille_1_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_1_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_1_label.setObjectName("main_statystyki_kille_1_label")
                self.main_statystyki_nick_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_2_label.setGeometry(QtCore.QRect(60, 90, 91, 20))
                self.main_statystyki_nick_2_label.setStyleSheet("QLabel {\n"
                "    color: silver;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_2_label.setObjectName("main_statystyki_nick_2_label")
                self.main_statystyki_nick_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_3_label.setGeometry(QtCore.QRect(60, 120, 91, 20))
                self.main_statystyki_nick_3_label.setStyleSheet("QLabel {\n"
                "    color: brown;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_3_label.setObjectName("main_statystyki_nick_3_label")
                self.main_statystyki_nick_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_4_label.setGeometry(QtCore.QRect(60, 150, 91, 20))
                self.main_statystyki_nick_4_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_4_label.setObjectName("main_statystyki_nick_4_label")
                self.main_statystyki_nick_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_5_label.setGeometry(QtCore.QRect(60, 180, 91, 20))
                self.main_statystyki_nick_5_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_5_label.setObjectName("main_statystyki_nick_5_label")
                self.main_statystyki_nick_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_6_label.setGeometry(QtCore.QRect(60, 210, 91, 20))
                self.main_statystyki_nick_6_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_6_label.setObjectName("main_statystyki_nick_6_label")
                self.main_statystyki_nick_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_nick_7_label.setGeometry(QtCore.QRect(60, 240, 91, 20))
                self.main_statystyki_nick_7_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_nick_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_nick_7_label.setObjectName("main_statystyki_nick_7_label")
                self.main_statystyki_kamien_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_2_label.setGeometry(QtCore.QRect(160, 90, 71, 20))
                self.main_statystyki_kamien_2_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_2_label.setObjectName("main_statystyki_kamien_2_label")
                self.main_statystyki_kamien_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_3_label.setGeometry(QtCore.QRect(160, 120, 71, 20))
                self.main_statystyki_kamien_3_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_3_label.setObjectName("main_statystyki_kamien_3_label")
                self.main_statystyki_kamien_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_4_label.setGeometry(QtCore.QRect(160, 150, 71, 20))
                self.main_statystyki_kamien_4_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_4_label.setObjectName("main_statystyki_kamien_4_label")
                self.main_statystyki_kamien_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_5_label.setGeometry(QtCore.QRect(160, 180, 71, 20))
                self.main_statystyki_kamien_5_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_5_label.setObjectName("main_statystyki_kamien_5_label")
                self.main_statystyki_kamien_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_6_label.setGeometry(QtCore.QRect(160, 210, 71, 20))
                self.main_statystyki_kamien_6_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_6_label.setObjectName("main_statystyki_kamien_6_label")
                self.main_statystyki_kamien_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kamien_7_label.setGeometry(QtCore.QRect(160, 240, 71, 20))
                self.main_statystyki_kamien_7_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kamien_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kamien_7_label.setObjectName("main_statystyki_kamien_7_label")
                self.main_statystyki_kratki_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_2_label.setGeometry(QtCore.QRect(240, 90, 71, 20))
                self.main_statystyki_kratki_2_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_2_label.setObjectName("main_statystyki_kratki_2_label")
                self.main_statystyki_kratki_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_3_label.setGeometry(QtCore.QRect(240, 120, 71, 20))
                self.main_statystyki_kratki_3_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_3_label.setObjectName("main_statystyki_kratki_3_label")
                self.main_statystyki_kratki_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_4_label.setGeometry(QtCore.QRect(240, 150, 71, 20))
                self.main_statystyki_kratki_4_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_4_label.setObjectName("main_statystyki_kratki_4_label")
                self.main_statystyki_kratki_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_5_label.setGeometry(QtCore.QRect(240, 180, 71, 20))
                self.main_statystyki_kratki_5_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_5_label.setObjectName("main_statystyki_kratki_5_label")
                self.main_statystyki_kratki_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_6_label.setGeometry(QtCore.QRect(240, 210, 71, 20))
                self.main_statystyki_kratki_6_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_6_label.setObjectName("main_statystyki_kratki_6_label")
                self.main_statystyki_kratki_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kratki_7_label.setGeometry(QtCore.QRect(240, 240, 71, 20))
                self.main_statystyki_kratki_7_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kratki_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kratki_7_label.setObjectName("main_statystyki_kratki_7_label")
                self.main_statystyki_pieniadze_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_2_label.setGeometry(QtCore.QRect(320, 90, 51, 20))
                self.main_statystyki_pieniadze_2_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_2_label.setObjectName("main_statystyki_pieniadze_2_label")
                self.main_statystyki_pieniadze_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_3_label.setGeometry(QtCore.QRect(320, 120, 51, 20))
                self.main_statystyki_pieniadze_3_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_3_label.setObjectName("main_statystyki_pieniadze_3_label")
                self.main_statystyki_pieniadze_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_4_label.setGeometry(QtCore.QRect(320, 150, 51, 20))
                self.main_statystyki_pieniadze_4_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_4_label.setObjectName("main_statystyki_pieniadze_4_label")
                self.main_statystyki_pieniadze_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_5_label.setGeometry(QtCore.QRect(320, 180, 51, 20))
                self.main_statystyki_pieniadze_5_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_5_label.setObjectName("main_statystyki_pieniadze_5_label")
                self.main_statystyki_pieniadze_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_6_label.setGeometry(QtCore.QRect(320, 210, 51, 20))
                self.main_statystyki_pieniadze_6_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_6_label.setObjectName("main_statystyki_pieniadze_6_label")
                self.main_statystyki_pieniadze_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_pieniadze_7_label.setGeometry(QtCore.QRect(320, 240, 51, 20))
                self.main_statystyki_pieniadze_7_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_pieniadze_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_pieniadze_7_label.setObjectName("main_statystyki_pieniadze_7_label")
                self.main_statystyki_kille_2_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_2_label.setGeometry(QtCore.QRect(400, 90, 41, 20))
                self.main_statystyki_kille_2_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_2_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_2_label.setObjectName("main_statystyki_kille_2_label")
                self.main_statystyki_kille_3_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_3_label.setGeometry(QtCore.QRect(400, 120, 41, 20))
                self.main_statystyki_kille_3_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_3_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_3_label.setObjectName("main_statystyki_kille_3_label")
                self.main_statystyki_kille_4_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_4_label.setGeometry(QtCore.QRect(400, 150, 41, 20))
                self.main_statystyki_kille_4_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_4_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_4_label.setObjectName("main_statystyki_kille_4_label")
                self.main_statystyki_kille_5_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_5_label.setGeometry(QtCore.QRect(400, 180, 41, 20))
                self.main_statystyki_kille_5_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_5_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_5_label.setObjectName("main_statystyki_kille_5_label")
                self.main_statystyki_kille_6_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_6_label.setGeometry(QtCore.QRect(400, 210, 41, 20))
                self.main_statystyki_kille_6_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_6_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_6_label.setObjectName("main_statystyki_kille_6_label")
                self.main_statystyki_kille_7_label = QtWidgets.QLabel(self.main_statystyki_frame)
                self.main_statystyki_kille_7_label.setGeometry(QtCore.QRect(400, 240, 41, 20))
                self.main_statystyki_kille_7_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_statystyki_kille_7_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_statystyki_kille_7_label.setObjectName("main_statystyki_kille_7_label")
                
                self.main_lista_zmian_listwidget = QtWidgets.QListWidget(self.main_page)
                self.main_lista_zmian_listwidget.setGeometry(QtCore.QRect(540, 140, 240, 300))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift SemiBold")
                self.main_lista_zmian_listwidget.setFont(font)
                self.main_lista_zmian_listwidget.setStyleSheet("QListWidget {\n"
                "    outline: 0;\n"
                "    background-color: rgb(40, 40, 40);\n"
                "    border-radius: 15px;\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    color: white;\n"
                "    padding-top: 10px;\n"
                "    padding-bottom: 10px;\n"
                "    padding-left: 10px;\n"
                "    padding-right: 10px;\n"
                "}\n"
                "QListView::item {\n"
                "    border: 0px;\n"
                "    outline: 0;\n"
                "}\n"
                "\n"
                "QScrollBar:vertical {\n"
                "    background-color: rgb(40, 40, 40);\n"
                "    width: 10px;\n"
                "    border: 0px;\n"
                "}\n"
                "QScrollBar::handle:vertical {    \n"
                "    background-color: rgb(120, 255, 120);\n"
                "    width: 10px;\n"
                "    border-radius: 5px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::sub-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::add-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}")
                self.main_lista_zmian_listwidget.setSpacing(2)
                self.main_lista_zmian_listwidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
                self.main_lista_zmian_listwidget.setTextElideMode(QtCore.Qt.ElideMiddle)
                self.main_lista_zmian_listwidget.setResizeMode(QtWidgets.QListView.Adjust)
                self.main_lista_zmian_listwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.main_lista_zmian_listwidget.setObjectName("main_lista_zmian_listwidget")
                item = QtWidgets.QListWidgetItem()
                self.main_lista_zmian_listwidget.addItem(item)
                item = QtWidgets.QListWidgetItem()
                self.main_lista_zmian_listwidget.addItem(item)
                item = QtWidgets.QListWidgetItem()
                self.main_lista_zmian_listwidget.addItem(item)
                item = QtWidgets.QListWidgetItem()
                self.main_lista_zmian_listwidget.addItem(item)
                self.main_lista_zmian_label = QtWidgets.QLabel(self.main_page)
                self.main_lista_zmian_label.setGeometry(QtCore.QRect(560, 100, 101, 30))
                self.main_lista_zmian_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_lista_zmian_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_lista_zmian_label.setObjectName("main_lista_zmian_label")
                self.main_plan_label = QtWidgets.QLabel(self.main_page)
                self.main_plan_label.setGeometry(QtCore.QRect(90, 500, 170, 30))
                self.main_plan_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_plan_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_plan_label.setObjectName("main_plan_label")
                self.main_licencja_label = QtWidgets.QLabel(self.main_page)
                self.main_licencja_label.setGeometry(QtCore.QRect(300, 500, 170, 30))
                self.main_licencja_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_licencja_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_licencja_label.setObjectName("main_licencja_label")
                self.main_wersja_label = QtWidgets.QLabel(self.main_page)
                self.main_wersja_label.setGeometry(QtCore.QRect(540, 500, 170, 30))
                self.main_wersja_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.main_wersja_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.main_wersja_label.setObjectName("main_wersja_label")
                
                #CLICKER
                self.stackedWidget.addWidget(self.main_page)
                self.clicker_page = QtWidgets.QWidget()
                self.clicker_page.setObjectName("clicker_page")
                #CLICKER_STATUS_FRAME
                self.clicker_status_frame = QtWidgets.QFrame(self.clicker_page)
                self.clicker_status_frame.setGeometry(QtCore.QRect(20, 20, 340, 80))
                self.clicker_status_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.clicker_status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.clicker_status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.clicker_status_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_status_frame.setObjectName("clicker_status_frame")
                self.clicker_status_label = QtWidgets.QLabel(self.clicker_status_frame)
                self.clicker_status_label.setGeometry(QtCore.QRect(20, 25, 50, 30))
                self.clicker_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_status_label.setObjectName("clicker_status_label")
                self.clicker_status_current_label = QtWidgets.QLabel(self.clicker_status_frame)
                self.clicker_status_current_label.setGeometry(QtCore.QRect(70, 25, 31, 30))
                self.clicker_status_current_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_status_current_label.setObjectName("clicker_status_current_label")
                self.clicker_status_current_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_status_start_pushbutton = PushButton(self.clicker_status_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.clicker_status_start_pushbutton.setGeometry(QtCore.QRect(140, 25, 80, 30))
                self.clicker_status_start_pushbutton.clicked.connect(lambda: self.start_clicker(1))
                self.clicker_status_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_status_start_pushbutton.setObjectName("clicker_status_start_pushbutton")
                self.clicker_status_stop_pushbutton = PushButton(self.clicker_status_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.clicker_status_stop_pushbutton.setGeometry(QtCore.QRect(240, 25, 80, 30))
                self.clicker_status_stop_pushbutton.clicked.connect(lambda: self.start_clicker(2))
                self.clicker_status_stop_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_status_stop_pushbutton.setObjectName("clicker_status_stop_pushbutton")
                self.clicker_bindy_frame = QtWidgets.QFrame(self.clicker_page)
                self.clicker_bindy_frame.setGeometry(QtCore.QRect(380, 20, 420, 110))
                self.clicker_bindy_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.clicker_bindy_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.clicker_bindy_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.clicker_bindy_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_bindy_frame.setObjectName("clicker_bindy_frame")
                self.clicker_bindy_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bindy_label.setGeometry(QtCore.QRect(20, 10, 40, 25))
                self.clicker_bindy_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bindy_label.setAlignment(QtCore.Qt.AlignCenter)
                self.clicker_bindy_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bindy_label.setObjectName("clicker_bindy_label")
                self.clicker_bind_clicker_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bind_clicker_label.setGeometry(QtCore.QRect(70, 30, 51, 31))
                self.clicker_bind_clicker_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bind_clicker_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bind_clicker_label.setObjectName("clicker_bind_clicker_label")
                self.clicker_bind_fakelag_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bind_fakelag_label.setGeometry(QtCore.QRect(180, 30, 51, 31))
                self.clicker_bind_fakelag_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bind_fakelag_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bind_fakelag_label.setObjectName("clicker_bind_fakelag_label")
                self.clicker_bind_komenda_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bind_komenda_label.setGeometry(QtCore.QRect(290, 30, 61, 31))
                self.clicker_bind_komenda_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bind_komenda_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bind_komenda_label.setObjectName("clicker_bind_komenda_label")
                self.clicker_bind_sniezka_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bind_sniezka_label.setGeometry(QtCore.QRect(100, 60, 51, 31))
                self.clicker_bind_sniezka_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bind_sniezka_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bind_sniezka_label.setObjectName("clicker_bind_sniezka_label")
                self.clicker_bind_zmiana_seta_label = QtWidgets.QLabel(self.clicker_bindy_frame)
                self.clicker_bind_zmiana_seta_label.setGeometry(QtCore.QRect(210, 60, 81, 31))
                self.clicker_bind_zmiana_seta_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_bind_zmiana_seta_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_bind_zmiana_seta_label.setObjectName("clicker_bind_zmiana_seta_label")
                self.clicker_bind_clicker_lineedit = QtWidgets.QLineEdit(self.clicker_bindy_frame)
                self.clicker_bind_clicker_lineedit.setGeometry(QtCore.QRect(125, 33, 25, 25))
                self.clicker_bind_clicker_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_bind_clicker_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_bind_clicker_lineedit.setObjectName("clicker_bind_clicker_lineedit")
                self.clicker_bind_fakelag_lineedit = QtWidgets.QLineEdit(self.clicker_bindy_frame)
                self.clicker_bind_fakelag_lineedit.setGeometry(QtCore.QRect(240, 33, 25, 25))
                self.clicker_bind_fakelag_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_bind_fakelag_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_bind_fakelag_lineedit.setObjectName("clicker_bind_fakelag_lineedit")
                self.clicker_bind_komenda_lineedit = QtWidgets.QLineEdit(self.clicker_bindy_frame)
                self.clicker_bind_komenda_lineedit.setGeometry(QtCore.QRect(360, 33, 25, 25))
                self.clicker_bind_komenda_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_bind_komenda_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_bind_komenda_lineedit.setObjectName("clicker_bind_komenda_lineedit")
                self.clicker_bind_sniezka_lineedit = QtWidgets.QLineEdit(self.clicker_bindy_frame)
                self.clicker_bind_sniezka_lineedit.setGeometry(QtCore.QRect(160, 63, 25, 25))
                self.clicker_bind_sniezka_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_bind_sniezka_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_bind_sniezka_lineedit.setObjectName("clicker_bind_sniezka_lineedit")
                self.clicker_bind_zmiana_seta_lineedit = QtWidgets.QLineEdit(self.clicker_bindy_frame)
                self.clicker_bind_zmiana_seta_lineedit.setGeometry(QtCore.QRect(290, 63, 25, 25))
                self.clicker_bind_zmiana_seta_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_bind_zmiana_seta_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_bind_zmiana_seta_lineedit.setObjectName("clicker_bind_zmiana_seta_lineedit")
                self.clicker_zmiana_seta_frame = QtWidgets.QFrame(self.clicker_page)
                self.clicker_zmiana_seta_frame.setGeometry(QtCore.QRect(20, 120, 340, 430))
                self.clicker_zmiana_seta_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}\n"
                "QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 10px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_zmiana_seta_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.clicker_zmiana_seta_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.clicker_zmiana_seta_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_zmiana_seta_frame.setObjectName("clicker_zmiana_seta_frame")
                self.clicker_zmiana_seta_label = QtWidgets.QLabel(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_label.setGeometry(QtCore.QRect(20, 10, 80, 25))
                self.clicker_zmiana_seta_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_zmiana_seta_label.setAlignment(QtCore.Qt.AlignCenter)
                self.clicker_zmiana_seta_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_zmiana_seta_label.setObjectName("clicker_zmiana_seta_label")
                self.clicker_zmiana_seta_opis_label = QtWidgets.QLabel(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_opis_label.setGeometry(QtCore.QRect(45, 70, 250, 80))
                self.clicker_zmiana_seta_opis_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_zmiana_seta_opis_label.setAlignment(QtCore.Qt.AlignCenter)
                self.clicker_zmiana_seta_opis_label.setWordWrap(True)
                self.clicker_zmiana_seta_opis_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_zmiana_seta_opis_label.setObjectName("clicker_zmiana_seta_opis_label")
                self.clicker_zmiana_seta_1_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_1_lineedit.setGeometry(QtCore.QRect(15, 180, 30, 30))
                self.clicker_zmiana_seta_1_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_1_lineedit.setObjectName("clicker_zmiana_seta_1_lineedit")
                self.clicker_zmiana_seta_2_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_2_lineedit.setGeometry(QtCore.QRect(50, 180, 30, 30))
                self.clicker_zmiana_seta_2_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_2_lineedit.setObjectName("clicker_zmiana_seta_2_lineedit")
                self.clicker_zmiana_seta_3_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_3_lineedit.setGeometry(QtCore.QRect(85, 180, 30, 30))
                self.clicker_zmiana_seta_3_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_3_lineedit.setObjectName("clicker_zmiana_seta_3_lineedit")
                self.clicker_zmiana_seta_4_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_4_lineedit.setGeometry(QtCore.QRect(120, 180, 30, 30))
                self.clicker_zmiana_seta_4_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_4_lineedit.setObjectName("clicker_zmiana_seta_4_lineedit")
                self.clicker_zmiana_seta_5_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_5_lineedit.setGeometry(QtCore.QRect(155, 180, 30, 30))
                self.clicker_zmiana_seta_5_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_5_lineedit.setObjectName("clicker_zmiana_seta_5_lineedit")
                self.clicker_zmiana_seta_6_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_6_lineedit.setGeometry(QtCore.QRect(190, 180, 30, 30))
                self.clicker_zmiana_seta_6_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_6_lineedit.setObjectName("clicker_zmiana_seta_6_lineedit")
                self.clicker_zmiana_seta_7_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_7_lineedit.setGeometry(QtCore.QRect(225, 180, 30, 30))
                self.clicker_zmiana_seta_7_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_7_lineedit.setObjectName("clicker_zmiana_seta_7_lineedit")
                self.clicker_zmiana_seta_8_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_8_lineedit.setGeometry(QtCore.QRect(260, 180, 30, 30))
                self.clicker_zmiana_seta_8_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_8_lineedit.setObjectName("clicker_zmiana_seta_8_lineedit")
                self.clicker_zmiana_seta_9_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_9_lineedit.setGeometry(QtCore.QRect(295, 180, 30, 30))
                self.clicker_zmiana_seta_9_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_9_lineedit.setObjectName("clicker_zmiana_seta_9_lineedit")
                self.clicker_zmiana_seta_10_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_10_lineedit.setGeometry(QtCore.QRect(15, 215, 30, 30))
                self.clicker_zmiana_seta_10_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_10_lineedit.setObjectName("clicker_zmiana_seta_10_lineedit")
                self.clicker_zmiana_seta_11_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_11_lineedit.setGeometry(QtCore.QRect(50, 215, 30, 30))
                self.clicker_zmiana_seta_11_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_11_lineedit.setObjectName("clicker_zmiana_seta_11_lineedit")
                self.clicker_zmiana_seta_12_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_12_lineedit.setGeometry(QtCore.QRect(85, 215, 30, 30))
                self.clicker_zmiana_seta_12_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_12_lineedit.setObjectName("clicker_zmiana_seta_12_lineedit")
                self.clicker_zmiana_seta_13_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_13_lineedit.setGeometry(QtCore.QRect(120, 215, 30, 30))
                self.clicker_zmiana_seta_13_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_13_lineedit.setObjectName("clicker_zmiana_seta_13_lineedit")
                self.clicker_zmiana_seta_14_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_14_lineedit.setGeometry(QtCore.QRect(155, 215, 30, 30))
                self.clicker_zmiana_seta_14_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_14_lineedit.setObjectName("clicker_zmiana_seta_14_lineedit")
                self.clicker_zmiana_seta_15_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_15_lineedit.setGeometry(QtCore.QRect(190, 215, 30, 30))
                self.clicker_zmiana_seta_15_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_15_lineedit.setObjectName("clicker_zmiana_seta_15_lineedit")
                self.clicker_zmiana_seta_16_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_16_lineedit.setGeometry(QtCore.QRect(225, 215, 30, 30))
                self.clicker_zmiana_seta_16_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_16_lineedit.setObjectName("clicker_zmiana_seta_16_lineedit")
                self.clicker_zmiana_seta_17_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_17_lineedit.setGeometry(QtCore.QRect(260, 215, 30, 30))
                self.clicker_zmiana_seta_17_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_17_lineedit.setObjectName("clicker_zmiana_seta_17_lineedit")
                self.clicker_zmiana_seta_18_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_18_lineedit.setGeometry(QtCore.QRect(295, 215, 30, 30))
                self.clicker_zmiana_seta_18_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_18_lineedit.setObjectName("clicker_zmiana_seta_18_lineedit")
                self.clicker_zmiana_seta_19_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_19_lineedit.setGeometry(QtCore.QRect(15, 250, 30, 30))
                self.clicker_zmiana_seta_19_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_19_lineedit.setObjectName("clicker_zmiana_seta_19_lineedit")
                self.clicker_zmiana_seta_20_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_20_lineedit.setGeometry(QtCore.QRect(50, 250, 30, 30))
                self.clicker_zmiana_seta_20_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_20_lineedit.setObjectName("clicker_zmiana_seta_20_lineedit")
                self.clicker_zmiana_seta_21_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_21_lineedit.setGeometry(QtCore.QRect(85, 250, 30, 30))
                self.clicker_zmiana_seta_21_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_21_lineedit.setObjectName("clicker_zmiana_seta_21_lineedit")
                self.clicker_zmiana_seta_22_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_22_lineedit.setGeometry(QtCore.QRect(120, 250, 30, 30))
                self.clicker_zmiana_seta_22_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_22_lineedit.setObjectName("clicker_zmiana_seta_22_lineedit")
                self.clicker_zmiana_seta_23_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_23_lineedit.setGeometry(QtCore.QRect(155, 250, 30, 30))
                self.clicker_zmiana_seta_23_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_23_lineedit.setObjectName("clicker_zmiana_seta_23_lineedit")
                self.clicker_zmiana_seta_24_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_24_lineedit.setGeometry(QtCore.QRect(190, 250, 30, 30))
                self.clicker_zmiana_seta_24_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_24_lineedit.setObjectName("clicker_zmiana_seta_24_lineedit")
                self.clicker_zmiana_seta_25_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_25_lineedit.setGeometry(QtCore.QRect(225, 250, 30, 30))
                self.clicker_zmiana_seta_25_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_25_lineedit.setObjectName("clicker_zmiana_seta_25_lineedit")
                self.clicker_zmiana_seta_26_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_26_lineedit.setGeometry(QtCore.QRect(260, 250, 30, 30))
                self.clicker_zmiana_seta_26_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_26_lineedit.setObjectName("clicker_zmiana_seta_26_lineedit")
                self.clicker_zmiana_seta_27_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_27_lineedit.setGeometry(QtCore.QRect(295, 250, 30, 30))
                self.clicker_zmiana_seta_27_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_27_lineedit.setObjectName("clicker_zmiana_seta_27_lineedit")
                self.clicker_zmiana_seta_28_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_28_lineedit.setGeometry(QtCore.QRect(15, 285, 30, 30))
                self.clicker_zmiana_seta_28_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_28_lineedit.setObjectName("clicker_zmiana_seta_28_lineedit")
                self.clicker_zmiana_seta_29_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_29_lineedit.setGeometry(QtCore.QRect(50, 285, 30, 30))
                self.clicker_zmiana_seta_29_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_29_lineedit.setObjectName("clicker_zmiana_seta_29_lineedit")
                self.clicker_zmiana_seta_30_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_30_lineedit.setGeometry(QtCore.QRect(85, 285, 30, 30))
                self.clicker_zmiana_seta_30_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_30_lineedit.setObjectName("clicker_zmiana_seta_30_lineedit")
                self.clicker_zmiana_seta_31_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_31_lineedit.setGeometry(QtCore.QRect(120, 285, 30, 30))
                self.clicker_zmiana_seta_31_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_31_lineedit.setObjectName("clicker_zmiana_seta_31_lineedit")
                self.clicker_zmiana_seta_32_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_32_lineedit.setGeometry(QtCore.QRect(155, 285, 30, 30))
                self.clicker_zmiana_seta_32_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_32_lineedit.setObjectName("clicker_zmiana_seta_32_lineedit")
                self.clicker_zmiana_seta_33_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_33_lineedit.setGeometry(QtCore.QRect(190, 285, 30, 30))
                self.clicker_zmiana_seta_33_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_33_lineedit.setObjectName("clicker_zmiana_seta_33_lineedit")
                self.clicker_zmiana_seta_34_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_34_lineedit.setGeometry(QtCore.QRect(225, 285, 30, 30))
                self.clicker_zmiana_seta_34_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_34_lineedit.setObjectName("clicker_zmiana_seta_34_lineedit")
                self.clicker_zmiana_seta_35_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_35_lineedit.setGeometry(QtCore.QRect(260, 285, 30, 30))
                self.clicker_zmiana_seta_35_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_35_lineedit.setObjectName("clicker_zmiana_seta_35_lineedit")
                self.clicker_zmiana_seta_36_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_36_lineedit.setGeometry(QtCore.QRect(295, 285, 30, 30))
                self.clicker_zmiana_seta_36_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_36_lineedit.setObjectName("clicker_zmiana_seta_36_lineedit")
                self.clicker_zmiana_seta_37_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_37_lineedit.setGeometry(QtCore.QRect(15, 335, 30, 30))
                self.clicker_zmiana_seta_37_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_37_lineedit.setObjectName("clicker_zmiana_seta_37_lineedit")
                self.clicker_zmiana_seta_38_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_38_lineedit.setGeometry(QtCore.QRect(50, 335, 30, 30))
                self.clicker_zmiana_seta_38_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_38_lineedit.setObjectName("clicker_zmiana_seta_38_lineedit")
                self.clicker_zmiana_seta_39_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_39_lineedit.setGeometry(QtCore.QRect(85, 335, 30, 30))
                self.clicker_zmiana_seta_39_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_39_lineedit.setObjectName("clicker_zmiana_seta_39_lineedit")
                self.clicker_zmiana_seta_40_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_40_lineedit.setGeometry(QtCore.QRect(120, 335, 30, 30))
                self.clicker_zmiana_seta_40_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_40_lineedit.setObjectName("clicker_zmiana_seta_40_lineedit")
                self.clicker_zmiana_seta_41_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_41_lineedit.setGeometry(QtCore.QRect(155, 335, 30, 30))
                self.clicker_zmiana_seta_41_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_41_lineedit.setObjectName("clicker_zmiana_seta_41_lineedit")
                self.clicker_zmiana_seta_42_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_42_lineedit.setGeometry(QtCore.QRect(190, 335, 30, 30))
                self.clicker_zmiana_seta_42_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_42_lineedit.setObjectName("clicker_zmiana_seta_42_lineedit")
                self.clicker_zmiana_seta_43_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_43_lineedit.setGeometry(QtCore.QRect(225, 335, 30, 30))
                self.clicker_zmiana_seta_43_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_43_lineedit.setObjectName("clicker_zmiana_seta_43_lineedit")
                self.clicker_zmiana_seta_44_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_44_lineedit.setGeometry(QtCore.QRect(260, 335, 30, 30))
                self.clicker_zmiana_seta_44_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_44_lineedit.setObjectName("clicker_zmiana_seta_44_lineedit")
                self.clicker_zmiana_seta_45_lineedit = QtWidgets.QLineEdit(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_45_lineedit.setGeometry(QtCore.QRect(295, 335, 30, 30))
                self.clicker_zmiana_seta_45_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_zmiana_seta_45_lineedit.setObjectName("clicker_zmiana_seta_45_lineedit")
                self.clicker_zmiana_seta_line_label = QtWidgets.QLabel(self.clicker_zmiana_seta_frame)
                self.clicker_zmiana_seta_line_label.setGeometry(QtCore.QRect(0, 325, 340, 1))
                self.clicker_zmiana_seta_line_label.setStyleSheet("border: none;")
                self.clicker_zmiana_seta_line_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
                self.clicker_zmiana_seta_line_label.setObjectName("clicker_zmiana_seta_line_label")
                self.clicker_opcje_frame = QtWidgets.QFrame(self.clicker_page)
                self.clicker_opcje_frame.setGeometry(QtCore.QRect(380, 150, 420, 400))
                self.clicker_opcje_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.clicker_opcje_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.clicker_opcje_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.clicker_opcje_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_opcje_frame.setObjectName("clicker_opcje_frame")
                self.clicker_opcje_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_label.setGeometry(QtCore.QRect(20, 10, 40, 25))
                self.clicker_opcje_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_label.setAlignment(QtCore.Qt.AlignCenter)
                self.clicker_opcje_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_label.setObjectName("clicker_opcje_label")
                
                #MS
                self.clicker_opcje_clicker_ms_slider_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_clicker_ms_slider_label.setObjectName(u"clicker_opcje_clicker_ms_slider_label")
                self.clicker_opcje_clicker_ms_slider_label.setGeometry(QtCore.QRect(90, 50, 31, 30))
                self.clicker_opcje_clicker_ms_slider_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_clicker_ms_slider_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_clicker_ms_slider = QtWidgets.QSlider(self.clicker_opcje_frame)
                self.clicker_opcje_clicker_ms_slider.setGeometry(QtCore.QRect(230, 55, 160, 20))
                self.clicker_opcje_clicker_ms_slider.setStyleSheet("background-color: none;")
                self.clicker_opcje_clicker_ms_slider.setMinimum(1)
                self.clicker_opcje_clicker_ms_slider.setMaximum(500)
                self.clicker_opcje_clicker_ms_slider.setValue(0)
                self.clicker_opcje_clicker_ms_slider.setOrientation(QtCore.Qt.Horizontal)
                self.clicker_opcje_clicker_ms_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.clicker_opcje_clicker_ms_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_opcje_clicker_ms_slider.valueChanged.connect(lambda: self.update_options('ms'))
                self.clicker_opcje_clicker_ms_slider.setObjectName("clicker_opcje_clicker_ms_slider")
                
                #GARDA
                self.clicker_opcje_garda_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_garda_checkbox.setGeometry(QtCore.QRect(30, 88, 25, 25))
                self.clicker_opcje_garda_checkbox.setText("")
                self.clicker_opcje_garda_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_garda_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_garda_checkbox.clicked.connect(lambda: self.update_options('garda'))
                self.clicker_opcje_garda_checkbox.setObjectName("clicker_opcje_garda_checkbox")
                self.clicker_opcje_garda_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_garda_label.setObjectName(u"clicker_opcje_garda_label")
                self.clicker_opcje_garda_label.setGeometry(QtCore.QRect(60, 85, 50, 30))
                self.clicker_opcje_garda_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_garda_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_garda_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_garda_status_label.setObjectName(u"clicker_opcje_garda_status_label")
                self.clicker_opcje_garda_status_label.setGeometry(QtCore.QRect(110, 85, 31, 30))
                self.clicker_opcje_garda_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_garda_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_garda_slider_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_garda_slider_label.setObjectName(u"clicker_opcje_garda_slider_label")
                self.clicker_opcje_garda_slider_label.setGeometry(QtCore.QRect(145, 85, 31, 30))
                self.clicker_opcje_garda_slider_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_garda_slider_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_garda_slider = QtWidgets.QSlider(self.clicker_opcje_frame)
                self.clicker_opcje_garda_slider.setGeometry(QtCore.QRect(230, 90, 160, 22))
                self.clicker_opcje_garda_slider.setStyleSheet("background-color: none;")
                self.clicker_opcje_garda_slider.setMinimum(1)
                self.clicker_opcje_garda_slider.setMaximum(500)
                self.clicker_opcje_garda_slider.setValue(1)
                self.clicker_opcje_garda_slider.setOrientation(QtCore.Qt.Horizontal)
                self.clicker_opcje_garda_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.clicker_opcje_garda_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_opcje_garda_slider.valueChanged.connect(lambda: self.update_options('garda'))
                self.clicker_opcje_garda_slider.setObjectName("clicker_opcje_garda_slider")
                
                #FAKELAG
                self.clicker_opcje_fakelag_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_fakelag_checkbox.setGeometry(QtCore.QRect(30, 123, 25, 25))
                self.clicker_opcje_fakelag_checkbox.setText("")
                self.clicker_opcje_fakelag_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_fakelag_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_fakelag_checkbox.clicked.connect(lambda: self.update_options('fakelag'))
                self.clicker_opcje_fakelag_checkbox.setObjectName("clicker_opcje_fakelag_checkbox")
                self.clicker_opcje_fakelag_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_fakelag_label.setObjectName(u"clicker_opcje_fakelag_label")
                self.clicker_opcje_fakelag_label.setGeometry(QtCore.QRect(60, 120, 60, 30))
                self.clicker_opcje_fakelag_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_fakelag_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_fakelag_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_fakelag_status_label.setObjectName(u"clicker_opcje_fakelag_status_label")
                self.clicker_opcje_fakelag_status_label.setGeometry(QtCore.QRect(120, 120, 31, 30))
                self.clicker_opcje_fakelag_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_fakelag_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_fakelag_slider_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_fakelag_slider_label.setObjectName(u"clicker_opcje_fakelag_slider_label")
                self.clicker_opcje_fakelag_slider_label.setGeometry(QtCore.QRect(155, 120, 31, 30))
                self.clicker_opcje_fakelag_slider_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_fakelag_slider_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_fakelag_slider = QtWidgets.QSlider(self.clicker_opcje_frame)
                self.clicker_opcje_fakelag_slider.setGeometry(QtCore.QRect(230, 125, 160, 22))
                self.clicker_opcje_fakelag_slider.setStyleSheet("background-color: none;")
                self.clicker_opcje_fakelag_slider.setMinimum(1)
                self.clicker_opcje_fakelag_slider.setMaximum(15)
                self.clicker_opcje_fakelag_slider.setPageStep(1)
                self.clicker_opcje_fakelag_slider.setOrientation(QtCore.Qt.Horizontal)
                self.clicker_opcje_fakelag_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.clicker_opcje_fakelag_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_opcje_fakelag_slider.valueChanged.connect(lambda: self.update_options('fakelag'))
                self.clicker_opcje_fakelag_slider.setObjectName("clicker_opcje_fakelag_slider")
                
                #ZMIANA SETA
                self.clicker_opcje_zmiana_seta_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_zmiana_seta_checkbox.setGeometry(QtCore.QRect(30, 158, 25, 25))
                self.clicker_opcje_zmiana_seta_checkbox.setText("")
                self.clicker_opcje_zmiana_seta_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_zmiana_seta_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_zmiana_seta_checkbox.clicked.connect(lambda: self.update_options('zmiana_seta'))
                self.clicker_opcje_zmiana_seta_checkbox.setObjectName("clicker_opcje_zmiana_seta_checkbox")
                self.clicker_opcje_zmiana_seta_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_zmiana_seta_label.setObjectName(u"clicker_opcje_zmiana_seta_label")
                self.clicker_opcje_zmiana_seta_label.setGeometry(QtCore.QRect(60, 155, 90, 30))
                self.clicker_opcje_zmiana_seta_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_zmiana_seta_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_zmiana_seta_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_zmiana_seta_status_label.setObjectName(u"clicker_opcje_zmiana_seta_status_label")
                self.clicker_opcje_zmiana_seta_status_label.setGeometry(QtCore.QRect(150, 155, 31, 30))
                self.clicker_opcje_zmiana_seta_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_zmiana_seta_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_zmiana_seta_slider_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_zmiana_seta_slider_label.setObjectName(u"clicker_opcje_zmiana_seta_slider_label")
                self.clicker_opcje_zmiana_seta_slider_label.setGeometry(QtCore.QRect(185, 155, 31, 30))
                self.clicker_opcje_zmiana_seta_slider_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_zmiana_seta_slider_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_zmiana_seta_slider = QtWidgets.QSlider(self.clicker_opcje_frame)
                self.clicker_opcje_zmiana_seta_slider.setGeometry(QtCore.QRect(230, 160, 160, 22))
                self.clicker_opcje_zmiana_seta_slider.setStyleSheet("background-color: none;")
                self.clicker_opcje_zmiana_seta_slider.setMinimum(0)
                self.clicker_opcje_zmiana_seta_slider.setMaximum(100)
                self.clicker_opcje_zmiana_seta_slider.setOrientation(QtCore.Qt.Horizontal)
                self.clicker_opcje_zmiana_seta_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.clicker_opcje_zmiana_seta_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.clicker_opcje_zmiana_seta_slider.valueChanged.connect(lambda: self.update_options('zmiana_seta'))
                self.clicker_opcje_zmiana_seta_slider.setObjectName("clicker_opcje_zmiana_seta_slider")
                self.clicker_opcje_clicker_ms_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_clicker_ms_label.setObjectName(u"clicker_opcje_clicker_ms_label")
                self.clicker_opcje_clicker_ms_label.setGeometry(QtCore.QRect(60, 50, 25, 30))
                self.clicker_opcje_clicker_ms_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_clicker_ms_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                
                #KOMENDA
                self.clicker_opcje_komenda_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_komenda_checkbox.setGeometry(QtCore.QRect(30, 193, 25, 25))
                self.clicker_opcje_komenda_checkbox.setText("")
                self.clicker_opcje_komenda_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_komenda_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_komenda_checkbox.clicked.connect(lambda: self.update_options('komenda'))
                self.clicker_opcje_komenda_checkbox.setObjectName("clicker_opcje_komenda_checkbox")
                self.clicker_opcje_komenda_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_komenda_label.setObjectName(u"clicker_opcje_komenda_label")
                self.clicker_opcje_komenda_label.setGeometry(QtCore.QRect(60, 190, 70, 30))
                self.clicker_opcje_komenda_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_komenda_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_komenda_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_komenda_status_label.setObjectName(u"clicker_opcje_komenda_status_label")
                self.clicker_opcje_komenda_status_label.setGeometry(QtCore.QRect(130, 190, 31, 30))
                self.clicker_opcje_komenda_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_komenda_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_komenda_lineedit = QtWidgets.QLineEdit(self.clicker_opcje_frame)
                self.clicker_opcje_komenda_lineedit.setGeometry(QtCore.QRect(230, 195, 161, 20))
                self.clicker_opcje_komenda_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 10px;\n"
                "    border: 2px solid rgb(45, 45, 45);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 0 4px;\n"
                "}")
                self.clicker_opcje_komenda_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_komenda_lineedit.setObjectName("clicker_opcje_komenda_lineedit")
                
                #SNIEZKA
                self.clicker_opcje_sniezka_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_label.setObjectName(u"clicker_opcje_sniezka_label")
                self.clicker_opcje_sniezka_label.setGeometry(QtCore.QRect(60, 225, 60, 30))
                self.clicker_opcje_sniezka_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_sniezka_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_sniezka_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_status_label.setObjectName(u"clicker_opcje_sniezka_status_label")
                self.clicker_opcje_sniezka_status_label.setGeometry(QtCore.QRect(120, 225, 31, 30))
                self.clicker_opcje_sniezka_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_sniezka_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_sniezka_slot_miecz_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_slot_miecz_label.setObjectName(u"clicker_opcje_sniezka_slot_miecz_label")
                self.clicker_opcje_sniezka_slot_miecz_label.setGeometry(QtCore.QRect(230, 225, 40, 30))
                self.clicker_opcje_sniezka_slot_miecz_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_sniezka_slot_miecz_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_sniezka_slot_miecz_lineedit = QtWidgets.QLineEdit(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_slot_miecz_lineedit.setObjectName(u"clicker_opcje_sniezka_slot_miecz_lineedit")
                self.clicker_opcje_sniezka_slot_miecz_lineedit.setGeometry(QtCore.QRect(270, 228, 25, 25))
                self.clicker_opcje_sniezka_slot_miecz_lineedit.setStyleSheet("QLineEdit {\n"
                "	background-color: rgb(65, 65, 65);\n"
                "	border-radius: 8px;\n"
                "	border: 2px solid rgb(30, 30, 30);\n"
                "	color: rgb(120, 255, 120);\n"
                "	padding: 0 4px;\n"
                "}")
                self.clicker_opcje_sniezka_slot_miecz_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_sniezka_slot_sniezka_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_slot_sniezka_label.setObjectName(u"clicker_opcje_sniezka_slot_sniezka_label")
                self.clicker_opcje_sniezka_slot_sniezka_label.setGeometry(QtCore.QRect(305, 225, 60, 30))
                self.clicker_opcje_sniezka_slot_sniezka_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "       background-color: none;\n"
                "	color: white;\n"
                "	font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_sniezka_slot_sniezka_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_sniezka_slot_sniezka_lineedit = QtWidgets.QLineEdit(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_slot_sniezka_lineedit.setObjectName(u"clicker_opcje_sniezka_slot_sniezka_lineedit")
                self.clicker_opcje_sniezka_slot_sniezka_lineedit.setGeometry(QtCore.QRect(360, 228, 25, 25))
                self.clicker_opcje_sniezka_slot_sniezka_lineedit.setStyleSheet("QLineEdit {\n"
                "	background-color: rgb(65, 65, 65);\n"
                "	border-radius: 8px;\n"
                "	border: 2px solid rgb(30, 30, 30);\n"
                "	color: rgb(120, 255, 120);\n"
                "	padding: 0 4px;\n"
                "}")
                self.clicker_opcje_sniezka_slot_sniezka_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_sniezka_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_sniezka_checkbox.setGeometry(QtCore.QRect(30, 228, 25, 25))
                self.clicker_opcje_sniezka_checkbox.setText("")
                self.clicker_opcje_sniezka_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_sniezka_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_sniezka_checkbox.clicked.connect(lambda: self.update_options('sniezka'))
                self.clicker_opcje_sniezka_checkbox.setObjectName("clicker_opcje_sniezka_checkbox")
                
                #JITTER
                self.clicker_opcje_jitter_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                self.clicker_opcje_jitter_checkbox.setGeometry(QtCore.QRect(30, 263, 25, 25))
                self.clicker_opcje_jitter_checkbox.setText("")
                self.clicker_opcje_jitter_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.clicker_opcje_jitter_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.clicker_opcje_jitter_checkbox.clicked.connect(lambda: self.update_options('jitter'))
                self.clicker_opcje_jitter_checkbox.setObjectName("clicker_opcje_jitter_checkbox")
                self.clicker_opcje_jitter_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_jitter_label.setObjectName(u"clicker_opcje_jitter_label")
                self.clicker_opcje_jitter_label.setGeometry(QtCore.QRect(60, 260, 51, 30))
                self.clicker_opcje_jitter_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_jitter_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_jitter_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_jitter_status_label.setObjectName(u"clicker_opcje_jitter_status_label")
                self.clicker_opcje_jitter_status_label.setGeometry(QtCore.QRect(110, 260, 31, 30))
                self.clicker_opcje_jitter_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_jitter_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                
                #PODGLAD
                #self.clicker_opcje_podglad_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                #self.clicker_opcje_podglad_checkbox.setGeometry(QtCore.QRect(30, 298, 25, 25))
                #self.clicker_opcje_podglad_checkbox.setText("")
                #self.clicker_opcje_podglad_checkbox.setStyleSheet("QCheckBox {\n"
                #"    background-color: none;\n"
                #"    color:white;\n"
                #"}\n"
                #"QCheckBox:hover {\n"
                #"    color: rgb(0, 255, 0);\n"
                #"}\n"
                #"QCheckBox::indicator {\n"
                #"    width: 17px;\n"
                #"    height: 17px;\n"
                #"    background-color: rgb(65, 65, 65);\n"
                #"    border: 2px solid rgb(30, 30, 30);\n"
                #"    border-radius: 5px;\n"
                #"}\n"
                #"QCheckBox::indicator:checked {\n"
                #"    image: url(img/checked_green.png);\n"
                #"}")
                #self.clicker_opcje_podglad_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                #self.clicker_opcje_podglad_checkbox.clicked.connect(lambda: self.update_options('podglad'))
                #self.clicker_opcje_podglad_checkbox.setObjectName("clicker_opcje_podglad_checkbox")
                self.clicker_opcje_podglad_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_podglad_label.setObjectName(u"clicker_opcje_podglad_label")
                self.clicker_opcje_podglad_label.setGeometry(QtCore.QRect(60, 295, 111, 30))
                self.clicker_opcje_podglad_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_podglad_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_podglad_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_podglad_status_label.setObjectName(u"clicker_opcje_podglad_status_label")
                self.clicker_opcje_podglad_status_label.setGeometry(QtCore.QRect(170, 295, 31, 30))
                self.clicker_opcje_podglad_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_podglad_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                
                #AIM ASSIST
                self.clicker_opcje_aim_assist_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_aim_assist_label.setObjectName(u"clicker_opcje_aim_assist_label")
                self.clicker_opcje_aim_assist_label.setGeometry(QtCore.QRect(60, 330, 131, 30))
                self.clicker_opcje_aim_assist_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_aim_assist_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.clicker_opcje_aim_assist_status_label = QtWidgets.QLabel(self.clicker_opcje_frame)
                self.clicker_opcje_aim_assist_status_label.setObjectName(u"clicker_opcje_aim_assist_status_label")
                self.clicker_opcje_aim_assist_status_label.setGeometry(QtCore.QRect(195, 330, 31, 30))
                self.clicker_opcje_aim_assist_status_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: red;\n"
                "       background-color: none;\n"
                "	font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.clicker_opcje_aim_assist_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                #self.clicker_opcje_aim_assist_checkbox = QtWidgets.QCheckBox(self.clicker_opcje_frame)
                #self.clicker_opcje_aim_assist_checkbox.setGeometry(QtCore.QRect(30, 333, 25, 25))
                #self.clicker_opcje_aim_assist_checkbox.setText("")
                #self.clicker_opcje_aim_assist_checkbox.setStyleSheet("QCheckBox {\n"
                #"    background-color: none;\n"
                #"    color:white;\n"
                #"}\n"
                #"QCheckBox:hover {\n"
                #"    color: rgb(0, 255, 0);\n"
                #"}\n"
                #"QCheckBox::indicator {\n"
                #"    width: 17px;\n"
                #"    height: 17px;\n"
                #"    background-color: rgb(65, 65, 65);\n"
                #"    border: 2px solid rgb(30, 30, 30);\n"
                #"    border-radius: 5px;\n"
                #"}\n"
                #"QCheckBox::indicator:checked {\n"
                #"    image: url(img/checked_green.png);\n"
                #"}")
                #self.clicker_opcje_aim_assist_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                #self.clicker_opcje_aim_assist_checkbox.clicked.connect(lambda: self.update_options('aim_assist'))
                #self.clicker_opcje_aim_assist_checkbox.setObjectName("clicker_opcje_aim_assist_checkbox")
                
                self.stackedWidget.addWidget(self.clicker_page)
                self.miner_page = QtWidgets.QWidget()
                self.miner_page.setObjectName("miner_page")
                self.miner_status_frame = QtWidgets.QFrame(self.miner_page)
                self.miner_status_frame.setGeometry(QtCore.QRect(20, 20, 380, 80))
                self.miner_status_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.miner_status_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.miner_status_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.miner_status_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.miner_status_frame.setObjectName("miner_status_frame")
                self.miner_status_label = QtWidgets.QLabel(self.miner_status_frame)
                self.miner_status_label.setGeometry(QtCore.QRect(20, 25, 50, 30))
                self.miner_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_status_label.setObjectName("miner_status_label")
                self.miner_status_current_label = QtWidgets.QLabel(self.miner_status_frame)
                self.miner_status_current_label.setGeometry(QtCore.QRect(70, 25, 31, 30))
                self.miner_status_current_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_status_current_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_status_current_label.setObjectName("miner_status_current_label")
                self.miner_status_start_pushbutton = PushButton(self.miner_status_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_status_start_pushbutton.setGeometry(QtCore.QRect(180, 25, 80, 30))
                self.miner_status_start_pushbutton.clicked.connect(lambda: self.start_miner())
                self.miner_status_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_status_start_pushbutton.setObjectName("miner_status_start_pushbutton")
                self.miner_status_stop_pushbutton = PushButton(self.miner_status_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_status_stop_pushbutton.setGeometry(QtCore.QRect(280, 25, 80, 30))
                self.miner_status_stop_pushbutton.clicked.connect(lambda: self.stop_miner())
                self.miner_status_stop_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_status_stop_pushbutton.setObjectName("miner_status_stop_pushbutton")
                self.miner_opcje_frame = QtWidgets.QFrame(self.miner_page)
                self.miner_opcje_frame.setGeometry(QtCore.QRect(415, 210, 380, 220))
                self.miner_opcje_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.miner_opcje_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.miner_opcje_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.miner_opcje_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.miner_opcje_frame.setObjectName("miner_opcje_frame")
                self.miner_opcje_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_label.setGeometry(QtCore.QRect(20, 10, 41, 25))
                self.miner_opcje_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_label.setAlignment(QtCore.Qt.AlignCenter)
                self.miner_opcje_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_label.setObjectName("miner_opcje_label")
                self.miner_opcje_anty_rodzic_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_anty_rodzic_label.setGeometry(QtCore.QRect(60, 47, 80, 31))
                self.miner_opcje_anty_rodzic_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_anty_rodzic_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_anty_rodzic_label.setObjectName("miner_opcje_anty_rodzic_label")
                self.miner_opcje_anty_rodzic_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_anty_rodzic_status_label.setGeometry(QtCore.QRect(145, 47, 31, 31))
                self.miner_opcje_anty_rodzic_status_label.setToolTip("")
                self.miner_opcje_anty_rodzic_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}\n"
                "")
                self.miner_opcje_anty_rodzic_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_anty_rodzic_status_label.setObjectName("miner_opcje_anty_rodzic_status_label")
                self.miner_opcje_anty_rodzic_godzina_timeedit = QtWidgets.QTimeEdit(self.miner_opcje_frame)
                self.miner_opcje_anty_rodzic_godzina_timeedit.setGeometry(QtCore.QRect(200, 52, 71, 22))
                self.miner_opcje_anty_rodzic_godzina_timeedit.setStyleSheet("QTimeEdit {\n"
                "	background-color: rgb(65, 65, 65);\n"
                "	border: 2px solid rgb(30, 30, 30);\n"
                "	border-radius: 8px;\n"
                f"	color: rgb(120, 255, 120);\n"
                "       padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QTimeEdit:hover {\n"
                "	color: rgb(255, 255, 255);\n"
                "}\n"
                "QTimeEdit::up-button {\n"
                f"	background-color: rgb(0, 200, 0);\n"
                "	border-top: 1px solid rgb(30, 30, 30);\n"
                "	border-right: 1px solid rgb(30, 30, 30);\n"
                "	border-top-right-radius: 7px;\n"
                "	border-bottom-left-radius: 5px;\n"
                "	margin-bottom: 1px;\n"
                "}\n"
                "QTimeEdit::down-button {\n"
                f"	background-color: rgb(0, 200, 0);\n"
                "	border-bottom: 1px solid rgb(30, 30, 30);\n"
                "	border-right: 1px solid rgb(30, 30, 30);\n"
                "	border-bottom-right-radius: 7px;\n"
                "	border-top-left-radius: 5px;\n"
                "	margin-top: 1px;\n"
                "}\n"
                "QTimeEdit::up-button:hover {\n"
                f"	background-color: rgb(0, 165, 0);\n"
                "}\n"
                "QTimeEdit::down-button:hover {\n"
                f"	background-color: rgb(0, 165, 0);\n"
                "}")
                self.miner_opcje_anty_rodzic_godzina_timeedit.setTime(QtCore.QTime(1, 10, 0))
                self.miner_opcje_anty_rodzic_godzina_timeedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_anty_rodzic_godzina_timeedit.setObjectName("miner_opcje_anty_rodzic_godzina_timeedit")
                self.miner_opcje_anty_rodzic_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_anty_rodzic_checkbox.setGeometry(QtCore.QRect(30, 50, 25, 25))
                self.miner_opcje_anty_rodzic_checkbox.setText("")
                self.miner_opcje_anty_rodzic_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.miner_opcje_anty_rodzic_checkbox.clicked.connect(lambda: self.update_options('anty_rodzic'))
                self.miner_opcje_anty_rodzic_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_anty_rodzic_checkbox.setObjectName("miner_opcje_anty_rodzic_checkbox")
                self.miner_opcje_tnt_logout_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_tnt_logout_label.setGeometry(QtCore.QRect(60, 77, 80, 31))
                self.miner_opcje_tnt_logout_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_tnt_logout_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_tnt_logout_label.setObjectName("miner_opcje_tnt_logout_label")
                self.miner_opcje_tnt_logout_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_tnt_logout_status_label.setGeometry(QtCore.QRect(145, 77, 31, 31))
                self.miner_opcje_tnt_logout_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_tnt_logout_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_tnt_logout_status_label.setObjectName("miner_opcje_tnt_logout_status_label")
                self.miner_opcje_tnt_logout_sciezka_lineedit = QtWidgets.QLineEdit(self.miner_opcje_frame)
                self.miner_opcje_tnt_logout_sciezka_lineedit.setGeometry(QtCore.QRect(200, 84, 161, 20))
                self.miner_opcje_tnt_logout_sciezka_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}")
                self.miner_opcje_tnt_logout_sciezka_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_tnt_logout_sciezka_lineedit.setObjectName("miner_opcje_tnt_logout_sciezka_lineedit")
                self.miner_opcje_tnt_logout_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_tnt_logout_checkbox.setGeometry(QtCore.QRect(30, 80, 25, 25))
                self.miner_opcje_tnt_logout_checkbox.setText("")
                self.miner_opcje_tnt_logout_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.miner_opcje_tnt_logout_checkbox.clicked.connect(lambda: self.update_options('tnt_logout'))
                self.miner_opcje_tnt_logout_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_tnt_logout_checkbox.setObjectName("miner_opcje_tnt_logout_checkbox")
                self.miner_opcje_kopanie_w_tle_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_label.setGeometry(QtCore.QRect(60, 107, 100, 31))
                self.miner_opcje_kopanie_w_tle_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kopanie_w_tle_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kopanie_w_tle_label.setObjectName("miner_opcje_kopanie_w_tle_label")
                self.miner_opcje_kopanie_w_tle_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_status_label.setGeometry(QtCore.QRect(160, 107, 31, 31))
                self.miner_opcje_kopanie_w_tle_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kopanie_w_tle_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kopanie_w_tle_status_label.setObjectName("miner_opcje_kopanie_w_tle_status_label")
                self.miner_opcje_kopanie_w_tle_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_checkbox.setGeometry(QtCore.QRect(30, 110, 25, 25))
                self.miner_opcje_kopanie_w_tle_checkbox.setText("")
                self.miner_opcje_kopanie_w_tle_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.miner_opcje_kopanie_w_tle_checkbox.clicked.connect(lambda: self.update_options('kopanie_w_tle'))
                self.miner_opcje_kopanie_w_tle_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_kopanie_w_tle_checkbox.setObjectName("miner_opcje_kopanie_w_tle_checkbox")
                self.miner_opcje_kopanie_w_tle_bp_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_bp_label.setGeometry(QtCore.QRect(230, 107, 30, 31))
                self.miner_opcje_kopanie_w_tle_bp_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kopanie_w_tle_bp_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kopanie_w_tle_bp_label.setObjectName("miner_opcje_kopanie_w_tle_bp_label")
                self.miner_opcje_kopanie_w_tle_bp_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_bp_status_label.setGeometry(QtCore.QRect(262, 107, 31, 31))
                self.miner_opcje_kopanie_w_tle_bp_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kopanie_w_tle_bp_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kopanie_w_tle_bp_status_label.setObjectName("miner_opcje_kopanie_w_tle_bp_status_label")
                self.miner_opcje_kopanie_w_tle_bp_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_kopanie_w_tle_bp_checkbox.setGeometry(QtCore.QRect(200, 110, 25, 25))
                self.miner_opcje_kopanie_w_tle_bp_checkbox.setText("")
                self.miner_opcje_kopanie_w_tle_bp_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked_green.png);\n"
                "}")
                self.miner_opcje_kopanie_w_tle_bp_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_kopanie_w_tle_bp_checkbox.setObjectName("miner_opcje_kopanie_w_tle_bp_checkbox")
                self.miner_opcje_auto_rejoin_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_auto_rejoin_label.setGeometry(QtCore.QRect(60, 137, 80, 31))
                self.miner_opcje_auto_rejoin_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_auto_rejoin_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_auto_rejoin_label.setObjectName("miner_opcje_auto_rejoin_label")
                self.miner_opcje_auto_rejoin_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_auto_rejoin_status_label.setGeometry(QtCore.QRect(143, 137, 31, 31))
                self.miner_opcje_auto_rejoin_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_auto_rejoin_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_auto_rejoin_status_label.setObjectName("miner_opcje_auto_rejoin_status_label")
                self.miner_opcje_auto_rejoin_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_auto_rejoin_checkbox.setGeometry(QtCore.QRect(30, 140, 25, 25))
                self.miner_opcje_auto_rejoin_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked.png);\n"
                "}")
                self.miner_opcje_auto_rejoin_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_auto_rejoin_checkbox.setText("")
                self.miner_opcje_auto_rejoin_checkbox.setObjectName("miner_opcje_auto_rejoin_checkbox")
                self.miner_opcje_kontrola_zdalna_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kontrola_zdalna_label.setGeometry(QtCore.QRect(60, 167, 111, 31))
                self.miner_opcje_kontrola_zdalna_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kontrola_zdalna_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kontrola_zdalna_label.setObjectName("miner_opcje_kontrola_zdalna_label")
                self.miner_opcje_kontrola_zdalna_status_label = QtWidgets.QLabel(self.miner_opcje_frame)
                self.miner_opcje_kontrola_zdalna_status_label.setGeometry(QtCore.QRect(172, 167, 31, 31))
                self.miner_opcje_kontrola_zdalna_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_opcje_kontrola_zdalna_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_opcje_kontrola_zdalna_status_label.setObjectName("miner_opcje_kontrola_zdalna_status_label")
                self.miner_opcje_kontrola_zdalna_checkbox = QtWidgets.QCheckBox(self.miner_opcje_frame)
                self.miner_opcje_kontrola_zdalna_checkbox.setGeometry(QtCore.QRect(30, 170, 25, 25))
                self.miner_opcje_kontrola_zdalna_checkbox.setStyleSheet("QCheckBox {\n"
                "    background-color: none;\n"
                "    color:white;\n"
                "}\n"
                "QCheckBox:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}\n"
                "QCheckBox::indicator {\n"
                "    width: 17px;\n"
                "    height: 17px;\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QCheckBox::indicator:checked {\n"
                "    image: url(img/checked.png);\n"
                "}")
                self.miner_opcje_kontrola_zdalna_checkbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_opcje_kontrola_zdalna_checkbox.setText("")
                self.miner_opcje_kontrola_zdalna_checkbox.clicked.connect(lambda: self.update_options('kontrola_zdalna'))
                self.miner_opcje_kontrola_zdalna_checkbox.setObjectName("miner_opcje_kontrola_zdalna_checkbox")
                self.miner_ustawienia_frame = QtWidgets.QFrame(self.miner_page)
                self.miner_ustawienia_frame.setGeometry(QtCore.QRect(20, 130, 380, 300))
                self.miner_ustawienia_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.miner_ustawienia_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.miner_ustawienia_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.miner_ustawienia_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.miner_ustawienia_frame.setObjectName("miner_ustawienia_frame")
                self.miner_ustawienia_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_label.setGeometry(QtCore.QRect(20, 10, 81, 25))
                self.miner_ustawienia_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_label.setAlignment(QtCore.Qt.AlignCenter)
                self.miner_ustawienia_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_label.setObjectName("miner_ustawienia_label")
                self.miner_ustawienia_dlugosc_stowniarek_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_dlugosc_stowniarek_label.setGeometry(QtCore.QRect(30, 40, 161, 31))
                self.miner_ustawienia_dlugosc_stowniarek_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_dlugosc_stowniarek_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_dlugosc_stowniarek_label.setObjectName("miner_ustawienia_dlugosc_stowniarek_label")
                self.miner_ustawienia_szerokosc_stowniarek_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_szerokosc_stowniarek_label.setGeometry(QtCore.QRect(30, 70, 181, 31))
                self.miner_ustawienia_szerokosc_stowniarek_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_szerokosc_stowniarek_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_szerokosc_stowniarek_label.setObjectName("miner_ustawienia_szerokosc_stowniarek_label")
                self.miner_ustawienia_ilosc_okrazen_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_ilosc_okrazen_label.setGeometry(QtCore.QRect(40, 200, 91, 21))
                self.miner_ustawienia_ilosc_okrazen_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_ilosc_okrazen_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_ilosc_okrazen_label.setObjectName("miner_ustawienia_ilosc_okrazen_label")
                self.miner_ustawienia_wpisywanie_komendy_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_wpisywanie_komendy_label.setGeometry(QtCore.QRect(30, 100, 191, 31))
                self.miner_ustawienia_wpisywanie_komendy_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_wpisywanie_komendy_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_wpisywanie_komendy_label.setObjectName("miner_ustawienia_wpisywanie_komendy_label")
                self.miner_ustawienia_czas_m_komendami_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_czas_m_komendami_label.setGeometry(QtCore.QRect(30, 130, 181, 31))
                self.miner_ustawienia_czas_m_komendami_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_czas_m_komendami_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_czas_m_komendami_label.setObjectName("miner_ustawienia_czas_m_komendami_label")
                self.miner_ustawienia_dlugosc_stowniarek_slider = QtWidgets.QSlider(self.miner_ustawienia_frame)
                self.miner_ustawienia_dlugosc_stowniarek_slider.setGeometry(QtCore.QRect(230, 45, 131, 20))
                self.miner_ustawienia_dlugosc_stowniarek_slider.setStyleSheet("background-color: none;")
                self.miner_ustawienia_dlugosc_stowniarek_slider.setMinimum(1)
                self.miner_ustawienia_dlugosc_stowniarek_slider.setMaximum(15)
                self.miner_ustawienia_dlugosc_stowniarek_slider.setValue(1)
                self.miner_ustawienia_dlugosc_stowniarek_slider.setOrientation(QtCore.Qt.Horizontal)
                self.miner_ustawienia_dlugosc_stowniarek_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.miner_ustawienia_dlugosc_stowniarek_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_dlugosc_stowniarek_slider.setObjectName("miner_ustawienia_dlugosc_stowniarek_slider")
                self.miner_ustawienia_szerokosc_stowniarek_slider = QtWidgets.QSlider(self.miner_ustawienia_frame)
                self.miner_ustawienia_szerokosc_stowniarek_slider.setGeometry(QtCore.QRect(230, 75, 131, 20))
                self.miner_ustawienia_szerokosc_stowniarek_slider.setStyleSheet("background-color: none;")
                self.miner_ustawienia_szerokosc_stowniarek_slider.setMinimum(1)
                self.miner_ustawienia_szerokosc_stowniarek_slider.setMaximum(10)
                self.miner_ustawienia_szerokosc_stowniarek_slider.setOrientation(QtCore.Qt.Horizontal)
                self.miner_ustawienia_szerokosc_stowniarek_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.miner_ustawienia_szerokosc_stowniarek_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_szerokosc_stowniarek_slider.setObjectName("miner_ustawienia_szerokosc_stowniarek_slider")
                #self.miner_ustawienia_ilosc_okrazen_slider = QtWidgets.QSlider(self.miner_ustawienia_frame)
                #self.miner_ustawienia_ilosc_okrazen_slider.setGeometry(QtCore.QRect(229, 135, 131, 20))
                #self.miner_ustawienia_ilosc_okrazen_slider.setStyleSheet("background-color: none;")
                #self.miner_ustawienia_ilosc_okrazen_slider.setMinimum(1)
                #self.miner_ustawienia_ilosc_okrazen_slider.setMaximum(100)
                #self.miner_ustawienia_ilosc_okrazen_slider.setOrientation(QtCore.Qt.Horizontal)
                #self.miner_ustawienia_ilosc_okrazen_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                #self.miner_ustawienia_ilosc_okrazen_slider.setObjectName("miner_ustawienia_ilosc_okrazen_slider")
                self.miner_ustawienia_wpisywanie_komendy_slider = QtWidgets.QSlider(self.miner_ustawienia_frame)
                self.miner_ustawienia_wpisywanie_komendy_slider.setGeometry(QtCore.QRect(230, 105, 131, 20))
                self.miner_ustawienia_wpisywanie_komendy_slider.setStyleSheet("background-color: none;")
                self.miner_ustawienia_wpisywanie_komendy_slider.setMinimum(1)
                self.miner_ustawienia_wpisywanie_komendy_slider.setMaximum(100)
                self.miner_ustawienia_wpisywanie_komendy_slider.setRange(1, 10)
                self.miner_ustawienia_wpisywanie_komendy_slider.setSingleStep(1)
                self.miner_ustawienia_wpisywanie_komendy_slider.setOrientation(QtCore.Qt.Horizontal)
                self.miner_ustawienia_wpisywanie_komendy_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.miner_ustawienia_wpisywanie_komendy_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_wpisywanie_komendy_slider.setObjectName("miner_ustawienia_wpisywanie_komendy_slider")
                self.miner_ustawienia_czas_m_komendami_slider = QtWidgets.QSlider(self.miner_ustawienia_frame)
                self.miner_ustawienia_czas_m_komendami_slider.setGeometry(QtCore.QRect(230, 135, 131, 20))
                self.miner_ustawienia_czas_m_komendami_slider.setStyleSheet("background-color: none;")
                self.miner_ustawienia_czas_m_komendami_slider.setMinimum(1)
                self.miner_ustawienia_czas_m_komendami_slider.setMaximum(100)
                self.miner_ustawienia_czas_m_komendami_slider.setRange(1, 10)
                self.miner_ustawienia_czas_m_komendami_slider.setSingleStep(1)
                self.miner_ustawienia_czas_m_komendami_slider.setOrientation(QtCore.Qt.Horizontal)
                self.miner_ustawienia_czas_m_komendami_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.miner_ustawienia_czas_m_komendami_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_czas_m_komendami_slider.setObjectName("miner_ustawienia_czas_m_komendami_slider")
                self.miner_ustawienia_komendy_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_komendy_label.setGeometry(QtCore.QRect(30, 170, 71, 31))
                self.miner_ustawienia_komendy_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_komendy_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_komendy_label.setObjectName("miner_ustawienia_komendy_label")
                self.miner_ustawienia_komenda_lineedit = QtWidgets.QLineEdit(self.miner_ustawienia_frame)
                self.miner_ustawienia_komenda_lineedit.setGeometry(QtCore.QRect(110, 222, 111, 20))
                self.miner_ustawienia_komenda_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QLineEdit:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.miner_ustawienia_komenda_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_komenda_lineedit.setObjectName("miner_ustawienia_komenda_lineedit")
                self.miner_ustawienia_komendy_listwidget = QtWidgets.QListWidget(self.miner_ustawienia_frame)
                self.miner_ustawienia_komendy_listwidget.setGeometry(QtCore.QRect(230, 170, 131, 111))
                self.miner_ustawienia_komendy_listwidget.setStyleSheet("QListWidget {\n"
                "    outline: 0;\n"
                "    background-color: rgb(30, 30, 30);\n"
                "    border-radius: 15px;\n"
                "    border: 2px solid rgb(20, 20, 20);\n"
                "    color: white;\n"
                "    padding-top: 7px;\n"
                "    padding-bottom: 7px;\n"
                "    padding-left: 5px;\n"
                "    padding-right: 5px;\n"
                "}\n"
                "QListView::item {\n"
                "    border: 0px;\n"
                "    outline: 0;\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:selected{\n"
                "    color: white;\n"
                "    background-color: rgb(0, 100, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:hover {\n"
                "    background-color: rgb(0, 120, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QScrollBar:vertical {\n"
                "    background-color: rgb(30, 30, 30);\n"
                "    width: 10px;\n"
                "    border: 0px;\n"
                "}\n"
                "QScrollBar::handle:vertical {    \n"
                "    background-color: rgb(0, 180, 0);\n"
                "    width: 10px;\n"
                "    border-radius: 5px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::sub-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::add-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}")
                self.miner_ustawienia_komendy_listwidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
                self.miner_ustawienia_komendy_listwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_komendy_listwidget.setObjectName("miner_ustawienia_komendy_listwidget")
                #item = QtWidgets.QListWidgetItem()
                #self.miner_ustawienia_komendy_listwidget.addItem(item)
                #item = QtWidgets.QListWidgetItem()
                #self.miner_ustawienia_komendy_listwidget.addItem(item)
                #item = QtWidgets.QListWidgetItem()
                #self.miner_ustawienia_komendy_listwidget.addItem(item)
                #item = QtWidgets.QListWidgetItem()
                #self.miner_ustawienia_komendy_listwidget.addItem(item)
                #item = QtWidgets.QListWidgetItem()
                #self.miner_ustawienia_komendy_listwidget.addItem(item)
                self.miner_ustawienia_komenda_label = QtWidgets.QLabel(self.miner_ustawienia_frame)
                self.miner_ustawienia_komenda_label.setGeometry(QtCore.QRect(40, 220, 61, 21))
                self.miner_ustawienia_komenda_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_ustawienia_komenda_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_ustawienia_komenda_label.setObjectName("miner_ustawienia_komenda_label")
                self.miner_ustawienia_komendy_dodaj_pushbutton = PushButton(self.miner_ustawienia_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_ustawienia_komendy_dodaj_pushbutton.setGeometry(QtCore.QRect(40, 250, 80, 30))
                self.miner_ustawienia_komendy_dodaj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_komendy_dodaj_pushbutton.clicked.connect(lambda: self.miner_komendy_listwidget("add"))
                self.miner_ustawienia_komendy_dodaj_pushbutton.setObjectName("miner_ustawienia_komendy_dodaj_pushbutton")
                self.miner_ustawienia_komendy_wyczysc_pushbutton = PushButton(self.miner_ustawienia_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_ustawienia_komendy_wyczysc_pushbutton.setGeometry(QtCore.QRect(140, 250, 80, 30))
                self.miner_ustawienia_komendy_wyczysc_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_komendy_wyczysc_pushbutton.clicked.connect(lambda: self.miner_komendy_listwidget("clear"))
                self.miner_ustawienia_komendy_wyczysc_pushbutton.setObjectName("miner_ustawienia_komendy_wyczysc_pushbutton")
                self.miner_ustawienia_ilosc_okrazen_spinbox = QtWidgets.QSpinBox(self.miner_ustawienia_frame)
                self.miner_ustawienia_ilosc_okrazen_spinbox.setGeometry(QtCore.QRect(175, 200, 45, 20))
                self.miner_ustawienia_ilosc_okrazen_spinbox.setStyleSheet("QSpinBox {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 8px;\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QSpinBox:hover {\n"
                "    color: rgb(255, 255, 255);\n"
                "}\n"
                "QSpinBox::up-button {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "    border-top: 1px solid rgb(30, 30, 30);\n"
                "    border-right: 1px solid rgb(30, 30, 30);\n"
                "    border-top-right-radius: 8px;\n"
                "    border-bottom-left-radius: 5px;\n"
                "    margin-bottom: 1px;\n"
                "}\n"
                "QSpinBox::down-button {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "    border-bottom: 1px solid rgb(30, 30, 30);\n"
                "    border-right: 1px solid rgb(30, 30, 30);\n"
                "    border-bottom-right-radius: 8px;\n"
                "    border-top-left-radius: 5px;\n"
                "    margin-top: 1px;\n"
                "}\n"
                "QSpinBox::up-button:hover {\n"
                "    background-color: rgb(0, 165, 0);\n"
                "}\n"
                "QSpinBox::down-button:hover {\n"
                "    background-color: rgb(0, 165, 0);\n"
                "}")
                self.miner_ustawienia_ilosc_okrazen_spinbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_ustawienia_ilosc_okrazen_spinbox.setObjectName("miner_ustawienia_ilosc_okrazen_spinbox")
                self.miner_wykryte_okna_frame = QtWidgets.QFrame(self.miner_page)
                self.miner_wykryte_okna_frame.setGeometry(QtCore.QRect(415, 20, 380, 170))
                self.miner_wykryte_okna_frame.setAcceptDrops(False)
                self.miner_wykryte_okna_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.miner_wykryte_okna_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.miner_wykryte_okna_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.miner_wykryte_okna_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.miner_wykryte_okna_frame.setObjectName("miner_wykryte_okna_frame")
                self.miner_wykryte_okna_label = QtWidgets.QLabel(self.miner_wykryte_okna_frame)
                self.miner_wykryte_okna_label.setGeometry(QtCore.QRect(20, 10, 250, 30))
                self.miner_wykryte_okna_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_wykryte_okna_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_wykryte_okna_label.setObjectName("miner_wykryte_okna_label")
                self.miner_wykryte_okna_count_label = QtWidgets.QLabel(self.miner_wykryte_okna_frame)
                self.miner_wykryte_okna_count_label.setGeometry(QtCore.QRect(140, 10, 21, 30))
                self.miner_wykryte_okna_count_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: rgb(0, 165, 0);\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_wykryte_okna_count_label.setObjectName("miner_wykryte_okna_count_label")
                self.miner_wykryte_okna_odswiez_pushbutton = PushButton(self.miner_wykryte_okna_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_wykryte_okna_odswiez_pushbutton.setGeometry(QtCore.QRect(35, 130, 80, 30))
                self.miner_wykryte_okna_odswiez_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_wykryte_okna_odswiez_pushbutton.clicked.connect(lambda: self.miner_wykrywanie_okien())
                self.miner_wykryte_okna_odswiez_pushbutton.setObjectName("miner_wykryte_okna_odswiez_pushbutton")
                self.miner_wykryte_okna_przywroc_pushbutton = PushButton(self.miner_wykryte_okna_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_wykryte_okna_przywroc_pushbutton.setGeometry(QtCore.QRect(150, 130, 80, 30))
                self.miner_wykryte_okna_przywroc_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_wykryte_okna_przywroc_pushbutton.setObjectName("miner_wykryte_okna_przywroc_pushbutton")
                self.miner_wykryte_okna_podglad_pushbutton = PushButton(self.miner_wykryte_okna_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.miner_wykryte_okna_podglad_pushbutton.setGeometry(QtCore.QRect(265, 130, 80, 30))
                self.miner_wykryte_okna_podglad_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_wykryte_okna_podglad_pushbutton.setObjectName("miner_wykryte_okna_podglad_pushbutton")
                self.miner_wykryte_okna_listwidget = QtWidgets.QListWidget(self.miner_wykryte_okna_frame)
                self.miner_wykryte_okna_listwidget.setGeometry(QtCore.QRect(29, 50, 321, 76))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift SemiBold")
                self.miner_wykryte_okna_listwidget.setFont(font)
                self.miner_wykryte_okna_listwidget.setAcceptDrops(False)
                self.miner_wykryte_okna_listwidget.setStyleSheet("QListWidget {\n"
                "    outline: 0;\n"
                "    background-color: rgb(30, 30, 30);\n"
                "    border-radius: 15px;\n"
                "    border: 2px solid rgb(20, 20, 20);\n"
                "    color: white;\n"
                "    padding-top: 7px;\n"
                "    padding-bottom: 7px;\n"
                "    padding-left: 5px;\n"
                "    padding-right: 5px;\n"
                "}\n"
                "QListView::item {\n"
                "    border: 0px;\n"
                "    outline: 0;\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:selected{\n"
                "    color: white;\n"
                "    background-color: rgb(0, 100, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QListView::item:hover {\n"
                "    background-color: rgb(0, 120, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "QScrollBar:vertical {\n"
                "    background-color: rgb(30, 30, 30);\n"
                "    width: 10px;\n"
                "    border: 0px;\n"
                "}\n"
                "QScrollBar::handle:vertical {    \n"
                "    background-color: rgb(0, 180, 0);\n"
                "    width: 10px;\n"
                "    border-radius: 5px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::sub-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::add-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}")
                self.miner_wykryte_okna_listwidget.setProperty("showDropIndicator", False)
                self.miner_wykryte_okna_listwidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
                self.miner_wykryte_okna_listwidget.setTextElideMode(QtCore.Qt.ElideMiddle)
                self.miner_wykryte_okna_listwidget.setResizeMode(QtWidgets.QListView.Adjust)
                self.miner_wykryte_okna_listwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.miner_wykryte_okna_listwidget.setObjectName("miner_wykryte_okna_listwidget")
                self.miner_statystyki_frame = QtWidgets.QFrame(self.miner_page)
                self.miner_statystyki_frame.setGeometry(QtCore.QRect(20, 460, 780, 80))
                self.miner_statystyki_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.miner_statystyki_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.miner_statystyki_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.miner_statystyki_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.miner_statystyki_frame.setObjectName("miner_statystyki_frame")
                self.miner_statystyki_label = QtWidgets.QLabel(self.miner_statystyki_frame)
                self.miner_statystyki_label.setGeometry(QtCore.QRect(20, 10, 70, 25))
                self.miner_statystyki_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_statystyki_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_statystyki_label.setAlignment(QtCore.Qt.AlignCenter)
                self.miner_statystyki_label.setObjectName("miner_statystyki_label")
                self.miner_statystyki_czas_kopania_label = QtWidgets.QLabel(self.miner_statystyki_frame)
                self.miner_statystyki_czas_kopania_label.setGeometry(QtCore.QRect(100, 30, 131, 31))
                self.miner_statystyki_czas_kopania_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_statystyki_czas_kopania_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_statystyki_czas_kopania_label.setObjectName("miner_statystyki_czas_kopania_label")
                self.miner_statystyki_przebyte_kratki_label = QtWidgets.QLabel(self.miner_statystyki_frame)
                self.miner_statystyki_przebyte_kratki_label.setGeometry(QtCore.QRect(240, 30, 141, 31))
                self.miner_statystyki_przebyte_kratki_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_statystyki_przebyte_kratki_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_statystyki_przebyte_kratki_label.setObjectName("miner_statystyki_przebyte_kratki_label")
                self.miner_statystyki_wykopany_kamien_label = QtWidgets.QLabel(self.miner_statystyki_frame)
                self.miner_statystyki_wykopany_kamien_label.setGeometry(QtCore.QRect(390, 30, 161, 31))
                self.miner_statystyki_wykopany_kamien_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_statystyki_wykopany_kamien_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_statystyki_wykopany_kamien_label.setObjectName("miner_statystyki_wykopany_kamien_label")
                self.miner_statystyki_zarobione_pieniadze_label = QtWidgets.QLabel(self.miner_statystyki_frame)
                self.miner_statystyki_zarobione_pieniadze_label.setGeometry(QtCore.QRect(560, 30, 171, 31))
                self.miner_statystyki_zarobione_pieniadze_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.miner_statystyki_zarobione_pieniadze_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.miner_statystyki_zarobione_pieniadze_label.setObjectName("miner_statystyki_zarobione_pieniadze_label")
                self.stackedWidget.addWidget(self.miner_page)
                self.premium_page = QtWidgets.QWidget()
                self.premium_page.setObjectName("premium_page")
                self.premium_passhunter_frame = QtWidgets.QFrame(self.premium_page)
                self.premium_passhunter_frame.setGeometry(QtCore.QRect(20, 20, 380, 250))
                self.premium_passhunter_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}\n"
                "")
                self.premium_passhunter_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.premium_passhunter_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.premium_passhunter_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.premium_passhunter_frame.setObjectName("premium_passhunter_frame")
                self.premium_passhunter_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_label.setGeometry(QtCore.QRect(20, 10, 80, 25))
                self.premium_passhunter_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_label.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_passhunter_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_label.setObjectName("premium_passhunter_label")
                self.premium_passhunter_threads_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_threads_label.setGeometry(QtCore.QRect(30, 100, 101, 31))
                self.premium_passhunter_threads_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_threads_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_threads_label.setObjectName("premium_passhunter_threads_label")
                self.premium_passhunter_adresy_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_adresy_label.setGeometry(QtCore.QRect(30, 140, 231, 31))
                self.premium_passhunter_adresy_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_adresy_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_adresy_label.setObjectName("premium_passhunter_adresy_label")
                self.premium_passhunter_znalezione_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_znalezione_label.setGeometry(QtCore.QRect(30, 170, 181, 31))
                self.premium_passhunter_znalezione_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_znalezione_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_znalezione_label.setObjectName("premium_passhunter_znalezione_label")
                self.premium_passhunter_threads_slider = QtWidgets.QSlider(self.premium_passhunter_frame)
                self.premium_passhunter_threads_slider.setGeometry(QtCore.QRect(230, 105, 131, 20))
                self.premium_passhunter_threads_slider.setStyleSheet("background-color: none;")
                self.premium_passhunter_threads_slider.setMinimum(1)
                self.premium_passhunter_threads_slider.setMaximum(30)
                self.premium_passhunter_threads_slider.setValue(1)
                self.premium_passhunter_threads_slider.setOrientation(QtCore.Qt.Horizontal)
                self.premium_passhunter_threads_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.premium_passhunter_threads_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_passhunter_threads_slider.setObjectName("premium_passhunter_threads_slider")
                self.premium_passhunter_start_pushbutton = PushButton(self.premium_passhunter_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_passhunter_start_pushbutton.setGeometry(QtCore.QRect(140, 50, 70, 30))
                self.premium_passhunter_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_passhunter_start_pushbutton.setObjectName("premium_passhunter_start_pushbutton")
                self.premium_passhunter_stop_pushbutton = PushButton(self.premium_passhunter_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_passhunter_stop_pushbutton.setGeometry(QtCore.QRect(220, 50, 70, 30))
                self.premium_passhunter_stop_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_passhunter_stop_pushbutton.setObjectName("premium_passhunter_stop_pushbutton")
                self.premium_passhunter_status_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_status_label.setGeometry(QtCore.QRect(30, 50, 51, 31))
                self.premium_passhunter_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_status_label.setObjectName("premium_passhunter_status_label")
                self.premium_passhunter_current_status_label = QtWidgets.QLabel(self.premium_passhunter_frame)
                self.premium_passhunter_current_status_label.setGeometry(QtCore.QRect(80, 50, 31, 31))
                self.premium_passhunter_current_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_passhunter_current_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_passhunter_current_status_label.setObjectName("premium_passhunter_current_status_label")
                self.premium_passhunter_zaladuj_pushbutton = PushButton(self.premium_passhunter_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_passhunter_zaladuj_pushbutton.setGeometry(QtCore.QRect(300, 50, 70, 30))
                self.premium_passhunter_zaladuj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_passhunter_zaladuj_pushbutton.setObjectName("premium_passhunter_zaladuj_pushbutton")
                self.premium_passhunter_progressbar = QtWidgets.QProgressBar(self.premium_passhunter_frame)
                self.premium_passhunter_progressbar.setGeometry(QtCore.QRect(50, 210, 271, 23))
                self.premium_passhunter_progressbar.setProperty("value", 0)
                self.premium_passhunter_progressbar.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_passhunter_progressbar.setStyleSheet("QProgressBar {\n"
                #"    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 10px;\n"
                "    color: black;\n"
                "}\n"
                "QProgressBar::chunk {\n"
                "    background-color: rgb(0,255,0);\n"
                "    border-radius :5px;\n"
                "}  ")
                self.premium_passhunter_progressbar.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_passhunter_progressbar.setObjectName("premium_passhunter_progressbar")
                self.premium_dehasher_frame = QtWidgets.QFrame(self.premium_page)
                self.premium_dehasher_frame.setGeometry(QtCore.QRect(415, 20, 380, 250))
                self.premium_dehasher_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                "    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.premium_dehasher_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.premium_dehasher_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.premium_dehasher_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.premium_dehasher_frame.setObjectName("premium_dehasher_frame")
                self.premium_dehasher_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_label.setGeometry(QtCore.QRect(20, 10, 71, 25))
                self.premium_dehasher_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_label.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_dehasher_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_label.setObjectName("premium_dehasher_label")
                self.premium_dehasher_threads_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_threads_label.setGeometry(QtCore.QRect(30, 100, 101, 31))
                self.premium_dehasher_threads_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_threads_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_threads_label.setObjectName("premium_dehasher_threads_label")
                self.premium_dehasher_zaszyfrowane_hasla_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_zaszyfrowane_hasla_label.setGeometry(QtCore.QRect(30, 140, 231, 31))
                self.premium_dehasher_zaszyfrowane_hasla_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_zaszyfrowane_hasla_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_zaszyfrowane_hasla_label.setObjectName("premium_dehasher_zaszyfrowane_hasla_label")
                self.premium_dehasher_znalezione_hasla_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_znalezione_hasla_label.setGeometry(QtCore.QRect(30, 170, 181, 31))
                self.premium_dehasher_znalezione_hasla_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_znalezione_hasla_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_znalezione_hasla_label.setObjectName("premium_dehasher_znalezione_hasla_label")
                self.premium_dehasher_threads_slider = QtWidgets.QSlider(self.premium_dehasher_frame)
                self.premium_dehasher_threads_slider.setGeometry(QtCore.QRect(230, 105, 131, 20))
                self.premium_dehasher_threads_slider.setStyleSheet("background-color: none;")
                self.premium_dehasher_threads_slider.setMinimum(1)
                self.premium_dehasher_threads_slider.setMaximum(50)
                self.premium_dehasher_threads_slider.setValue(1)
                self.premium_dehasher_threads_slider.setOrientation(QtCore.Qt.Horizontal)
                self.premium_dehasher_threads_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.premium_dehasher_threads_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dehasher_threads_slider.setObjectName("premium_dehasher_threads_slider")
                self.premium_dehasher_start_pushbutton = PushButton(self.premium_dehasher_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_dehasher_start_pushbutton.setGeometry(QtCore.QRect(140, 50, 70, 30))
                self.premium_dehasher_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dehasher_start_pushbutton.setObjectName("premium_dehasher_start_pushbutton")
                self.premium_dehasher_stop_button = PushButton(self.premium_dehasher_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_dehasher_stop_button.setGeometry(QtCore.QRect(220, 50, 70, 30))
                self.premium_dehasher_stop_button.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dehasher_stop_button.setObjectName("premium_dehasher_stop_button")
                self.premium_dehasher_status_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_status_label.setGeometry(QtCore.QRect(30, 50, 51, 31))
                self.premium_dehasher_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_status_label.setObjectName("premium_dehasher_status_label")
                self.premium_dehasher_current_status_label = QtWidgets.QLabel(self.premium_dehasher_frame)
                self.premium_dehasher_current_status_label.setGeometry(QtCore.QRect(80, 50, 31, 31))
                self.premium_dehasher_current_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dehasher_current_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dehasher_current_status_label.setObjectName("premium_dehasher_current_status_label")
                self.premium_dehasher_zaladuj_pushbutton = PushButton(self.premium_dehasher_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_dehasher_zaladuj_pushbutton.setGeometry(QtCore.QRect(300, 50, 70, 30))
                self.premium_dehasher_zaladuj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dehasher_zaladuj_pushbutton.setObjectName("premium_dehasher_zaladuj_pushbutton")
                self.premium_dehasher_progressbar = QtWidgets.QProgressBar(self.premium_dehasher_frame)
                self.premium_dehasher_progressbar.setGeometry(QtCore.QRect(50, 210, 271, 23))
                self.premium_dehasher_progressbar.setProperty("value", 0)
                self.premium_dehasher_progressbar.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_dehasher_progressbar.setStyleSheet("QProgressBar {\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 10px;\n"
                "    color: black;\n"
                "}\n"
                "QProgressBar::chunk {\n"
                "    background-color: rgb(0,255,0);\n"
                "    border-radius :5px;\n"
                "}  ")
                self.premium_dehasher_progressbar.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dehasher_progressbar.setObjectName("premium_dehasher_progressbar")
                self.premium_dork_generator_frame = QtWidgets.QFrame(self.premium_page)
                self.premium_dork_generator_frame.setGeometry(QtCore.QRect(20, 290, 380, 250))
                self.premium_dork_generator_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.premium_dork_generator_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.premium_dork_generator_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.premium_dork_generator_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.premium_dork_generator_frame.setObjectName("premium_dork_generator_frame")
                self.premium_dork_generator_label = QtWidgets.QLabel(self.premium_dork_generator_frame)
                self.premium_dork_generator_label.setGeometry(QtCore.QRect(20, 10, 101, 25))
                self.premium_dork_generator_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dork_generator_label.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_dork_generator_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dork_generator_label.setObjectName("premium_dork_generator_label")
                self.premium_dork_generator_count_label = QtWidgets.QLabel(self.premium_dork_generator_frame)
                self.premium_dork_generator_count_label.setGeometry(QtCore.QRect(30, 100, 101, 31))
                self.premium_dork_generator_count_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dork_generator_count_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dork_generator_count_label.setObjectName("premium_dork_generator_count_label")
                self.premium_dork_generator_count_slider = QtWidgets.QSlider(self.premium_dork_generator_frame)
                self.premium_dork_generator_count_slider.setGeometry(QtCore.QRect(230, 105, 131, 20))
                self.premium_dork_generator_count_slider.setStyleSheet("background-color: none;")
                self.premium_dork_generator_count_slider.setMinimum(1)
                self.premium_dork_generator_count_slider.setMaximum(1000000)
                self.premium_dork_generator_count_slider.setValue(1)
                self.premium_dork_generator_count_slider.setOrientation(QtCore.Qt.Horizontal)
                self.premium_dork_generator_count_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.premium_dork_generator_count_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dork_generator_count_slider.setObjectName("premium_dork_generator_count_slider")
                self.premium_dork_generator_start_pushbutton = PushButton(self.premium_dork_generator_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_dork_generator_start_pushbutton.setGeometry(QtCore.QRect(220, 50, 70, 30))
                self.premium_dork_generator_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dork_generator_start_pushbutton.setObjectName("premium_dork_generator_start_pushbutton")
                self.premium_dork_generator_stop_pushbutton = PushButton(self.premium_dork_generator_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_dork_generator_stop_pushbutton.setGeometry(QtCore.QRect(300, 50, 70, 30))
                self.premium_dork_generator_stop_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dork_generator_stop_pushbutton.setObjectName("premium_dork_generator_stop_pushbutton")
                self.premium_dork_generator_status_label = QtWidgets.QLabel(self.premium_dork_generator_frame)
                self.premium_dork_generator_status_label.setGeometry(QtCore.QRect(30, 50, 51, 31))
                self.premium_dork_generator_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dork_generator_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dork_generator_status_label.setObjectName("premium_dork_generator_status_label")
                self.premium_dork_generator_current_status_label = QtWidgets.QLabel(self.premium_dork_generator_frame)
                self.premium_dork_generator_current_status_label.setGeometry(QtCore.QRect(80, 50, 31, 31))
                self.premium_dork_generator_current_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_dork_generator_current_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_dork_generator_current_status_label.setObjectName("premium_dork_generator_current_status_label")
                self.premium_dork_generator_progressbar = QtWidgets.QProgressBar(self.premium_dork_generator_frame)
                self.premium_dork_generator_progressbar.setGeometry(QtCore.QRect(50, 210, 271, 23))
                self.premium_dork_generator_progressbar.setProperty("value", 0)
                self.premium_dork_generator_progressbar.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_dork_generator_progressbar.setStyleSheet("QProgressBar {\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 10px;\n"
                "    color: black;\n"
                "}\n"
                "QProgressBar::chunk {\n"
                "    background-color: rgb(0,255,0);\n"
                "    border-radius :5px;\n"
                "}  ")
                self.premium_dork_generator_progressbar.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_dork_generator_progressbar.setObjectName("premium_dork_generator_progressbar")
                self.premium_keyword_scraper_frame = QtWidgets.QFrame(self.premium_page)
                self.premium_keyword_scraper_frame.setGeometry(QtCore.QRect(415, 290, 380, 250))
                self.premium_keyword_scraper_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}\n"
                "")
                self.premium_keyword_scraper_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.premium_keyword_scraper_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.premium_keyword_scraper_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.premium_keyword_scraper_frame.setObjectName("premium_keyword_scraper_frame")
                self.premium_keyword_scraper_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_label.setGeometry(QtCore.QRect(20, 10, 111, 25))
                self.premium_keyword_scraper_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_label.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_keyword_scraper_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_label.setObjectName("premium_keyword_scraper_label")
                self.premium_keyword_scraper_threads_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_threads_label.setGeometry(QtCore.QRect(30, 100, 101, 31))
                self.premium_keyword_scraper_threads_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_threads_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_threads_label.setObjectName("premium_keyword_scraper_threads_label")
                self.premium_keyword_scraper_bazowe_slowa_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_bazowe_slowa_label.setGeometry(QtCore.QRect(30, 140, 231, 31))
                self.premium_keyword_scraper_bazowe_slowa_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_bazowe_slowa_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_bazowe_slowa_label.setObjectName("premium_keyword_scraper_bazowe_slowa_label")
                self.premium_keyword_scraper_znalezione_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_znalezione_label.setGeometry(QtCore.QRect(30, 170, 191, 31))
                self.premium_keyword_scraper_znalezione_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_znalezione_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_znalezione_label.setObjectName("premium_keyword_scraper_znalezione_label")
                self.premium_keyword_scraper_threads_slider = QtWidgets.QSlider(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_threads_slider.setGeometry(QtCore.QRect(230, 105, 131, 20))
                self.premium_keyword_scraper_threads_slider.setStyleSheet("background-color: none;")
                self.premium_keyword_scraper_threads_slider.setMinimum(1)
                self.premium_keyword_scraper_threads_slider.setMaximum(50)
                self.premium_keyword_scraper_threads_slider.setValue(1)
                self.premium_keyword_scraper_threads_slider.setOrientation(QtCore.Qt.Horizontal)
                self.premium_keyword_scraper_threads_slider.setStyleSheet("QSlider {\n"
                "    background-color: none;\n"
                "    margin: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QSlider::groove::horizontal {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(120, 255, 120);\n"
                "}\n"
                "QSlider::groove:horizontal::hover {\n"
                "    background-color: rgb(0, 250, 0);\n"
                "}\n"
                "QSlider::handle:horizontal {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(0, 120, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:hover {\n"
                "    background-color: rgb(0, 150, 0);\n"
                "}\n"
                "QSlider::handle:horizontal:pressed {\n"
                "    background-color: rgb(0, 200, 0);\n"
                "}\n"
                "\n"
                "\n"
                "QSlider::groove::vertical {\n"
                "    border-radius: 5px;\n"
                "    height: 10px;\n"
                "    margin: 0px;\n"
                "    background-color: rgb(54, 59, 72);\n"
                "}\n"
                "QSlider::groove:vertical::hover {\n"
                "    background-color: rgb(55, 53, 12);\n"
                "}\n"
                "QSlider::handle:vertical {\n"
                "    border: none;\n"
                "    height: 10px;\n"
                "    width: 10px;\n"
                "    margin: 0px;\n"
                "    border-radius: 5px;\n"
                "    background-color: rgb(89, 147, 29);\n"
                "}\n"
                "QSlider::handle:vertical:hover {\n"
                "    background-color: rgb(100, 200, 10);\n"
                "}\n"
                "QSlider::handle:vertical:pressed {\n"
                "    background-color: rgb(10, 150, 10);\n"
                "}")
                self.premium_keyword_scraper_threads_slider.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_keyword_scraper_threads_slider.setObjectName("premium_keyword_scraper_threads_slider")
                self.premium_keyword_scraper_start_pushbutton = PushButton(self.premium_keyword_scraper_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_keyword_scraper_start_pushbutton.setGeometry(QtCore.QRect(140, 50, 70, 30))
                self.premium_keyword_scraper_start_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_keyword_scraper_start_pushbutton.setObjectName("premium_keyword_scraper_start_pushbutton")
                self.premium_keyword_scraper_stop_pushbutton = PushButton(self.premium_keyword_scraper_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_keyword_scraper_stop_pushbutton.setGeometry(QtCore.QRect(220, 50, 70, 30))
                self.premium_keyword_scraper_stop_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_keyword_scraper_stop_pushbutton.setObjectName("premium_keyword_scraper_stop_pushbutton")
                self.premium_keyword_scraper_status_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_status_label.setGeometry(QtCore.QRect(30, 50, 51, 31))
                self.premium_keyword_scraper_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_status_label.setObjectName("premium_keyword_scraper_status_label")
                self.premium_keyword_scraper_current_status_label = QtWidgets.QLabel(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_current_status_label.setGeometry(QtCore.QRect(80, 50, 31, 31))
                self.premium_keyword_scraper_current_status_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: red;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.premium_keyword_scraper_current_status_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 200)))
                self.premium_keyword_scraper_current_status_label.setObjectName("premium_keyword_scraper_current_status_label")
                self.premium_keyword_scraper_zaladuj_pushbutton = PushButton(self.premium_keyword_scraper_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.premium_keyword_scraper_zaladuj_pushbutton.setGeometry(QtCore.QRect(300, 50, 70, 30))
                self.premium_keyword_scraper_zaladuj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_keyword_scraper_zaladuj_pushbutton.setObjectName("premium_keyword_scraper_zaladuj_pushbutton")
                self.premium_keyword_scraper_progressbar = QtWidgets.QProgressBar(self.premium_keyword_scraper_frame)
                self.premium_keyword_scraper_progressbar.setGeometry(QtCore.QRect(50, 210, 271, 23))
                self.premium_keyword_scraper_progressbar.setProperty("value", 0)
                self.premium_keyword_scraper_progressbar.setAlignment(QtCore.Qt.AlignCenter)
                self.premium_keyword_scraper_progressbar.setStyleSheet("QProgressBar {\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    border-radius: 10px;\n"
                "    color: black;\n"
                "}\n"
                "QProgressBar::chunk {\n"
                "    background-color: rgb(0,255,0);\n"
                "    border-radius :5px;\n"
                "}  ")
                self.premium_keyword_scraper_progressbar.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.premium_keyword_scraper_progressbar.setObjectName("premium_keyword_scraper_progressbar")
                self.stackedWidget.addWidget(self.premium_page)
                self.ustawienia_page = QtWidgets.QWidget()
                self.ustawienia_page.setObjectName("ustawienia_page")
                self.ustawienia_skin_frame = QtWidgets.QFrame(self.ustawienia_page)
                self.ustawienia_skin_frame.setGeometry(QtCore.QRect(590, 80, 200, 360))
                self.ustawienia_skin_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.ustawienia_skin_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.ustawienia_skin_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.ustawienia_skin_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.ustawienia_skin_frame.setObjectName("ustawienia_skin_frame")
                self.ustawienia_skin_frame_nick_label = QtWidgets.QLabel(self.ustawienia_skin_frame)
                self.ustawienia_skin_frame_nick_label.setGeometry(QtCore.QRect(10, 10, 181, 20))
                self.ustawienia_skin_frame_nick_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.ustawienia_skin_frame_nick_label.setAlignment(QtCore.Qt.AlignCenter)
                self.ustawienia_skin_frame_nick_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
                self.ustawienia_skin_frame_nick_label.setObjectName("ustawienia_skin_frame_nick_label")
                self.ustawienia_skin_frame_skin_display_label = QtWidgets.QLabel(self.ustawienia_skin_frame)
                self.ustawienia_skin_frame_skin_display_label.setGeometry(QtCore.QRect(0, 22, 201, 321))
                self.ustawienia_skin_frame_skin_display_label.setStyleSheet("QLabel {\n"
                f"    background-image: url(img/srumi.png);\n"
                "    border: none;\n"
                "    background-color: none;\n"
                "}")
                self.ustawienia_skin_frame_skin_display_label.setText("")
                self.ustawienia_skin_frame_skin_display_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.ustawienia_skin_frame_skin_display_label.setObjectName("ustawienia_skin_frame_skin_display_label")
                self.ustawienia_config_frame = QtWidgets.QFrame(self.ustawienia_page)
                self.ustawienia_config_frame.setGeometry(QtCore.QRect(20, 60, 531, 401))
                self.ustawienia_config_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(40, 40, 40);\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    border-radius: 20px;\n"
                "}")
                self.ustawienia_config_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.ustawienia_config_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.ustawienia_config_frame.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.ustawienia_config_frame.setObjectName("ustawienia_config_frame")
                self.ustawienia_config_label = QtWidgets.QLabel(self.ustawienia_config_frame)
                self.ustawienia_config_label.setGeometry(QtCore.QRect(20, 10, 75, 25))
                self.ustawienia_config_label.setStyleSheet("QLabel {\n"
                "    border-top: none;\n"
                "    border-right: none;\n"
                "    border-left: none;\n"
                "    border-bottom: 1px solid rgba(0, 250, 0, 160);\n"
                "    margin-left: 1px;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 10pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.ustawienia_config_label.setAlignment(QtCore.Qt.AlignCenter)
                self.ustawienia_config_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
                self.ustawienia_config_label.setObjectName("ustawienia_config_label")
                self.ustawienia_config_lista_configow_listwidget = QtWidgets.QListWidget(self.ustawienia_config_frame)
                self.ustawienia_config_lista_configow_listwidget.setGeometry(QtCore.QRect(30, 140, 181, 121))
                font = QtGui.QFont()
                font.setFamily("Bahnschrift SemiBold")
                self.ustawienia_config_lista_configow_listwidget.setFont(font)
                self.ustawienia_config_lista_configow_listwidget.setStyleSheet("QListWidget {\n"
                "    background-color: rgb(35, 35, 35);\n"
                "    border-radius: 15px;\n"
                #"    border: 2px solid rgb(20, 20, 20);\n"
                "    color: white;\n"
                "    padding-top: 7px;\n"
                "    padding-bottom: 7px;\n"
                "    padding-left: 5px;\n"
                "    padding-right: 5px;\n"
                "    outline: 0;\n"
                "}\n"
                "QListWidget::item {\n"
                "    margin-left: 1ex;\n"
                "    text-align: right;\n"
                "    border: 0px;\n"
                "    outline: 0;\n"
                "}\n"
                "\n"
                "QListWidget::item:selected {\n"
                "    color: black;\n"
                "    background-color: rgb(0, 255, 0);\n"
                "    border: 1px solid rgb(0, 155, 0);\n"
                "    border-radius: 5px;\n"
                "    outline: 0;\n"
                "}\n"
                "\n"
                "QListWidget::item:selected:active {\n"
                "    color: black;\n"
                "    background-color: rgb(0, 255, 0);\n"
                "    border: 1px solid rgb(0, 155, 0);\n"
                "    border-radius: 5px;\n"
                "    outline: 0;\n"
                "}\n"
                "\n"
                "QListWidget::item:hover {\n"
                "    color: black;\n"
                "    background-color: rgb(0, 255, 0);\n"
                "    border: 1px solid rgb(0, 155, 0);\n"
                "    border-radius: 5px;\n"
                "}\n"
                "\n"
                "QScrollBar:vertical {\n"
                "    background-color: rgb(35, 35, 35);\n"
                "    width: 10px;\n"
                "    border: 0px;\n"
                "}\n"
                "QScrollBar::handle:vertical {\n"
                "    background-color: rgb(0, 180, 0);\n"
                "    width: 10px;\n"
                "    border-radius: 5px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::sub-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::add-line:vertical {\n"
                "    border: none;\n"
                "    height: 0px;\n"
                "}\n"
                "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}\n"
                "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                "    background: none;\n"
                "    height: 0px;\n"
                "    border: none;\n"
                "}")
                self.ustawienia_config_lista_configow_listwidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
                self.ustawienia_config_lista_configow_listwidget.setTextElideMode(QtCore.Qt.ElideMiddle)
                self.ustawienia_config_lista_configow_listwidget.setResizeMode(QtWidgets.QListView.Adjust)
                self.ustawienia_config_lista_configow_listwidget.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=20, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.ustawienia_config_lista_configow_listwidget.setObjectName("ustawienia_config_lista_configow_listwidget")
                self.ustawienia_config_generator_wczytaj_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_generator_wczytaj_pushbutton.setGeometry(QtCore.QRect(440, 50, 70, 30))
                self.ustawienia_config_generator_wczytaj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_generator_wczytaj_pushbutton.setObjectName("ustawienia_config_generator_wczytaj_pushbutton")
                self.ustawienia_config_usun_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_usun_pushbutton.setGeometry(QtCore.QRect(120, 340, 70, 30))
                self.ustawienia_config_usun_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_usun_pushbutton.setObjectName("ustawienia_config_usun_pushbutton")
                self.ustawienia_config_generator_generuj_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_generator_generuj_pushbutton.setGeometry(QtCore.QRect(360, 50, 70, 30))
                self.ustawienia_config_generator_generuj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_generator_generuj_pushbutton.setObjectName("ustawienia_config_generator_generuj_pushbutton")
                self.ustawienia_config_dodaj_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_dodaj_pushbutton.setGeometry(QtCore.QRect(40, 340, 70, 30))
                self.ustawienia_config_dodaj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_dodaj_pushbutton.setObjectName("ustawienia_config_dodaj_pushbutton")
                self.ustawienia_config_nazwa_lineedit = QtWidgets.QLineEdit(self.ustawienia_config_frame)
                self.ustawienia_config_nazwa_lineedit.setGeometry(QtCore.QRect(40, 270, 161, 20))
                self.ustawienia_config_nazwa_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QLineEdit:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.ustawienia_config_nazwa_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_nazwa_lineedit.setObjectName("ustawienia_config_nazwa_lineedit")
                self.ustawienia_config_generator_lineedit = QtWidgets.QLineEdit(self.ustawienia_config_frame)
                self.ustawienia_config_generator_lineedit.setGeometry(QtCore.QRect(190, 55, 161, 20))
                self.ustawienia_config_generator_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QLineEdit:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.ustawienia_config_generator_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_generator_lineedit.setObjectName("ustawienia_config_generator_lineedit")
                self.ustawienia_config_zapisz_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_zapisz_pushbutton.setGeometry(QtCore.QRect(120, 300, 70, 30))
                self.ustawienia_config_zapisz_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_zapisz_pushbutton.setObjectName("ustawienia_config_zapisz_pushbutton")
                self.ustawienia_config_wczytaj_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_config_wczytaj_pushbutton.setGeometry(QtCore.QRect(40, 300, 70, 30))
                self.ustawienia_config_wczytaj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_config_wczytaj_pushbutton.setObjectName("ustawienia_config_wczytaj_pushbutton")
                #self.ustawienia_config_kolory_combobox = QtWidgets.QComboBox(self.ustawienia_config_frame)
                #self.ustawienia_config_kolory_combobox.setGeometry(QtCore.QRect(430, 380, 69, 22))
                #self.ustawienia_config_kolory_combobox.addItem("")
                #self.ustawienia_config_kolory_combobox.addItem("")
                #self.ustawienia_config_kolory_combobox.setStyleSheet("QComboBox{\n"
                #"    border-radius: 5px;\n"
                #"    border: 1px solid black;\n"
                #"    padding: 0 5px 0 5px;\n"
                #"    color: white;\n"
                #"    background-color: rgb(65, 65, 65);\n"
                #"}\n"
                #"\n"
                #"QComboBox QAbstractItemView {\n"
                #"    outline: 0;\n"
                #"    border: none;\n"
                #"    color: white;\n"
                #"    selection-background-color: rgba(0, 200, 0, 50);\n"
                #"}\n"
                #"QComboBox::drop-down {\n"
                #"    padding: 0 3px 0 0;\n"
                #"    image: url(img/chevron-down.png);\n"
                #"    width: 15px;\n"
                #"    height: 20px;\n"
                #"}")
                #self.ustawienia_config_kolory_combobox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                #self.ustawienia_config_kolory_combobox.activated.connect(lambda: self.change_color(self.ustawienia_config_kolory_combobox.currentText()))
                #self.ustawienia_config_kolory_combobox.setObjectName(u"ustawienia_config_kolory_combobox")
                self.ustawienia_config_lista_label = QtWidgets.QLabel(self.ustawienia_config_frame)
                self.ustawienia_config_lista_label.setGeometry(QtCore.QRect(40, 110, 51, 30))
                self.ustawienia_config_lista_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.ustawienia_config_lista_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
                self.ustawienia_config_lista_label.setObjectName("ustawienia_config_lista_label")
                self.ustawienia_config_generator_label = QtWidgets.QLabel(self.ustawienia_config_frame)
                self.ustawienia_config_generator_label.setGeometry(QtCore.QRect(40, 50, 131, 30))
                self.ustawienia_config_generator_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.ustawienia_config_generator_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
                self.ustawienia_config_generator_label.setObjectName("ustawienia_config_generator_label")
                self.ustawienia_discord_id_label = QtWidgets.QLabel(self.ustawienia_config_frame)
                self.ustawienia_discord_id_label.setGeometry(QtCore.QRect(290, 110, 71, 30))
                self.ustawienia_discord_id_label.setStyleSheet("QLabel {\n"
                "    border: none;\n"
                "    border-radius: none;\n"
                "    color: white;\n"
                "    background-color: none;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.ustawienia_discord_id_label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(100, 100, 100, 250)))
                self.ustawienia_discord_id_label.setObjectName("ustawienia_discord_id_label")
                self.ustawienia_discord_id_lineedit = QtWidgets.QLineEdit(self.ustawienia_config_frame)
                self.ustawienia_discord_id_lineedit.setGeometry(QtCore.QRect(300, 145, 161, 20))
                self.ustawienia_discord_id_lineedit.setStyleSheet("QLineEdit {\n"
                "    background-color: rgb(65, 65, 65);\n"
                "    border-radius: 8px;\n"
                "    border: 2px solid rgb(30, 30, 30);\n"
                "    color: rgb(120, 255, 120);\n"
                "    padding: 1px 2px 2px 3px;\n"
                "}\n"
                "QLineEdit:hover {\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.ustawienia_discord_id_lineedit.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_discord_id_lineedit.setObjectName("ustawienia_discord_id_lineedit")
                self.ustawienia_discord_id_wczytaj_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_discord_id_wczytaj_pushbutton.setGeometry(QtCore.QRect(305, 170, 70, 30))
                self.ustawienia_discord_id_wczytaj_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_discord_id_wczytaj_pushbutton.setObjectName("ustawienia_discord_id_wczytaj_pushbutton")
                self.ustawienia_discord_id_zapisz_pushbutton = PushButton(self.ustawienia_config_frame, "#4CAF50", "#1e1e1e", "black", "#78ff78") #QtWidgets.Q
                self.ustawienia_discord_id_zapisz_pushbutton.setGeometry(QtCore.QRect(385, 170, 70, 30))
                self.ustawienia_discord_id_zapisz_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=30, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 150)))
                self.ustawienia_discord_id_zapisz_pushbutton.setObjectName("ustawienia_discord_id_zapisz_pushbutton")
                self.stackedWidget.addWidget(self.ustawienia_page)
                self.window_bar_frame = QtWidgets.QFrame(self.widget)
                self.window_bar_frame.setGeometry(QtCore.QRect(0, 0, 900, 35))
                self.window_bar_frame.setStyleSheet("QFrame {\n"
                "    background-color: rgb(0, 0, 0);\n"
                "    border-top-left-radius: 20px;\n"
                "    border-top-right-radius: 20px;\n"
                "    border-bottom-left-radius: 0px;\n"
                "    border-bottom-right-radius: 0px;\n"
                "    border-bottom: 1px solid rgb(40, 40, 40);\n"
                "}\n"
                "QLabel {\n"
                "    border: none;\n"
                "    color: white;\n"
                "    font: 11pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.window_bar_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.window_bar_frame.setObjectName("window_bar_frame")
                self.window_bar_pvp_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_pvp_label.setGeometry(QtCore.QRect(20, 7, 25, 20))
                self.window_bar_pvp_label.setAlignment(QtCore.Qt.AlignCenter)
                self.window_bar_pvp_label.setObjectName("window_bar_pvp_label")
                self.window_bar_booster_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_booster_label.setGeometry(QtCore.QRect(45, 7, 50, 20))
                self.window_bar_booster_label.setStyleSheet("QLabel {\n"
                "    color: rgb(0, 255, 0);\n"
                "}")
                self.window_bar_booster_label.setAlignment(QtCore.Qt.AlignCenter)
                self.window_bar_booster_label.setObjectName("window_bar_booster_label")
                self.window_bar_pvpbooster_przedzial_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_pvpbooster_przedzial_label.setGeometry(QtCore.QRect(110, 6, 1, 23))
                self.window_bar_pvpbooster_przedzial_label.setStyleSheet("QLabel {\n"
                "    background: rgb(30, 30, 30);\n"
                "}")
                self.window_bar_pvpbooster_przedzial_label.setText("")
                self.window_bar_pvpbooster_przedzial_label.setObjectName("window_bar_pvpbooster_przedzial_label")
                self.window_bar_pvpbooster_site_button = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_pvpbooster_site_button.clicked.connect(lambda: webbrowser.open('https://pvpbooster.pl', new=2))
                self.window_bar_pvpbooster_site_button.setGeometry(QtCore.QRect(740, 8, 20, 20))
                self.window_bar_pvpbooster_site_button.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/website.png);\n"
                "}")
                self.window_bar_pvpbooster_site_button.setText("")
                self.window_bar_pvpbooster_site_button.setObjectName("window_bar_pvpbooster_site_button")
                self.window_bar_discord_button = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_discord_button.clicked.connect(lambda: webbrowser.open('https://discord.gg/sW5TmXPH74', new=2))
                self.window_bar_discord_button.setGeometry(QtCore.QRect(770, 8, 20, 20))
                self.window_bar_discord_button.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/discord.png);\n"
                "}")
                self.window_bar_discord_button.setText("")
                self.window_bar_discord_button.setObjectName("window_bar_discord_button")
                self.window_bar_minimize_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_minimize_pushbutton.clicked.connect(lambda: self.showMinimized())
                self.window_bar_minimize_pushbutton.setGeometry(QtCore.QRect(830, 8, 20, 20))
                self.window_bar_minimize_pushbutton.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/subtract.png);\n"
                "}")
                self.window_bar_minimize_pushbutton.setText("")
                self.window_bar_minimize_pushbutton.setObjectName("window_bar_minimize_pushbutton")
                self.window_bar_close_pushbutton = QtWidgets.QPushButton(self.window_bar_frame)
                self.window_bar_close_pushbutton.clicked.connect(lambda: self.close())
                self.window_bar_close_pushbutton.setGeometry(QtCore.QRect(860, 8, 20, 20))
                self.window_bar_close_pushbutton.setStyleSheet("QPushButton {\n"
                "    border-radius: 5px;\n"
                "    background-color: none;\n"
                "    image: url(img/close.png);\n"
                "}")
                self.window_bar_close_pushbutton.setText("")
                self.window_bar_close_pushbutton.setObjectName("window_bar_close_pushbutton")
                self.window_bar_pvpbooster_przedzial_label_2 = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_pvpbooster_przedzial_label_2.setGeometry(QtCore.QRect(810, 6, 1, 23))
                self.window_bar_pvpbooster_przedzial_label_2.setStyleSheet("QLabel {\n"
                "    background: rgb(30, 30, 30);\n"
                "}")
                self.window_bar_pvpbooster_przedzial_label_2.setText("")
                self.window_bar_pvpbooster_przedzial_label_2.setObjectName("window_bar_pvpbooster_przedzial_label_2")
                self.window_bar_status_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_status_label.setGeometry(QtCore.QRect(125, 7, 171, 20))
                self.window_bar_status_label.setStyleSheet("QLabel {\n"
                "    color: white;\n"
                "    font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_status_label.setObjectName("window_bar_status_label")
                self.window_bar_personal_id_label = QtWidgets.QLabel(self.window_bar_frame)
                self.window_bar_personal_id_label.setGeometry(QtCore.QRect(669, 7, 61, 20))
                self.window_bar_personal_id_label.setStyleSheet("QLabel {\n"
                "	border: none;\n"
                "	border-radius: none;\n"
                "	color: white;\n"
                "	font: 12pt \"Bahnschrift SemiBold\";\n"
                "}")
                self.window_bar_personal_id_label.setObjectName(u"window_bar_personal_id_label")
                self.pages_frame = QtWidgets.QFrame(self.widget)
                self.pages_frame.setGeometry(QtCore.QRect(0, 35, 80, 565))
                self.pages_frame.setStyleSheet("QFrame {\n"
                "    border-right: 1px solid rgb(20, 20, 20);\n"
                "    background-color: rgb(45, 45, 45);\n"
                "    border-top-left-radius: 0px;\n"
                "    border-top-right-radius: 0px;\n"
                "    border-bottom-left-radius: 20px;\n"
                "    border-bottom-right-radius: 0px;\n"
                "}")
                self.pages_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.pages_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.pages_frame.setObjectName("pages_frame")
                self.pages_main_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_main_page_pushbutton.clicked.connect(lambda: self.change_page_main())
                self.pages_main_page_pushbutton.setGeometry(QtCore.QRect(10, 10, 60, 60))
                self.pages_main_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/minecraft_creeper_green.png);\n"
                "}")
                self.pages_main_page_pushbutton.setText("")
                self.pages_main_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(*self.shadow_color)))
                self.pages_main_page_pushbutton.setObjectName("pages_main_page_pushbutton")
                self.pages_clicker_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_clicker_page_pushbutton.clicked.connect(lambda: self.change_page_clicker())
                self.pages_clicker_page_pushbutton.setGeometry(QtCore.QRect(15, 100, 50, 50))
                self.pages_clicker_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/minecraft_sword_green.png);\n"
                "}")
                self.pages_clicker_page_pushbutton.setText("")
                self.pages_clicker_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_clicker_page_pushbutton.setObjectName("pages_clicker_page_pushbutton")
                self.pages_miner_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_miner_page_pushbutton.clicked.connect(lambda: self.change_page_miner())
                self.pages_miner_page_pushbutton.setGeometry(QtCore.QRect(15, 170, 50, 50))
                self.pages_miner_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/minecraft_pickaxe_green.png);\n"
                "}")
                self.pages_miner_page_pushbutton.setText("")
                self.pages_miner_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_miner_page_pushbutton.setObjectName("pages_miner_page_pushbutton")
                self.pages_premium_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_premium_page_pushbutton.clicked.connect(lambda: self.change_page_premium())
                self.pages_premium_page_pushbutton.setGeometry(QtCore.QRect(15, 240, 50, 50))
                self.pages_premium_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/diamond_green.png);\n"
                "}")
                self.pages_premium_page_pushbutton.setText("")
                self.pages_premium_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_premium_page_pushbutton.setObjectName("pages_premium_page_pushbutton")
                self.pages_uzytkownik_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_uzytkownik_page_pushbutton.setGeometry(QtCore.QRect(20, 440, 40, 40))
                self.pages_uzytkownik_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/male_user_green.png);\n"
                "}")
                self.pages_uzytkownik_page_pushbutton.setText("")
                self.pages_uzytkownik_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_uzytkownik_page_pushbutton.setObjectName("pages_uzytkownik_page_pushbutton")
                self.pages_ustawienia_page_pushbutton = QtWidgets.QPushButton(self.pages_frame)
                self.pages_ustawienia_page_pushbutton.clicked.connect(lambda: self.change_page_ustawienia())
                self.pages_ustawienia_page_pushbutton.setGeometry(QtCore.QRect(20, 510, 40, 40))
                self.pages_ustawienia_page_pushbutton.setStyleSheet("QPushButton {\n"
                "    background-color: none;\n"
                "    image: url(img/settings_green.png);\n"
                "}")
                self.pages_ustawienia_page_pushbutton.setText("")
                self.pages_ustawienia_page_pushbutton.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=40, xOffset=0, yOffset=0, color=QtGui.QColor(0, 0, 0, 200)))
                self.pages_ustawienia_page_pushbutton.setObjectName("pages_ustawienia_page_pushbutton")
                self.pages_przedzial_label = QtWidgets.QLabel(self.pages_frame)
                self.pages_przedzial_label.setGeometry(QtCore.QRect(15, 80, 50, 1))
                self.pages_przedzial_label.setStyleSheet("QLabel {\n"
                "    background-color: rgb(20, 20, 20);\n"
                "}")
                self.pages_przedzial_label.setText("")
                self.pages_przedzial_label.setObjectName("pages_przedzial_label")
                self.pages_przedzial_label_2 = QtWidgets.QLabel(self.pages_frame)
                self.pages_przedzial_label_2.setGeometry(QtCore.QRect(15, 495, 50, 1))
                self.pages_przedzial_label_2.setStyleSheet("QLabel {\n"
                "    background-color: rgb(20, 20, 20);\n"
                "}")
                self.pages_przedzial_label_2.setText("")
                self.pages_przedzial_label_2.setObjectName("pages_przedzial_label_2")
                MainWindow.setCentralWidget(self.centralwidget)

                self.retranslateUi(MainWindow)
                self.stackedWidget.setCurrentIndex(0)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "pvpbooster v2.0"))
                self.main_witaj_nick_label.setText(_translate("MainWindow", f"Witaj, TEST"))
                self.main_online_label.setText(_translate("MainWindow", "Online:"))
                self.main_online_count_label.setText(_translate("MainWindow", "0"))
                self.main_statystyki_label.setText(_translate("MainWindow", "Statystyki"))
                __sortingEnabled = self.main_lista_zmian_listwidget.isSortingEnabled()
                self.main_lista_zmian_listwidget.setSortingEnabled(False)
                item = self.main_lista_zmian_listwidget.item(0)
                item.setText(_translate("MainWindow", "Wprowadzono nowy wygląd GUI"))
                item = self.main_lista_zmian_listwidget.item(1)
                item.setText(_translate("MainWindow", "Optymalizacja kodu"))
                item = self.main_lista_zmian_listwidget.item(2)
                item.setText(_translate("MainWindow", "Dodano config system(20%) + małe\npoprawki"))
                item = self.main_lista_zmian_listwidget.item(3)
                item.setText(_translate("MainWindow", "Wprowadzono możliwość zmiany\nkoloru GUI"))
                self.main_lista_zmian_listwidget.setSortingEnabled(__sortingEnabled)
                self.main_lista_zmian_label.setText(_translate("MainWindow", "Lista zmian:"))
                self.main_plan_label.setText(_translate("MainWindow", f"Plan: FREE"))
                self.main_licencja_label.setText(_translate("MainWindow", f"Licencja: ..."))
                self.main_wersja_label.setText(_translate("MainWindow", "Wersja: 2.0 [BETA]"))
                self.main_statystyki_nick_label.setText(_translate("MainWindow", "Nick"))
                self.main_statystyki_kamien_label.setText(_translate("MainWindow", "Kamień"))
                self.main_statystyki_kratki_label.setText(_translate("MainWindow", "Kratki"))
                self.main_statystyki_pieniadze_label.setText(_translate("MainWindow", "Pieniądze"))
                self.main_statystyki_kille_label.setText(_translate("MainWindow", "Kille"))
                self.main_statystyki_top_label.setText(_translate("MainWindow", "TOP"))
                self.main_statystyki_top_1_label.setText(_translate("MainWindow", "1"))
                self.main_statystyki_top_2_label.setText(_translate("MainWindow", "2"))
                self.main_statystyki_top_3_label.setText(_translate("MainWindow", "3"))
                self.main_statystyki_top_4_label.setText(_translate("MainWindow", "4"))
                self.main_statystyki_top_5_label.setText(_translate("MainWindow", "5"))
                self.main_statystyki_top_6_label.setText(_translate("MainWindow", "6"))
                self.main_statystyki_top_7_label.setText(_translate("MainWindow", "7"))
                self.main_statystyki_nick_1_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_2_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_3_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_4_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_5_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_6_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_nick_7_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_1_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_2_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_3_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_4_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_5_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_6_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kamien_7_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_1_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_2_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_3_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_4_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_5_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_6_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kratki_7_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_1_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_2_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_3_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_4_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_5_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_6_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_pieniadze_7_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_1_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_2_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_3_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_4_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_5_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_6_label.setText(_translate("MainWindow", "blad"))
                self.main_statystyki_kille_7_label.setText(_translate("MainWindow", "blad"))
                self.clicker_status_label.setText(_translate("MainWindow", "Status:"))
                self.clicker_status_current_label.setText(_translate("MainWindow", "OFF"))
                self.clicker_status_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.clicker_status_stop_pushbutton.setText(_translate("MainWindow", "STOP"))
                self.clicker_bindy_label.setText(_translate("MainWindow", "Bindy"))
                self.clicker_bind_clicker_label.setText(_translate("MainWindow", "Clicker:"))
                self.clicker_bind_fakelag_label.setText(_translate("MainWindow", "Fakelag:"))
                self.clicker_bind_komenda_label.setText(_translate("MainWindow", "Komenda:"))
                self.clicker_bind_sniezka_label.setText(_translate("MainWindow", "Śnieżka:"))
                self.clicker_bind_zmiana_seta_label.setText(_translate("MainWindow", "Zmiana seta:"))
                self.clicker_zmiana_seta_label.setText(_translate("MainWindow", "Zmiana seta"))
                self.clicker_zmiana_seta_opis_label.setText(_translate("MainWindow", "Zmiana seta (min. 400x560)       Ustaw pozycje:                                 1-Hełm 2-Klata 3-Nogawki 4-Buty"))
                self.clicker_zmiana_seta_line_label.setText(_translate("MainWindow", "____________________________________________________"))
                
                self.clicker_opcje_label.setText(_translate("MainWindow", "Opcje"))
                self.clicker_opcje_clicker_ms_label.setText(_translate("MainWindow", "Ms:"))
                self.clicker_opcje_clicker_ms_slider_label.setText(_translate("MainWindow", "1"))
                self.clicker_opcje_garda_label.setText(_translate("MainWindow", "Garda:"))
                self.clicker_opcje_garda_status_label.setText(_translate("MainWindow", "OFF"))
                self.clicker_opcje_garda_slider_label.setText(_translate("MainWindow", "1"))
                self.clicker_opcje_fakelag_label.setText(_translate("MainWindow", "Fakelag:"))
                self.clicker_opcje_fakelag_status_label.setText(_translate("MainWindow", "OFF"))
                self.clicker_opcje_fakelag_slider_label.setText(_translate("MainWindow", "1"))
                self.clicker_opcje_zmiana_seta_label.setText(_translate("MainWindow", "Zmiana seta:"))
                self.clicker_opcje_zmiana_seta_status_label.setText(_translate("MainWindow", "OFF"))
                self.clicker_opcje_zmiana_seta_slider_label.setText(_translate("MainWindow", "0"))
                self.clicker_opcje_komenda_label.setText(_translate("MainWindow", "Komenda:"))
                self.clicker_opcje_komenda_status_label.setText(_translate("MainWindow", "OFF"))                
                self.clicker_opcje_sniezka_label.setText(_translate("MainWindow", "Śnieżka:"))
                self.clicker_opcje_sniezka_status_label.setText(_translate("MainWindow", "OFF"))
                self.clicker_opcje_sniezka_slot_miecz_label.setText(_translate("MainWindow", "Miecz:"))
                self.clicker_opcje_sniezka_slot_sniezka_label.setText(_translate("MainWindow", "Śnieżka:"))
                self.clicker_opcje_jitter_label.setText(_translate("MainWindow", "Jitter :"))
                self.clicker_opcje_jitter_status_label.setText(_translate("MainWindow", "OFF"))
                #self.clicker_opcje_podglad_label.setText(_translate("MainWindow", "Podglad [OFF] :"))
                #self.clicker_opcje_podglad_status_label.setText(_translate("MainWindow", "OFF"))
                #self.clicker_opcje_aim_assist_label.setText(_translate("MainWindow", "Aim assist [OFF] :"))
                #self.clicker_opcje_aim_assist_status_label.setText(_translate("MainWindow", "OFF"))
                
                self.miner_status_label.setText(_translate("MainWindow", "Status:"))
                self.miner_status_current_label.setText(_translate("MainWindow", "OFF"))
                self.miner_status_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.miner_status_stop_pushbutton.setText(_translate("MainWindow", "STOP"))
                self.miner_opcje_label.setText(_translate("MainWindow", "Opcje"))
                self.miner_opcje_anty_rodzic_label.setText(_translate("MainWindow", "Anty-rodzic:"))
                self.miner_opcje_anty_rodzic_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_opcje_tnt_logout_label.setText(_translate("MainWindow", "TNT Logout:"))
                self.miner_opcje_tnt_logout_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_opcje_tnt_logout_sciezka_lineedit.setPlaceholderText(_translate("MainWindow", "Ścieżka folderu mc"))
                self.miner_opcje_kopanie_w_tle_label.setText(_translate("MainWindow", "Kopanie w tle:"))
                self.miner_opcje_kopanie_w_tle_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_opcje_kopanie_w_tle_bp_label.setText(_translate("MainWindow", "BP :"))
                self.miner_opcje_kopanie_w_tle_bp_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_opcje_auto_rejoin_label.setText(_translate("MainWindow", "Auto rejoin:"))
                self.miner_opcje_auto_rejoin_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_opcje_kontrola_zdalna_label.setText(_translate("MainWindow", "Kontrola zdalna:"))
                self.miner_opcje_kontrola_zdalna_status_label.setText(_translate("MainWindow", "OFF"))
                self.miner_ustawienia_label.setText(_translate("MainWindow", "Ustawienia"))
                self.miner_ustawienia_dlugosc_stowniarek_label.setText(_translate("MainWindow", "Długość stowniarek: 1"))
                self.miner_ustawienia_szerokosc_stowniarek_label.setText(_translate("MainWindow", "Szerokość stowniarek: 1"))
                self.miner_ustawienia_wpisywanie_komendy_label.setText(_translate("MainWindow", "Wpisywanie komendy: 0.1"))
                self.miner_ustawienia_czas_m_komendami_label.setText(_translate("MainWindow", "Czas m. komendami: 0.1"))
                self.miner_ustawienia_komendy_label.setText(_translate("MainWindow", "Komendy:"))
                self.miner_ustawienia_ilosc_okrazen_label.setText(_translate("MainWindow", "Ilość okrążeń:"))
                self.miner_ustawienia_komenda_label.setText(_translate("MainWindow", "Komenda:"))
                self.miner_ustawienia_komenda_lineedit.setPlaceholderText(_translate("MainWindow", "/repair"))
                self.miner_ustawienia_komendy_dodaj_pushbutton.setText(_translate("MainWindow", "Dodaj"))
                self.miner_ustawienia_komendy_wyczysc_pushbutton.setText(_translate("MainWindow", "Wyczyść"))
                #__sortingEnabled = self.miner_ustawienia_komendy_listwidget.isSortingEnabled()
                #self.miner_ustawienia_komendy_listwidget.setSortingEnabled(False)
                #item = self.miner_ustawienia_komendy_listwidget.item(0)
                #item.setText(_translate("MainWindow", "1"))
                #item = self.miner_ustawienia_komendy_listwidget.item(1)
                #item.setText(_translate("MainWindow", "2"))
                #item = self.miner_ustawienia_komendy_listwidget.item(2)
                #item.setText(_translate("MainWindow", "3"))
                #item = self.miner_ustawienia_komendy_listwidget.item(3)
                #item.setText(_translate("MainWindow", "4"))
                #item = self.miner_ustawienia_komendy_listwidget.item(4)
                #item.setText(_translate("MainWindow", "5"))
                self.miner_wykryte_okna_label.setText(_translate("MainWindow", "Wykryte okna mc:"))
                self.miner_wykryte_okna_count_label.setText(_translate("MainWindow", "5"))
                self.miner_wykryte_okna_przywroc_pushbutton.setText(_translate("MainWindow", "Przywróć"))
                self.miner_wykryte_okna_odswiez_pushbutton.setText(_translate("MainWindow", "Odśwież"))
                self.miner_wykryte_okna_podglad_pushbutton.setText(_translate("MainWindow", "Podgląd"))
                #__sortingEnabled = self.miner_wykryte_okna_listwidget.isSortingEnabled()
                #self.miner_wykryte_okna_listwidget.setSortingEnabled(False)
                #self.miner_wykryte_okna_listwidget.setSortingEnabled(__sortingEnabled)
                self.miner_statystyki_label.setText(_translate("MainWindow", "Statystyki"))
                self.miner_statystyki_czas_kopania_label.setText(_translate("MainWindow", "Czas kopania: 00:00:00"))
                self.miner_statystyki_przebyte_kratki_label.setText(_translate("MainWindow", "Przebyte kratki: 0"))
                self.miner_statystyki_wykopany_kamien_label.setText(_translate("MainWindow", "Wykopany kamień: 0"))
                self.miner_statystyki_zarobione_pieniadze_label.setText(_translate("MainWindow", "Zarobione pieniądze: 0"))
                self.premium_passhunter_label.setText(_translate("MainWindow", "Test1"))
                self.premium_passhunter_threads_label.setText(_translate("MainWindow", "Test1: 1"))
                self.premium_passhunter_adresy_label.setText(_translate("MainWindow", "Test1: 0"))
                self.premium_passhunter_znalezione_label.setText(_translate("MainWindow", "Test1: 0"))
                self.premium_passhunter_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.premium_passhunter_stop_pushbutton.setText(_translate("MainWindow", "STOP"))
                self.premium_passhunter_status_label.setText(_translate("MainWindow", "Status:"))
                self.premium_passhunter_current_status_label.setText(_translate("MainWindow", "OFF"))
                self.premium_passhunter_zaladuj_pushbutton.setText(_translate("MainWindow", "Załaduj"))
                self.premium_dehasher_label.setText(_translate("MainWindow", "Test2"))
                self.premium_dehasher_threads_label.setText(_translate("MainWindow", "Test2: 1"))
                self.premium_dehasher_zaszyfrowane_hasla_label.setText(_translate("MainWindow", "Test2: 0"))
                self.premium_dehasher_znalezione_hasla_label.setText(_translate("MainWindow", "Test2: 0"))
                self.premium_dehasher_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.premium_dehasher_stop_button.setText(_translate("MainWindow", "STOP"))
                self.premium_dehasher_status_label.setText(_translate("MainWindow", "Status:"))
                self.premium_dehasher_current_status_label.setText(_translate("MainWindow", "OFF"))
                self.premium_dehasher_zaladuj_pushbutton.setText(_translate("MainWindow", "Załaduj"))
                self.premium_dork_generator_label.setText(_translate("MainWindow", "Test3"))
                self.premium_dork_generator_count_label.setText(_translate("MainWindow", "Test3: 0"))
                self.premium_dork_generator_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.premium_dork_generator_stop_pushbutton.setText(_translate("MainWindow", "STOP"))
                self.premium_dork_generator_status_label.setText(_translate("MainWindow", "Status:"))
                self.premium_dork_generator_current_status_label.setText(_translate("MainWindow", "OFF"))
                self.premium_keyword_scraper_label.setText(_translate("MainWindow", "Test4"))
                self.premium_keyword_scraper_threads_label.setText(_translate("MainWindow", "Wątki: 1"))
                self.premium_keyword_scraper_bazowe_slowa_label.setText(_translate("MainWindow", "Test4: 0"))
                self.premium_keyword_scraper_znalezione_label.setText(_translate("MainWindow", "Test4: 0"))
                self.premium_keyword_scraper_start_pushbutton.setText(_translate("MainWindow", "START"))
                self.premium_keyword_scraper_stop_pushbutton.setText(_translate("MainWindow", "STOP"))
                self.premium_keyword_scraper_status_label.setText(_translate("MainWindow", "Status:"))
                self.premium_keyword_scraper_current_status_label.setText(_translate("MainWindow", "OFF"))
                self.premium_keyword_scraper_zaladuj_pushbutton.setText(_translate("MainWindow", "Załaduj"))
                self.ustawienia_skin_frame_nick_label.setText(_translate("MainWindow", "srumi"))
                self.ustawienia_config_label.setText(_translate("MainWindow", "Ustawienia"))
                self.ustawienia_config_generator_wczytaj_pushbutton.setText(_translate("MainWindow", "Wczytaj"))
                self.ustawienia_config_usun_pushbutton.setText(_translate("MainWindow", "Usuń"))
                self.ustawienia_config_generator_generuj_pushbutton.setText(_translate("MainWindow", "Generuj"))
                self.ustawienia_config_dodaj_pushbutton.setText(_translate("MainWindow", "Dodaj"))
                self.ustawienia_config_nazwa_lineedit.setPlaceholderText(_translate("MainWindow", "Nazwa"))
                self.ustawienia_config_zapisz_pushbutton.setText(_translate("MainWindow", "Zapisz"))
                self.ustawienia_config_wczytaj_pushbutton.setText(_translate("MainWindow", "Wczytaj"))
                self.ustawienia_config_lista_label.setText(_translate("MainWindow", "Lista:"))
                self.ustawienia_config_generator_label.setText(_translate("MainWindow", "Generator configu:"))
                self.ustawienia_discord_id_label.setText(_translate("MainWindow", "Discord id:"))
                self.ustawienia_discord_id_lineedit.setPlaceholderText(_translate("MainWindow", "Nazwa"))
                self.ustawienia_discord_id_wczytaj_pushbutton.setText(_translate("MainWindow", "Wczytaj"))
                self.ustawienia_discord_id_zapisz_pushbutton.setText(_translate("MainWindow", "Zapisz"))
                self.window_bar_pvp_label.setText(_translate("MainWindow", "pvp"))
                self.window_bar_booster_label.setText(_translate("MainWindow", "booster"))
                self.window_bar_status_label.setText(_translate("MainWindow", "Strona główna"))
                self.window_bar_personal_id_label.setText(_translate("MainWindow", f"({personal_id})"))

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

#if __name__ == "__main__":
#app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
#w = MoveWindow()
#w.show()
#sys.exit(app.exec_())
