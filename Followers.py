# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apps/Followers.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ContentWindow(object):
    def setupUi(self, ContentWindow):
        ContentWindow.setObjectName("ContentWindow")
        ContentWindow.setWindowModality(QtCore.Qt.NonModal)
        ContentWindow.setEnabled(True)
        ContentWindow.resize(900, 500)
        ContentWindow.setMinimumSize(QtCore.QSize(900, 500))
        ContentWindow.setMaximumSize(QtCore.QSize(900, 500))
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
        ContentWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        ContentWindow.setFont(font)
        ContentWindow.setMouseTracking(False)
        ContentWindow.setWindowOpacity(1.0)
        ContentWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        ContentWindow.setAutoFillBackground(False)
        ContentWindow.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        ContentWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        ContentWindow.setAnimated(True)
        ContentWindow.setDocumentMode(False)
        ContentWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(ContentWindow)
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
        self.button_form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_form.setStyleSheet("QFrame{\n"
"    background-color: #ECCEF5;\n"
"    padding: 5px;\n"
"}")
        self.button_form.setObjectName("button_form")
        self.form_button = QtWidgets.QGridLayout(self.button_form)
        self.form_button.setObjectName("form_button")
        self.content_btn = QtWidgets.QPushButton(self.button_form)
        self.content_btn.setMinimumSize(QtCore.QSize(120, 0))
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
        self.content_btn.setAutoDefault(False)
        self.content_btn.setFlat(False)
        self.content_btn.setObjectName("content_btn")
        self.form_button.addWidget(self.content_btn, 0, 0, 1, 1)
        self.main.addWidget(self.button_form, 0, 0, 1, 1)
        self.followers_space = QtWidgets.QScrollArea(self.main_widget)
        self.followers_space.setWidgetResizable(True)
        self.followers_space.setObjectName("followers_space")
        self.followers_space_widget = QtWidgets.QWidget()
        self.followers_space_widget.setGeometry(QtCore.QRect(0, 0, 710, 464))
        self.followers_space_widget.setObjectName("followers_space_widget")
        self.followers_space.setWidget(self.followers_space_widget)
        self.main.addWidget(self.followers_space, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        ContentWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ContentWindow)
        QtCore.QMetaObject.connectSlotsByName(ContentWindow)

    def retranslateUi(self, ContentWindow):
        _translate = QtCore.QCoreApplication.translate
        ContentWindow.setWindowTitle(_translate("ContentWindow", "Подписчики"))
        self.content_btn.setText(_translate("ContentWindow", "Вернуться"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ContentWindow = QtWidgets.QMainWindow()
    ui = Ui_ContentWindow()
    ui.setupUi(ContentWindow)
    ContentWindow.show()
    sys.exit(app.exec_())
