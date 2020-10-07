from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
import UserAccount
import main
import FullComposition


class FullCompositionWindow(
    QtWidgets.QMainWindow, FullComposition.Ui_FullComposition
):
    def __init__(self, text_composition):
        super().__init__()
        self.setupUi(self)
        self.text_composition = text_composition
        self.text.setStyleSheet(
            "font: 10pt \"Lucida Sans\";"
            "color: #2121F2;"
            "background-color: #F5E4FA;"
            "border-bottom: 2px solid #4169E1;"
        )

    def load_text(self):
        self.text.setText(self.text_composition)
        self.text.setReadOnly(True)


class UserAccountWindow(QtWidgets.QMainWindow, UserAccount.Ui_UserAccount):
    def __init__(self, id_writer):
        super().__init__()
        self.setupUi(self)
        self.id_writer = id_writer

    def load_user_account(self):
        writers = main.SearchDB.get_writers()
        for writer in writers:
            if writer['id'] == self.id_writer:
                self.login_input_label.setText(writer['name_writer'])
                self.date_input_label.setText(str(writer['date_of_born']))
                self.status_input_label.setText(str(writer['work_experience']))


class QLabel_click(QtWidgets.QLabel):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(QLabel_click, self).__init__(parent)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()


class QTextEdit_click(QtWidgets.QTextEdit):
    clicked = pyqtSignal()

    def __init__(self, parent=None):
        super(QTextEdit_click, self).__init__(parent)

    def mouseReleaseEvent(self, event):
        self.clicked.emit()


class Item(QtWidgets.QFrame):

    def __init__(self, name, text,
                 user_connect, id_writer):
        super().__init__()
        self.user_connect = user_connect
        self.id_writer = id_writer
        self.mainLayout = QtWidgets.QHBoxLayout()
        self.left_label = QLabel_click(self)
        self.left_label.setMinimumWidth(200)
        self.left_label.setText(name)
        self.left_label.setWordWrap(True)
        self.left_label.setStyleSheet("QLabel {"
                                      "border: 1px solid blue;"
                                      "border-radius: 20px;"
                                      "font: 10pt \"Lucida Sans\";"
                                      "color: #2121F2;"
                                      "background-color: #ECCEF5;"
                                      "}"
                                      "\n"
                                      "QLabel:hover {"
                                      "border: 3px solid blue;"
                                      "}"
                                      )

        self.left_label.clicked.connect(self.click_label)
        self.right_label = QTextEdit_click(self)
        self.right_label.setStyleSheet(
            "font: 10pt \"Lucida Sans\";"
            "color: #2121F2;"
            "background-color: #F5E4FA;"
            "border-bottom: 2px solid #4169E1;"
        )
        self.right_label.setText(text)
        self.right_label.setReadOnly(True)
        self.right_label.clicked.connect(self.click_text_edit)
        self.mainLayout.addWidget(self.left_label)
        self.mainLayout.addWidget(self.right_label)
        self.setLayout(self.mainLayout)
        self.new_window = -1

    def click_label(self):
        try:
            self.new_window = UserAccountWindow(
                self.id_writer
            )
            self.new_window.load_user_account()
            self.new_window.show()
        except Exception as e:
            print(e)

    def click_text_edit(self):
        self.new_window = FullCompositionWindow(
            self.right_label.toPlainText()
        )
        self.new_window.load_text()
        self.new_window.show()
