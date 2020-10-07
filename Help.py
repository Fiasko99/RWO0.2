from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.setWindowModality(QtCore.Qt.NonModal)
        HelpWindow.setEnabled(True)
        HelpWindow.resize(800, 440)
        HelpWindow.setMinimumSize(QtCore.QSize(800, 440))
        HelpWindow.setMaximumSize(QtCore.QSize(800, 440))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        HelpWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        HelpWindow.setFont(font)
        HelpWindow.setMouseTracking(False)
        HelpWindow.setWindowOpacity(1.0)
        HelpWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        HelpWindow.setAutoFillBackground(False)
        HelpWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        HelpWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        HelpWindow.setAnimated(True)
        HelpWindow.setDocumentMode(False)
        HelpWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    align-text: center;\n"
"    \n"
"    background-color: #F8E6E0;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.project_name = QtWidgets.QLabel(self.centralwidget)
        self.project_name.setStyleSheet("QLabel {\n"
"    color: #8181F7;\n"
"    font: 75 24pt \"Lucida Sans\";\n"
"    background-color: #F6D8CE;\n"
"    border-radius: 10px;\n"
"    margin-right: 20px;\n"
"    margin-left: 20px;\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: white;\n"
"}")
        self.project_name.setAlignment(QtCore.Qt.AlignCenter)
        self.project_name.setObjectName("project_name")
        self.gridLayout.addWidget(self.project_name, 0, 0, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setStyleSheet("QWidget {\n"
"    background-color: #F8E6E0;\n"
"    border-radius: 10px;\n"
"}")
        self.main_widget.setObjectName("main_widget")
        self.main = QtWidgets.QGridLayout(self.main_widget)
        self.main.setObjectName("main")
        self.input_widget = QtWidgets.QFrame(self.main_widget)
        self.input_widget.setStyleSheet("QFrame {\n"
"    background-color: #ECCEF5;\n"
"    padding: 10px;\n"
"    height: 100%;\n"
"}")
        self.input_widget.setObjectName("input_widget")
        self.form_input = QtWidgets.QGridLayout(self.input_widget)
        self.form_input.setObjectName("form_input")
        self.role_label = QtWidgets.QLabel(self.input_widget)
        self.role_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.role_label.setObjectName("role_label")
        self.form_input.addWidget(self.role_label, 1, 0, 1, 1)
        self.role_value = QtWidgets.QComboBox(self.input_widget)
        self.role_value.setStyleSheet("QComboBox {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    background-color: #F5F5DC;\n"
"}")
        self.role_value.setObjectName("role_value")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.form_input.addWidget(self.role_value, 1, 1, 1, 1)
        self.code_label = QtWidgets.QLabel(self.input_widget)
        self.code_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.code_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.code_label.setObjectName("code_label")
        self.form_input.addWidget(self.code_label, 0, 0, 1, 1)
        self.secret_code_value = QtWidgets.QLineEdit(self.input_widget)
        self.secret_code_value.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #F5F5DC;\n"
"}")
        self.secret_code_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret_code_value.setObjectName("secret_code_value")
        self.form_input.addWidget(self.secret_code_value, 0, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 2, 0, 1, 2)
        self.password_label = QtWidgets.QLabel(self.input_widget)
        self.password_label.setStyleSheet("QLabel {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.password_label.setObjectName("password_label")
        self.form_input.addWidget(self.password_label, 3, 0, 1, 2)
        self.main.addWidget(self.input_widget, 0, 0, 1, 1)
        self.button_form = QtWidgets.QFrame(self.main_widget)
        self.button_form.setStyleSheet("QFrame{\n"
"    background-color: #ECCEF5;\n"
"    padding: 5px;\n"
"}")
        self.button_form.setObjectName("button_form")
        self.form_button = QtWidgets.QGridLayout(self.button_form)
        self.form_button.setObjectName("form_button")
        self.back_btn = QtWidgets.QPushButton(self.button_form)
        self.back_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.back_btn.setStyleSheet("QPushButton {\n"
"    background-color: #F6D8CE;\n"
"    font: 75 10pt \"Lucida Sans\";\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid gray;\n"
"}")
        self.back_btn.setObjectName("back_btn")
        self.form_button.addWidget(self.back_btn, 1, 0, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.button_form)
        self.send_btn.setStyleSheet("QPushButton {\n"
"    background-color: #F6D8CE;\n"
"    font: 75 10pt \"Lucida Sans\";\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid gray;\n"
"}")
        self.send_btn.setObjectName("send_btn")
        self.form_button.addWidget(self.send_btn, 0, 0, 1, 1)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 1, 0, 1, 1)
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Восстановление доступа"))
        self.project_name.setText(_translate("HelpWindow", "RWO"))
        self.role_label.setText(_translate("HelpWindow", "Выбрать роль:"))
        self.role_value.setCurrentText(_translate("HelpWindow", "Выбрать"))
        self.role_value.setItemText(0, _translate("HelpWindow", "Выбрать"))
        self.role_value.setItemText(1, _translate("HelpWindow", "Инвестор"))
        self.role_value.setItemText(2, _translate("HelpWindow", "Писатель"))
        self.role_value.setItemText(3, _translate("HelpWindow", "Читатель"))
        self.code_label.setText(_translate("HelpWindow", "Введите код доступа:"))
        self.secret_code_value.setPlaceholderText(_translate("HelpWindow", "введите код доступа"))
        self.login_label.setText(_translate("HelpWindow", "Логин:"))
        self.password_label.setText(_translate("HelpWindow", "Пароль: "))
        self.back_btn.setText(_translate("HelpWindow", "Вернуться"))
        self.send_btn.setText(_translate("HelpWindow", "Вывести данные"))