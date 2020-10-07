from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UserAccount(object):
    def setupUi(self, UserAccount):
        UserAccount.setObjectName("UserAccount")
        UserAccount.setWindowModality(QtCore.Qt.NonModal)
        UserAccount.setEnabled(True)
        UserAccount.resize(610, 386)
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
        UserAccount.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        UserAccount.setFont(font)
        UserAccount.setMouseTracking(False)
        UserAccount.setWindowOpacity(1.0)
        UserAccount.setLayoutDirection(QtCore.Qt.LeftToRight)
        UserAccount.setAutoFillBackground(False)
        UserAccount.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        UserAccount.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        UserAccount.setAnimated(True)
        UserAccount.setDocumentMode(False)
        UserAccount.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(UserAccount)
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
        self.login_input_label = QtWidgets.QLabel(self.input_widget)
        self.login_input_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.login_input_label.setObjectName("login_input_label")
        self.form_input.addWidget(self.login_input_label, 1, 1, 1, 1)
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
        self.date_input_label = QtWidgets.QLabel(self.input_widget)
        self.date_input_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.date_input_label.setObjectName("date_input_label")
        self.form_input.addWidget(self.date_input_label, 4, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 1, 0, 1, 1)
        self.label_date = QtWidgets.QLabel(self.input_widget)
        self.label_date.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_date.setObjectName("label_date")
        self.form_input.addWidget(self.label_date, 4, 0, 1, 1)
        self.follow_input_label = QtWidgets.QLabel(self.input_widget)
        self.follow_input_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.follow_input_label.setObjectName("follow_input_label")
        self.form_input.addWidget(self.follow_input_label, 5, 1, 1, 1)
        self.label_status = QtWidgets.QLabel(self.input_widget)
        self.label_status.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.label_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_status.setObjectName("label_status")
        self.form_input.addWidget(self.label_status, 2, 0, 1, 1)
        self.status_input_label = QtWidgets.QLabel(self.input_widget)
        self.status_input_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"}")
        self.status_input_label.setObjectName("status_input_label")
        self.form_input.addWidget(self.status_input_label, 2, 1, 1, 1)
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
        self.user_content_btn = QtWidgets.QPushButton(self.button_form)
        self.user_content_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.user_content_btn.setStyleSheet("QPushButton {\n"
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
        self.user_content_btn.setObjectName("user_content_btn")
        self.form_button.addWidget(self.user_content_btn, 1, 0, 1, 1)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        UserAccount.setCentralWidget(self.centralwidget)

        self.retranslateUi(UserAccount)
        QtCore.QMetaObject.connectSlotsByName(UserAccount)

    def retranslateUi(self, UserAccount):
        _translate = QtCore.QCoreApplication.translate
        UserAccount.setWindowTitle(_translate("UserAccount", "Пользовать RWO"))
        self.login_input_label.setText(_translate("UserAccount", "str"))
        self.profile_label.setText(_translate("UserAccount", "Имя пользователя"))
        self.stars_label.setText(_translate("UserAccount", "status_variant"))
        self.date_input_label.setText(_translate("UserAccount", "str"))
        self.login_label.setText(_translate("UserAccount", "Логин:"))
        self.label_date.setText(_translate("UserAccount", "Дата рождения:"))
        self.follow_input_label.setText(_translate("UserAccount", "num"))
        self.label_status.setText(_translate("UserAccount", "Статус:"))
        self.status_input_label.setText(_translate("UserAccount", "str"))
        self.user_content_btn.setText(_translate("UserAccount", "Открыть историю постов"))
