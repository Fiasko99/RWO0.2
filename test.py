# # -*- coding: utf-8 -*-
# # ----------------------------------------------------------------------------
# # Nombre:       QLabel_clickable.py
# # Autor:        Miguel Andres Garcia Niño
# # Creado:       11 de Abril 2018
# # Modificado:   11 de Abril 2018
# # Copyright:    (c) 2018 by Miguel Andres Garcia Niño, 2018
# # License:      Apache License 2.0
# # ----------------------------------------------------------------------------
#
# __versión__ = "1.0"
#
# """
# El módulo *QLabel_clickable* permite llamar a una función al hacer clic o doble clic sobre
# un QLabel
# """
#
# from PyQt5.QtGui import QIcon, QPixmap
# from PyQt5.QtCore import Qt, pyqtSignal
# from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QMessageBox
#
#
# # ===================== CLASE QLabelClickable ======================
#
# class QLabel_click(QLabel):
#     clicked = pyqtSignal()
#
#     def __init__(self, parent=None):
#         super(QLabel_click, self).__init__(parent)
#
#     def mouseReleaseEvent(self, event):
#         self.clicked.emit()
#
#
# # ===================== CLASE labelClickable =======================
#
# class ClickLabel(QDialog):
#     def __init__(self, parent=None):
#         super(ClickLabel, self).__init__(parent)
#         self.pixmapImagen = None
#         self.labelImagen = None
#
#         self.setWindowTitle("Label clickable por: ANDRES NIÑO")
#         self.setWindowIcon(QIcon("icono.png"))
#         self.setWindowFlags(Qt.WindowCloseButtonHint | Qt.MSWindowsFixedSizeDialogHint)
#         self.setFixedSize(400, 511)
#
#         self.initUI()
#
#     def initUI(self):
#         # ==================== WIDGET QLABEL =======================
#
#         self.labelImagen = QLabel_click(self)
#         self.labelImagen.setGeometry(15, 15, 118, 130)
#         self.labelImagen.setToolTip("Imagen")
#         self.labelImagen.setCursor(Qt.PointingHandCursor)
#
#         self.labelImagen.setStyleSheet("QLabel {background-color: white; border: 1px solid "
#                                        "#01DFD7; border-radius: 5px;}")
#
#         self.pixmapImagen = QPixmap("Qt.png").scaled(112, 128, Qt.KeepAspectRatio,
#                                                      Qt.SmoothTransformation)
#         self.labelImagen.setPixmap(self.pixmapImagen)
#         self.labelImagen.setAlignment(Qt.AlignCenter)
#
#         # ===================== EVENTO QLABEL ======================
#
#         # Llamar función al hacer clic o doble clic sobre el label
#         self.labelImagen.clicked.connect(self.Clic)
#
#     # ======================= FUNCIONES ============================
#
#     def Clic(self):
#         QMessageBox.information(self, "Tipo de clic",
#                                 "Hicist")
#
#
# # ================================================================
#
# if __name__ == '__main__':
#     import sys
#
#     aplicacion = QApplication(sys.argv)
#
#     ventana = ClickLabel()
#     ventana.show()
#
#     sys.exit(aplicacion.exec_())


# def func_test(num: int) -> int:
#     return num + 1
# print(", ".join("s"))
#
# import requests
# print(requests.get('0WPY0DBOcEpUXEYfV0CcWkyL2ZbWKY7u489mwwSBJhdH6fSnVax26vNY0ddKkW8Q'))
# import platform
# print(platform.uname())
# import os.path
# print(os.path.exists("DataBases/localDB.sqlite"))
import sqlite3
connection = sqlite3.connect('DataBases/localDB.sqlite')
cursor = connection.cursor()
sql = "INSERT INTO save_user(login, password) " \
              "VALUES(?, ?)"
val = ('newAdmin', 'newAdmin')
cursor.execute(sql, val)
connection.commit()
user = cursor.execute('Select * from save_user')
print(user.fetchall())
