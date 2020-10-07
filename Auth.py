# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apps/Auth.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthWindow(object):
    def setupUi(self, AuthWindow):
        AuthWindow.setObjectName("AuthWindow")
        AuthWindow.setWindowModality(QtCore.Qt.NonModal)
        AuthWindow.setEnabled(True)
        AuthWindow.resize(690, 320)
        AuthWindow.setMinimumSize(QtCore.QSize(690, 320))
        AuthWindow.setMaximumSize(QtCore.QSize(690, 320))
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
        AuthWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        AuthWindow.setFont(font)
        AuthWindow.setMouseTracking(False)
        AuthWindow.setWindowOpacity(1.0)
        AuthWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        AuthWindow.setAutoFillBackground(False)
        AuthWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        AuthWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        AuthWindow.setAnimated(True)
        AuthWindow.setDocumentMode(False)
        AuthWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(AuthWindow)
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
"    border-radius: 5px;\n"
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
"    background-color: #F8E6E0;\n"
"}")
        self.login_value.setObjectName("login_value")
        self.form_input.addWidget(self.login_value, 0, 1, 1, 1)
        self.login_label = QtWidgets.QLabel(self.input_widget)
        self.login_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.login_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.login_label.setObjectName("login_label")
        self.form_input.addWidget(self.login_label, 0, 0, 1, 1)
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
"    background-color: #F8E6E0;\n"
"}")
        self.password_value.setText("")
        self.password_value.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_value.setDragEnabled(False)
        self.password_value.setReadOnly(False)
        self.password_value.setObjectName("password_value")
        self.form_input.addWidget(self.password_value, 1, 1, 1, 1)
        self.password_label = QtWidgets.QLabel(self.input_widget)
        self.password_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.password_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.password_label.setObjectName("password_label")
        self.form_input.addWidget(self.password_label, 1, 0, 1, 1)
        self.role_value = QtWidgets.QComboBox(self.input_widget)
        self.role_value.setStyleSheet("QComboBox {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    background-color: white;\n"
"    color: black;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"    height: 16px;\n"
"}\n"
"\n"
"QComboBox:hover{\n"
"    background-color: #F8E6E0;\n"
"}")
        self.role_value.setObjectName("role_value")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.role_value.addItem("")
        self.form_input.addWidget(self.role_value, 2, 1, 1, 1)
        self.role_label = QtWidgets.QLabel(self.input_widget)
        self.role_label.setStyleSheet("QLabel {\n"
"    font: 10pt \"Lucida Sans\";\n"
"    color: #8181F7;\n"
"}")
        self.role_label.setObjectName("role_label")
        self.form_input.addWidget(self.role_label, 2, 0, 1, 1)
        self.main.addWidget(self.input_widget, 0, 0, 1, 1)
        self.button_form = QtWidgets.QFrame(self.main_widget)
        self.button_form.setStyleSheet("QFrame{\n"
"    background-color: #ECCEF5;\n"
"    padding: 5px;\n"
"}")
        self.button_form.setObjectName("button_form")
        self.form_button = QtWidgets.QGridLayout(self.button_form)
        self.form_button.setObjectName("form_button")
        self.login_btn = QtWidgets.QPushButton(self.button_form)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_btn.setStyleSheet("QPushButton {\n"
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
        self.login_btn.setObjectName("login_btn")
        self.form_button.addWidget(self.login_btn, 0, 1, 1, 1)
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
        self.form_button.addWidget(self.registration_btn, 0, 0, 1, 1)
        self.help_btn = QtWidgets.QPushButton(self.button_form)
        self.help_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help_btn.setStyleSheet("QPushButton {\n"
"    font: 75 10pt \"Lucida Sans\";\n"
"    color: #2121F2;\n"
"    background-color: #ECCEF5;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #F6D8CE;\n"
"    border: 1px solid gray;\n"
"    border-radius: 4px;\n"
"}")
        self.help_btn.setObjectName("help_btn")
        self.form_button.addWidget(self.help_btn, 0, 2, 1, 1)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 1, 0, 1, 1)
        AuthWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AuthWindow)
        QtCore.QMetaObject.connectSlotsByName(AuthWindow)

    def retranslateUi(self, AuthWindow):
        _translate = QtCore.QCoreApplication.translate
        AuthWindow.setWindowTitle(_translate("AuthWindow", "Авторизация"))
        self.project_name.setText(_translate("AuthWindow", "RWO"))
        self.login_value.setPlaceholderText(_translate("AuthWindow", "min 6 symbol"))
        self.login_label.setText(_translate("AuthWindow", "Логин:"))
        self.password_value.setPlaceholderText(_translate("AuthWindow", "min 8 symbol"))
        self.password_label.setText(_translate("AuthWindow", "Пароль:"))
        self.role_value.setCurrentText(_translate("AuthWindow", "Выбрать"))
        self.role_value.setItemText(0, _translate("AuthWindow", "Выбрать"))
        self.role_value.setItemText(1, _translate("AuthWindow", "Инвестор"))
        self.role_value.setItemText(2, _translate("AuthWindow", "Писатель"))
        self.role_value.setItemText(3, _translate("AuthWindow", "Читатель"))
        self.role_label.setText(_translate("AuthWindow", "Выберите роль:"))
        self.login_btn.setText(_translate("AuthWindow", "Войти"))
        self.registration_btn.setText(_translate("AuthWindow", "Регистрация"))
        self.help_btn.setText(_translate("AuthWindow", "Забыли данные?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthWindow = QtWidgets.QMainWindow()
    ui = Ui_AuthWindow()
    ui.setupUi(AuthWindow)
    AuthWindow.show()
    sys.exit(app.exec_())
