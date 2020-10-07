from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditProfileWindow(object):
    def setupUi(self, EditProfileWindow):
        EditProfileWindow.setObjectName("EditProfileWindow")
        EditProfileWindow.setWindowModality(QtCore.Qt.NonModal)
        EditProfileWindow.setEnabled(True)
        EditProfileWindow.resize(808, 374)
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
        EditProfileWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        EditProfileWindow.setFont(font)
        EditProfileWindow.setMouseTracking(False)
        EditProfileWindow.setWindowOpacity(1.0)
        EditProfileWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        EditProfileWindow.setAutoFillBackground(False)
        EditProfileWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        EditProfileWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        EditProfileWindow.setAnimated(True)
        EditProfileWindow.setDocumentMode(False)
        EditProfileWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(EditProfileWindow)
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
        self.edit_btn = QtWidgets.QPushButton(self.button_form)
        self.edit_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_btn.setStyleSheet("QPushButton {\n"
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
        self.edit_btn.setObjectName("edit_btn")
        self.form_button.addWidget(self.edit_btn, 0, 1, 1, 1)
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
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.form_input.addWidget(self.password_label, 2, 0, 1, 1)
        self.date_value = QtWidgets.QDateEdit(self.input_widget)
        self.date_value.setStyleSheet("QDateEdit{\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QDateEdit:hover:hover {\n"
"    background-color: #F6D8CE;\n"
"}")
        self.date_value.setCalendarPopup(False)
        self.date_value.setDate(QtCore.QDate(2020, 6, 15))
        self.date_value.setObjectName("date_value")
        self.form_input.addWidget(self.date_value, 4, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self.input_widget)
        self.label_name.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.form_input.addWidget(self.label_name, 3, 0, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 1, 0, 1, 1)
        self.name_value = QtWidgets.QLineEdit(self.input_widget)
        self.name_value.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #F6D8CE;\n"
"}")
        self.name_value.setObjectName("name_value")
        self.form_input.addWidget(self.name_value, 3, 1, 1, 1)
        self.code_label_2 = QtWidgets.QLabel(self.input_widget)
        self.code_label_2.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.code_label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.code_label_2.setObjectName("code_label_2")
        self.form_input.addWidget(self.code_label_2, 5, 0, 1, 1)
        self.password_value = QtWidgets.QLineEdit(self.input_widget)
        self.password_value.setTabletTracking(False)
        self.password_value.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.password_value.setAutoFillBackground(False)
        self.password_value.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #F6D8CE;\n"
"}")
        self.password_value.setText("")
        self.password_value.setMaxLength(12)
        self.password_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_value.setDragEnabled(False)
        self.password_value.setReadOnly(False)
        self.password_value.setObjectName("password_value")
        self.form_input.addWidget(self.password_value, 2, 1, 1, 1)
        self.label_date = QtWidgets.QLabel(self.input_widget)
        self.label_date.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName("label_date")
        self.form_input.addWidget(self.label_date, 4, 0, 1, 1)
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
"    background-color: #F6D8CE;\n"
"}")
        self.secret_code_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secret_code_value.setObjectName("secret_code_value")
        self.form_input.addWidget(self.secret_code_value, 5, 1, 1, 1)
        self.login_value = QtWidgets.QLineEdit(self.input_widget)
        self.login_value.setStyleSheet("QLineEdit{\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"    background-color: #F6D8CE;\n"
"}")
        self.login_value.setMaxLength(12)
        self.login_value.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.login_value.setObjectName("login_value")
        self.form_input.addWidget(self.login_value, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.input_widget)
        self.label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 10px;\n"
"    background-color: #F6D8CE;\n"
"}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.form_input.addWidget(self.label, 0, 0, 1, 2)
        self.main.addWidget(self.input_widget, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        EditProfileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(EditProfileWindow)

    def retranslateUi(self, EditProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        EditProfileWindow.setWindowTitle(_translate("EditProfileWindow", "Изменение данных"))
        self.edit_btn.setText(_translate("EditProfileWindow", "Изменить"))
        self.back_btn.setText(_translate("EditProfileWindow", "Вернуться"))
        self.password_label.setText(_translate("EditProfileWindow", "Пароль:"))
        self.label_name.setText(_translate("EditProfileWindow", "Имя:"))
        self.login_label.setText(_translate("EditProfileWindow", "Логин:"))
        self.name_value.setPlaceholderText(_translate("EditProfileWindow", "min 3 symbol"))
        self.code_label_2.setText(_translate("EditProfileWindow", "Код доступа:"))
        self.password_value.setPlaceholderText(_translate("EditProfileWindow", "min 8 symbol"))
        self.label_date.setText(_translate("EditProfileWindow", "Дата рождения:"))
        self.secret_code_value.setPlaceholderText(_translate("EditProfileWindow", "Подтвердите своё намерение"))
        self.login_value.setPlaceholderText(_translate("EditProfileWindow", "min 6 symbol"))
        self.label.setText(_translate("EditProfileWindow", "Для изменения заполните поля, которые хотите изменить"))
