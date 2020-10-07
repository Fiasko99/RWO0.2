from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegistrationWindow(object):
    def setupUi(self, RegistrationWindow):
        RegistrationWindow.setObjectName("RegistrationWindow")
        RegistrationWindow.setWindowModality(QtCore.Qt.NonModal)
        RegistrationWindow.setEnabled(True)
        RegistrationWindow.resize(800, 440)
        RegistrationWindow.setMinimumSize(QtCore.QSize(800, 440))
        RegistrationWindow.setMaximumSize(QtCore.QSize(800, 440))
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
        RegistrationWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        RegistrationWindow.setFont(font)
        RegistrationWindow.setMouseTracking(False)
        RegistrationWindow.setWindowOpacity(1.0)
        RegistrationWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        RegistrationWindow.setAutoFillBackground(False)
        RegistrationWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        RegistrationWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        RegistrationWindow.setAnimated(True)
        RegistrationWindow.setDocumentMode(False)
        RegistrationWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(RegistrationWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setStyleSheet("QWidget{\n"
"    align-text: center;\n"
"    \n"
"    background-color: #F8E6E0;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setStyleSheet("QWidget {\n"
"    background-color: #F8E6E0;\n"
"    border-radius: 10px;\n"
"}")
        self.main_widget.setObjectName("main_widget")
        self.main = QtWidgets.QGridLayout(self.main_widget)
        self.main.setObjectName("main")
        self.button_form = QtWidgets.QFrame(self.main_widget)
        self.button_form.setStyleSheet("QFrame{\n"
"    background-color: #ECCEF5;\n"
"    padding: 5px;\n"
"}")
        self.button_form.setObjectName("button_form")
        self.form_button = QtWidgets.QGridLayout(self.button_form)
        self.form_button.setObjectName("form_button")
        self.registration_btn = QtWidgets.QPushButton(self.button_form)
        self.registration_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.registration_btn.setStyleSheet("QPushButton {\n"
"    background-color: #F6D8CE;\n"
"    font: 75 10pt \"Lucida Sans\";\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border: 2px solid gray;\n"
"}\n"
"")
        self.registration_btn.setObjectName("registration_btn")
        self.form_button.addWidget(self.registration_btn, 0, 1, 1, 1)
        self.back_btn = QtWidgets.QPushButton(self.button_form)
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
"}\n"
"")
        self.back_btn.setObjectName("back_btn")
        self.form_button.addWidget(self.back_btn, 0, 0, 1, 1)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.input_widget = QtWidgets.QFrame(self.main_widget)
        self.input_widget.setStyleSheet("QFrame {\n"
"    background-color: #ECCEF5;\n"
"    padding: 10px;\n"
"    height: 100%;\n"
"}")
        self.input_widget.setObjectName("input_widget")
        self.form_input = QtWidgets.QGridLayout(self.input_widget)
        self.form_input.setObjectName("form_input")
        self.password_label = QtWidgets.QLabel(self.input_widget)
        self.password_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.password_label.setAlignment(QtCore.Qt.AlignCenter)
        self.password_label.setObjectName("password_label")
        self.form_input.addWidget(self.password_label, 2, 0, 1, 1)
        self.secret_code_label = QtWidgets.QLabel(self.input_widget)
        self.secret_code_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.secret_code_label.setAlignment(QtCore.Qt.AlignCenter)
        self.secret_code_label.setObjectName("secret_code_label")
        self.form_input.addWidget(self.secret_code_label, 4, 0, 1, 1)
        self.role_value = QtWidgets.QComboBox(self.input_widget)
        self.role_value.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.role_value.setStyleSheet("QComboBox {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: blue;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    background-color: #F5F5DC;\n"
"}")
        self.role_value.setObjectName("role_value")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.form_input.addWidget(self.role_value, 0, 2, 1, 1)
        self.secret_code_value = QtWidgets.QLineEdit(self.input_widget)
        self.secret_code_value.setStyleSheet("QLineEdit {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: blue;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #F5F5DC;\n"
"}")
        self.secret_code_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret_code_value.setObjectName("secret_code_value")
        self.form_input.addWidget(self.secret_code_value, 4, 2, 1, 1)
        self.name_label = QtWidgets.QLabel(self.input_widget)
        self.name_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.form_input.addWidget(self.name_label, 3, 0, 1, 1)
        self.name_value = QtWidgets.QLineEdit(self.input_widget)
        self.name_value.setStyleSheet("QLineEdit {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: blue;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #F5F5DC;\n"
"}")
        self.name_value.setObjectName("name_value")
        self.form_input.addWidget(self.name_value, 3, 2, 1, 1)
        self.agree_label = QtWidgets.QLabel(self.input_widget)
        self.agree_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: red;\n"
"}")
        self.agree_label.setAlignment(QtCore.Qt.AlignCenter)
        self.agree_label.setObjectName("agree_label")
        self.form_input.addWidget(self.agree_label, 5, 0, 1, 1)
        self.login_value = QtWidgets.QLineEdit(self.input_widget)
        self.login_value.setStyleSheet("QLineEdit {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: blue;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #F5F5DC;\n"
"}")
        self.login_value.setObjectName("login_value")
        self.form_input.addWidget(self.login_value, 1, 2, 1, 1)
        self.role_label = QtWidgets.QLabel(self.input_widget)
        self.role_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.role_label.setAlignment(QtCore.Qt.AlignCenter)
        self.role_label.setObjectName("role_label")
        self.form_input.addWidget(self.role_label, 0, 0, 1, 1)
        self.password_value = QtWidgets.QLineEdit(self.input_widget)
        self.password_value.setStyleSheet("QLineEdit {\n"
"    font: 63 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: blue;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    background-color: #F5F5DC;\n"
"}")
        self.password_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_value.setObjectName("password_value")
        self.form_input.addWidget(self.password_value, 2, 2, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setCursor(QtGui.QCursor(QtCore.Qt.SizeVerCursor))
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignCenter)
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 1, 0, 1, 1)
        self.agree_checkbox = QtWidgets.QCheckBox(self.input_widget)
        self.agree_checkbox.setMinimumSize(QtCore.QSize(400, 0))
        self.agree_checkbox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.agree_checkbox.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"    background-color: red;\n"
"    margin-left: 50px;\n"
"    padding: 5px;\n"
"}")
        self.agree_checkbox.setObjectName("agree_checkbox")
        self.form_input.addWidget(self.agree_checkbox, 5, 1, 1, 2)
        self.main.addWidget(self.input_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 1, 0, 1, 1)
        self.project_name = QtWidgets.QLabel(self.centralwidget)
        self.project_name.setStyleSheet("QLabel {\n"
"    color: #8181F7;\n"
"    font: 75 24pt \"Lucida Sans\";\n"
"}\n"
"\n"
"QLabel:hover {\n"
"    color: white;\n"
"}")
        self.project_name.setAlignment(QtCore.Qt.AlignCenter)
        self.project_name.setObjectName("project_name")
        self.gridLayout.addWidget(self.project_name, 0, 0, 1, 1)
        RegistrationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RegistrationWindow)
        QtCore.QMetaObject.connectSlotsByName(RegistrationWindow)

    def retranslateUi(self, RegistrationWindow):
        _translate = QtCore.QCoreApplication.translate
        RegistrationWindow.setWindowTitle(_translate("RegistrationWindow", "Регистрация"))
        self.registration_btn.setText(_translate("RegistrationWindow", "Регистрация"))
        self.back_btn.setText(_translate("RegistrationWindow", "Вернуться"))
        self.password_label.setText(_translate("RegistrationWindow", "Пароль:"))
        self.secret_code_label.setText(_translate("RegistrationWindow", "Секретный код:"))
        self.role_value.setCurrentText(_translate("RegistrationWindow", "Выбрать"))
        self.role_value.setItemText(0, _translate("RegistrationWindow", "Выбрать"))
        self.role_value.setItemText(1, _translate("RegistrationWindow", "Инвестор"))
        self.role_value.setItemText(2, _translate("RegistrationWindow", "Писатель"))
        self.role_value.setItemText(3, _translate("RegistrationWindow", "Читатель"))
        self.secret_code_value.setPlaceholderText(_translate("RegistrationWindow", "min 8 symbol"))
        self.name_label.setText(_translate("RegistrationWindow", "Имя:"))
        self.name_value.setPlaceholderText(_translate("RegistrationWindow", "min 3 symbol"))
        self.agree_label.setText(_translate("RegistrationWindow", "Вы совершеннолетний?"))
        self.login_value.setPlaceholderText(_translate("RegistrationWindow", "min 6 symbol"))
        self.role_label.setText(_translate("RegistrationWindow", "Статус:"))
        self.password_value.setPlaceholderText(_translate("RegistrationWindow", "min 8 symbol"))
        self.login_label.setText(_translate("RegistrationWindow", "Логин:"))
        self.agree_checkbox.setText(_translate("RegistrationWindow", "Я совершеннолетний"))
        self.project_name.setText(_translate("RegistrationWindow", "RWO"))

