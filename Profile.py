from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileWindow(object):
    def setupUi(self, ProfileWindow):
        ProfileWindow.setObjectName("ProfileWindow")
        ProfileWindow.setWindowModality(QtCore.Qt.NonModal)
        ProfileWindow.setEnabled(True)
        ProfileWindow.resize(760, 448)
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
        ProfileWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        ProfileWindow.setFont(font)
        ProfileWindow.setMouseTracking(False)
        ProfileWindow.setWindowOpacity(1.0)
        ProfileWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        ProfileWindow.setAutoFillBackground(False)
        ProfileWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        ProfileWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        ProfileWindow.setAnimated(True)
        ProfileWindow.setDocumentMode(False)
        ProfileWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ProfileWindow)
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
        self.input_widget = QtWidgets.QFrame(self.main_widget)
        self.input_widget.setStyleSheet("QFrame {\n"
"    background-color: #ECCEF5;\n"
"    padding: 10px;\n"
"    height: 100%;\n"
"}")
        self.input_widget.setObjectName("input_widget")
        self.form_input = QtWidgets.QGridLayout(self.input_widget)
        self.form_input.setObjectName("form_input")
        self.profile_label = QtWidgets.QLabel(self.input_widget)
        self.profile_label.setStyleSheet("QLabel {\n"
"    font: 63 18pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.profile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_label.setObjectName("profile_label")
        self.form_input.addWidget(self.profile_label, 0, 0, 1, 2)
        self.stars_label = QtWidgets.QLabel(self.input_widget)
        self.stars_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.stars_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.stars_label.setObjectName("stars_label")
        self.form_input.addWidget(self.stars_label, 5, 0, 1, 1)
        self.name_value_label = QtWidgets.QLabel(self.input_widget)
        self.name_value_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.name_value_label.setObjectName("name_value_label")
        self.form_input.addWidget(self.name_value_label, 3, 1, 1, 1)
        self.login_value_label = QtWidgets.QLabel(self.input_widget)
        self.login_value_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.login_value_label.setObjectName("login_value_label")
        self.form_input.addWidget(self.login_value_label, 1, 1, 1, 1)
        self.edit_data_btn = QtWidgets.QPushButton(self.input_widget)
        self.edit_data_btn.setStyleSheet("QPushButton {\n"
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
        self.edit_data_btn.setObjectName("edit_data_btn")
        self.form_input.addWidget(self.edit_data_btn, 6, 0, 1, 2)
        self.date_value_label = QtWidgets.QLabel(self.input_widget)
        self.date_value_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.date_value_label.setObjectName("date_value_label")
        self.form_input.addWidget(self.date_value_label, 4, 1, 1, 1)
        self.role_value_label = QtWidgets.QLabel(self.input_widget)
        self.role_value_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.role_value_label.setObjectName("role_value_label")
        self.form_input.addWidget(self.role_value_label, 5, 1, 1, 1)
        self.label_name = QtWidgets.QLabel(self.input_widget)
        self.label_name.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_name.setObjectName("label_name")
        self.form_input.addWidget(self.label_name, 3, 0, 1, 1)
        self.label_date = QtWidgets.QLabel(self.input_widget)
        self.label_date.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName("label_date")
        self.form_input.addWidget(self.label_date, 4, 0, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 1, 0, 1, 1)
        self.additional_btn = QtWidgets.QPushButton(self.input_widget)
        self.additional_btn.setStyleSheet("QPushButton {\n"
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
        self.additional_btn.setObjectName("additional_btn")
        self.form_input.addWidget(self.additional_btn, 7, 0, 1, 2)
        self.main.addWidget(self.input_widget, 0, 0, 1, 1)
        self.button_form = QtWidgets.QFrame(self.main_widget)
        self.button_form.setStyleSheet("QFrame{\n"
"    background-color: #ECCEF5;\n"
"    padding: 5px;\n"
"}")
        self.button_form.setLineWidth(1)
        self.button_form.setObjectName("button_form")
        self.form_button = QtWidgets.QGridLayout(self.button_form)
        self.form_button.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.form_button.setContentsMargins(9, -1, -1, -1)
        self.form_button.setVerticalSpacing(6)
        self.form_button.setObjectName("form_button")
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
"}")
        self.back_btn.setObjectName("back_btn")
        self.form_button.addWidget(self.back_btn, 2, 1, 1, 1)
        self.content_btn = QtWidgets.QPushButton(self.button_form)
        self.content_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.content_btn.setStyleSheet("QPushButton {\n"
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
        self.content_btn.setObjectName("content_btn")
        self.form_button.addWidget(self.content_btn, 0, 1, 1, 3)
        self.history_auth_btn = QtWidgets.QPushButton(self.button_form)
        self.history_auth_btn.setStyleSheet("QPushButton {\n"
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
        self.history_auth_btn.setObjectName("history_auth_btn")
        self.form_button.addWidget(self.history_auth_btn, 2, 2, 1, 2)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        ProfileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(ProfileWindow)

    def retranslateUi(self, ProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        ProfileWindow.setWindowTitle(_translate("ProfileWindow", "Профиль"))
        self.profile_label.setText(_translate("ProfileWindow", "Ваш профиль"))
        self.stars_label.setText(_translate("ProfileWindow", "Роль:"))
        self.name_value_label.setText(_translate("ProfileWindow", "str"))
        self.login_value_label.setText(_translate("ProfileWindow", "str"))
        self.edit_data_btn.setText(_translate("ProfileWindow", "Изменить свои данные"))
        self.date_value_label.setText(_translate("ProfileWindow", "date"))
        self.role_value_label.setText(_translate("ProfileWindow", "str"))
        self.label_name.setText(_translate("ProfileWindow", "Имя:"))
        self.label_date.setText(_translate("ProfileWindow", "Дата рождения:"))
        self.login_label.setText(_translate("ProfileWindow", "Логин:"))
        self.additional_btn.setText(_translate("ProfileWindow", "role_variant"))
        self.back_btn.setText(_translate("ProfileWindow", "Выйти из профиля"))
        self.content_btn.setText(_translate("ProfileWindow", "К основному контенту"))
        self.history_auth_btn.setText(_translate("ProfileWindow", "История авторизации"))
