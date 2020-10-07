# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'apps/FullComposition.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FullComposition(object):
    def setupUi(self, FullComposition):
        FullComposition.setObjectName("FullComposition")
        FullComposition.resize(969, 756)
        self.centralwidget = QtWidgets.QWidget(FullComposition)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setObjectName("text")
        self.gridLayout.addWidget(self.text, 0, 0, 1, 1)
        FullComposition.setCentralWidget(self.centralwidget)

        self.retranslateUi(FullComposition)
        QtCore.QMetaObject.connectSlotsByName(FullComposition)

    def retranslateUi(self, FullComposition):
        _translate = QtCore.QCoreApplication.translate
        FullComposition.setWindowTitle(_translate("FullComposition", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FullComposition = QtWidgets.QMainWindow()
    ui = Ui_FullComposition()
    ui.setupUi(FullComposition)
    FullComposition.show()
    sys.exit(app.exec_())
