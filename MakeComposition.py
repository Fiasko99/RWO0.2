from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MakeComposition(object):
    def setupUi(self, MakeComposition):
        MakeComposition.setObjectName("MakeComposition")
        MakeComposition.setWindowModality(QtCore.Qt.NonModal)
        MakeComposition.setEnabled(True)
        MakeComposition.resize(774, 758)
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
        MakeComposition.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Lucida Sans")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        MakeComposition.setFont(font)
        MakeComposition.setMouseTracking(False)
        MakeComposition.setWindowOpacity(1.0)
        MakeComposition.setLayoutDirection(QtCore.Qt.LeftToRight)
        MakeComposition.setAutoFillBackground(False)
        MakeComposition.setStyleSheet("background-color: white;\n"
"font: 10pt \"Lucida Sans\";")
        MakeComposition.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MakeComposition.setAnimated(True)
        MakeComposition.setDocumentMode(False)
        MakeComposition.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MakeComposition)
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
        self.main_genre_value = QtWidgets.QLineEdit(self.input_widget)
        self.main_genre_value.setStyleSheet("QLineEdit {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 4px;\n"
"}\n"
"")
        self.main_genre_value.setAlignment(QtCore.Qt.AlignCenter)
        self.main_genre_value.setObjectName("main_genre_value")
        self.form_input.addWidget(self.main_genre_value, 3, 1, 1, 1)
        self.text_composition_label = QtWidgets.QLabel(self.input_widget)
        self.text_composition_label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: #F6D8CE;\n"
"}")
        self.text_composition_label.setAlignment(QtCore.Qt.AlignCenter)
        self.text_composition_label.setObjectName("text_composition_label")
        self.form_input.addWidget(self.text_composition_label, 4, 0, 1, 2)
        self.name_label = QtWidgets.QLabel(self.input_widget)
        self.name_label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: #F6D8CE;\n"
"}")
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.form_input.addWidget(self.name_label, 0, 0, 1, 2)
        self.age_limit_label = QtWidgets.QLabel(self.input_widget)
        self.age_limit_label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: #F6D8CE;\n"
"}")
        self.age_limit_label.setAlignment(QtCore.Qt.AlignCenter)
        self.age_limit_label.setObjectName("age_limit_label")
        self.form_input.addWidget(self.age_limit_label, 2, 0, 1, 1)
        self.age_limit_box = QtWidgets.QComboBox(self.input_widget)
        self.age_limit_box.setStyleSheet("QComboBox {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 4px;\n"
"}\n"
"\n"
"")
        self.age_limit_box.setObjectName("age_limit_box")
        self.form_input.addWidget(self.age_limit_box, 3, 0, 1, 1)
        self.text_composition_value = QtWidgets.QTextEdit(self.input_widget)
        self.text_composition_value.setStyleSheet("QTextEdit {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.text_composition_value.setObjectName("text_composition_value")
        self.form_input.addWidget(self.text_composition_value, 5, 0, 1, 2)
        self.genre_label = QtWidgets.QLabel(self.input_widget)
        self.genre_label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    background-color: #F6D8CE;\n"
"}")
        self.genre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.genre_label.setObjectName("genre_label")
        self.form_input.addWidget(self.genre_label, 2, 1, 1, 1)
        self.name_value = QtWidgets.QLineEdit(self.input_widget)
        self.name_value.setStyleSheet("QLineEdit {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"    border: 1px solid gray;\n"
"    border-radius: 8px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding: 8px;\n"
"}\n"
"")
        self.name_value.setAlignment(QtCore.Qt.AlignCenter)
        self.name_value.setObjectName("name_value")
        self.form_input.addWidget(self.name_value, 1, 0, 1, 2)
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
"}\n"
"")
        self.back_btn.setObjectName("back_btn")
        self.form_button.addWidget(self.back_btn, 1, 0, 1, 1)
        self.send_btn = QtWidgets.QPushButton(self.button_form)
        self.send_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.form_button.addWidget(self.send_btn, 1, 1, 1, 1)
        self.information_label = QtWidgets.QLabel(self.button_form)
        self.information_label.setStyleSheet("QLabel {\n"
"    font: 75 10pt Lucida Sans;\n"
"    color: #2121F2;\n"
"}")
        self.information_label.setAlignment(QtCore.Qt.AlignCenter)
        self.information_label.setObjectName("information_label")
        self.form_button.addWidget(self.information_label, 0, 0, 1, 2)
        self.main.addWidget(self.button_form, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.main_widget, 0, 0, 1, 1)
        MakeComposition.setCentralWidget(self.centralwidget)

        self.retranslateUi(MakeComposition)
        QtCore.QMetaObject.connectSlotsByName(MakeComposition)

    def retranslateUi(self, MakeComposition):
        _translate = QtCore.QCoreApplication.translate
        MakeComposition.setWindowTitle(_translate("MakeComposition", "Оформление поста"))
        self.text_composition_label.setText(_translate("MakeComposition", "Текст произведения:"))
        self.name_label.setText(_translate("MakeComposition", "Название произведения"))
        self.age_limit_label.setText(_translate("MakeComposition", "Ограничение возраста:"))
        self.genre_label.setText(_translate("MakeComposition", "Жанр:"))
        self.back_btn.setText(_translate("MakeComposition", "Вернуться"))
        self.send_btn.setText(_translate("MakeComposition", "Отправить"))
        self.information_label.setText(_translate("MakeComposition", "Автосохранение работает."))
