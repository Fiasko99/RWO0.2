import sys
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
import db_data as rf
import platform
import sqlite3
import Auth
import Registration
import EditProfile
import Profile
import Help
import Content
import pymysql
import ItemClass
import MakeComposition
import datetime
from pymysql.cursors import DictCursor


class SearchDB:
    @staticmethod
    def get_profile_by_secret_code(
            secret_code: str, role: str
    ) -> dict:
        connection = DataBase.connect()
        cursor = connection.cursor()

        if len(secret_code) > 7:
            try:
                cursor.execute(
                    "SELECT * FROM " + role +
                    "s WHERE secret_code=%s",
                    secret_code
                )
                return cursor.fetchone()
            except Exception as e:
                HelpWindow().error(str(e))
        else:
            HelpWindow().error(
                "Длина кода доступа должна быть больше 8 символов"
            )

    @staticmethod
    def check_user(login: str, password: str, role: str) -> dict:
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = False
        try:
            success = cursor.execute(
                "SELECT * FROM " + role +
                "s WHERE login_" + role +
                "=%s AND password_" + role +
                "=%s", (login, password))
        except Exception as e:
            AuthWindow().error(str(e))

        if success:
            return cursor.fetchone()
        else:
            AuthWindow().error(
                "Пользователь не найден, "
                "проверьте верность введённых данных"
            )

    @staticmethod
    def get_profile_by_id(id_profile: int, role: str) -> dict:
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = False
        try:
            success = cursor.execute(
                "SELECT * from " + role +
                "s WHERE id=%s", id_profile
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchone()

    @staticmethod
    def get_list_age_limit():
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = False
        list_age = []

        try:
            success = cursor.execute(
                "SELECT value FROM age_limits"
            )
        except Exception as e:
            print(e)

        if success:
            for age in cursor.fetchall():
                list_age.append(age['value'])
            return list_age

    @staticmethod
    def get_id_age_limit_by_value(value: str) -> int:
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = False

        try:
            success = cursor.execute(
                "SELECT id from age_limits"
                " WHERE value=%s", value
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchone()['id']

    @staticmethod
    def check_user_by_login(login: str, role: str) -> bool:
        connection = DataBase.connect()
        cursor = connection.cursor()

        if len(login) >= 6:
            flag_find = cursor.execute(
                "SELECT * from " + role +
                "s WHERE login_" + role +
                "=%s", login
            )

            if flag_find:
                return False
            return True
        return False

    @staticmethod
    def check_user_by_secret_code(secret_code, role):
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = None

        try:
            success = cursor.execute(
                "SELECT * from " + role +
                "s WHERE secret_code=%s", secret_code
            )
        except Exception as e:
            print(e)

        if success:
            return True
        return False

    @staticmethod
    def get_writers() -> list:
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = None

        try:
            success = cursor.execute(
                "SELECT * FROM writers"
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchall()

    @staticmethod
    def get_name_by_id(id_writer):
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = None

        try:
            success = cursor.execute(
                "SELECT name_writer FROM writers"
                " WHERE id=%s", id_writer
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchone()['name_writer']

    @staticmethod
    def get_compositions():
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = None

        try:
            success = cursor.execute(
                "SELECT * FROM compositions"
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchall()

    @staticmethod
    def get_age_limit_by_id(id_age_limit):
        connection = DataBase.connect()
        cursor = connection.cursor()
        success = None

        try:
            success = cursor.execute(
                "SELECT value FROM age_limits"
                " WHERE id=%s", id_age_limit
            )
        except Exception as e:
            print(e)

        if success:
            return cursor.fetchone()['value']


class DataBase:
    @staticmethod
    def connect():
        connection = pymysql.connect(
            host=rf.host(),
            user=rf.user_db(),
            password=rf.password(),
            db=rf.user_db(),
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    @staticmethod
    def connect_local():
        try:
            conn = sqlite3.connect('DataBases/localDB.sqlite')
            return conn
        except Exception as e:
            print(e)


class PostDB:
    @staticmethod
    def create_user(
            login: str, password: str,
            secret_code: str, name: str,
            role: str
    ) -> None:

        if User.check_len_str(
                login, password, secret_code, name
        ):
            connection = DataBase.connect()

            cursor = connection.cursor()

            sql_profile = "INSERT INTO " + role + \
                          "s (login_" + role + \
                          ", password_" + role + \
                          ", secret_code, " \
                          "name_" + role + ") " \
                          "VALUES (%s, %s, %s, %s)"

            val_profile = (
                login, password, secret_code, name
            )

            try:
                PostDB.post(
                    cursor, connection,
                    sql_profile, val_profile
                )
            except Exception as e:
                RegistrationWindow().error(str(e))
        else:
            RegistrationWindow().error(
                " Не соблюдены условия "
                "запрашиваемых данных "
            )

    @staticmethod
    def post_composition(
            name_composition: str, age_limit: str,
            main_genre: str, text_composition: str,
            id_writer: int
    ):
        id_age_limit = SearchDB.get_id_age_limit_by_value(age_limit)

        connection = DataBase.connect()
        cursor = connection.cursor()

        sql = "INSERT INTO compositions " \
              "(name_composition, main_genre, " \
              "id_age_limit, text_composition, id_writer) " \
              "VALUES (%s, %s, %s, %s, %s)"

        values = (
            name_composition, main_genre,
            id_age_limit, text_composition,
            id_writer
        )
        try:
            PostDB.post(
                cursor, connection,
                sql, values
            )
        except Exception as e:
            print(e)

    @staticmethod
    def post(cursor, connection, sql, values):
        success = cursor.execute(sql, values)
        if success == 1:
            connection.commit()
        else:
            RegistrationWindow().error(
                'Ошибка!\n'
                'Данные не были отправлены'
            )


class User:
    def __init__(self,
                 id_profile: int, login: str,
                 name: str, role: str
                 ):
        self.id_profile = id_profile
        self.login = login
        self.name = name
        self.role = role
        self.date_of_born = datetime.datetime.today()
        self.additional_field = None

    @staticmethod
    def convert(word: str) -> str:
        if word == "Инвестор":
            return "offer"
        elif word == "Писатель":
            return "writer"
        elif word == "Читатель":
            return "reader"

    @staticmethod
    def un_convert(word: str) -> str:
        if word == "offer":
            return "offerИнвестор"
        elif word == "writer":
            return "Писатель"
        elif word == "reader":
            return "Читатель"

    @staticmethod
    def check_len_str(
            login: str, password: str,
            secret_code: str, name: str
    ) -> bool:
        if len(login) < 6:
            return False
        elif len(password) < 8:
            return False
        elif len(secret_code) < 8:
            return False
        elif len(name) < 3:
            return False
        else:
            return True


class MakeCompositionWindow(
    QtWidgets.QMainWindow, MakeComposition.Ui_MakeComposition
):
    def __init__(self, user_connect):
        super().__init__()
        self.setupUi(self)
        self.user_connect = user_connect
        self.new_window = None
        self.send_btn.clicked.connect(self.send_composition)
        self.back_btn.clicked.connect(self.back_window)

    def send_composition(self):
        name_composition = self.name_value.text()
        age_limit = self.age_limit_box.currentText()
        main_genre = self.main_genre_value.text()
        text_composition = self.text_composition_value.toPlainText()

        if self.check_len(name_composition, 2) \
                and self.check_len(main_genre, 2) \
                and self.check_len(text_composition, 100):
            PostDB.post_composition(
                name_composition,
                age_limit,
                main_genre,
                text_composition,
                self.user_connect.id_profile
            )
            self.information_label.setText("Пост успешно отправлен!")
        else:
            self.error(
                "Не оставляйте поля пустыми!"
                " Минимальный порог пропуска: 2 символа"
            )

    def back_window(self):
        self.new_window = ProfileWindow(
            self.user_connect
        )
        self.new_window.on_load_profile()
        self.new_window.show()
        self.close()

    def on_load_age_limit(self):
        try:
            self.age_limit_box.addItems(
                SearchDB.get_list_age_limit()
            )
        except Exception as e:
            print(e)

    def error(self, e):
        QtWidgets.QMessageBox.information(self, 'Error', e)

    @staticmethod
    def check_len(text: str, count: int) -> bool:
        if len(text) >= count:
            return True
        return False


class AuthWindow(QtWidgets.QMainWindow, Auth.Ui_AuthWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_window = None
        self.user_connect = None
        self.login_btn.clicked.connect(self.check_existence)
        self.registration_btn.clicked.connect(self.registration_window)
        self.help_btn.clicked.connect(self.help_window)

    def check_existence(self):
        login = self.login_value.text()
        password = self.password_value.text()
        role = User.convert(
            self.role_value.currentText()
        )
        # Конвертиртация в английский вариант
        profile = None

        if len(login) > 5 and len(password) > 7\
                and role:
            profile = SearchDB.check_user(login, password, role)
            # Если пользователь существует, то вернет его профиль
        else:
            self.error("Форма заполнена неверно")

        if isinstance(profile, dict):
            self.fill_user_class(profile, role)
            self.save_user_local()

    def save_user_local(self):
        login = self.user_connect.login
        password = self.password_value.text()
        system = platform.system()
        version = platform.version()
        processor = platform.processor()

        spl = "INSERT INTO save_user(login, password) " \
              "VALUES(?, ?)"
        val = (login, password)

        sql_platform = "INSERT INTO " \
                       "platform_user(system, version, processor, id_user) " \
                       "VALUES(?, ?, ?, ?)"
        success = None

        try:
            connection = DataBase.connect_local()
            cursor = connection.cursor()
            cursor.execute(spl, val)
            connection.commit()
            success = cursor.lastrowid
            if success:
                cursor.execute(
                    sql_platform, (
                        system, version, processor, success
                    )
                )
                connection.commit()
        except Exception as e:
            self.error(str(e))

    def fill_user_class(self, profile: dict, role: str):
        try:
            self.user_connect = User(
                profile['id'],
                profile['login_' + role],
                profile['name_' + role],
                role
            )
            self.profile_window()
        except Exception as e:
            self.error(str(e))

    def registration_window(self):
        self.new_window = RegistrationWindow()
        self.new_window.show()
        self.close()

    def help_window(self):
        self.new_window = HelpWindow()
        self.new_window.show()
        self.close()

    def profile_window(self):
        if self.user_connect:
            self.new_window = ProfileWindow(
                self.user_connect
            )
            self.new_window.on_load_profile()
            self.new_window.show()
            self.close()

    def error(self, error: str):
        # QtWidgets.QMessageBox.information(
        #     self, 'Error', error
        # )
        print(error)


class RegistrationWindow(
    QtWidgets.QMainWindow, Registration.Ui_RegistrationWindow
):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.new_window = None
        self.agree_label.setVisible(False)
        self.agree_checkbox.setVisible(False)
        self.role_value.currentTextChanged.connect(self.change_visible_checkbox)
        self.agree_checkbox.stateChanged.connect(self.change_enable_btn)
        self.registration_btn.setEnabled(False)
        self.registration_btn.clicked.connect(self.registration_user)
        self.back_btn.clicked.connect(self.back_window)

    def registration_user(self):
        login = self.login_value.text()
        password = self.password_value.text()
        secret_code = self.secret_code_value.text()
        name = self.name_value.text()
        role = User.convert(
            self.role_value.currentText()
        )

        if role:
            PostDB.create_user(
                login, password,
                secret_code, name,
                role
            )
            self.new_window = AuthWindow()
            self.new_window.show()
            self.close()
        else:
            self.error(
                "  Вы не выбрали роль   "
            )

    def change_enable_btn(self):
        self.flag = not self.flag
        self.registration_btn.setEnabled(self.flag)

    def change_visible_checkbox(self):
        value_combo = self.role_value.currentText()

        if value_combo == "Инвестор":
            self.agree_label.setVisible(True)
            self.agree_checkbox.setVisible(True)
        else:
            self.agree_label.setVisible(False)
            self.agree_checkbox.setVisible(False)

    def back_window(self):
        self.new_window = AuthWindow()
        self.new_window.show()
        self.close()

    def error(self, e):
        QtWidgets.QMessageBox.information(self, 'Error', e)


class HelpWindow(QtWidgets.QMainWindow, Help.Ui_HelpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.new_window = None
        self.send_btn.clicked.connect(self.check_data)
        self.back_btn.clicked.connect(self.auth_window)

    def auth_window(self):
        self.new_window = AuthWindow()
        self.new_window.show()
        self.close()

    def check_data(self):
        role = User.convert(
            self.role_value.currentText()
        )
        secret_code = self.secret_code_value.text()

        if role:
            profile = SearchDB.get_profile_by_secret_code(
                secret_code, role
            )
            self.fill_labels(profile, role)
        else:
            self.error("Нужно выбрать роль")

    def error(self, message):
        QtWidgets.QMessageBox.information(
            self, 'Error', message
        )

    def fill_labels(self, profile: dict, role: str) -> None:
        if isinstance(profile, dict):
            login = self.login_label.text() + profile['login_' + role]
            password = self.password_label.text() + profile['password_' + role]

            self.login_label.setText(login)
            self.password_label.setText(password)
        else:
            self.error("  Повторите попытку  ")


class ProfileWindow(QtWidgets.QMainWindow, Profile.Ui_ProfileWindow):
    def __init__(self, user_connect):
        super().__init__()
        self.setupUi(self)
        self.new_window = None
        self.user_connect = user_connect
        self.back_btn.clicked.connect(self.back_window)
        self.content_btn.clicked.connect(self.content_window)
        self.edit_data_btn.clicked.connect(self.edit_window)
        self.history_auth_btn.clicked.connect(self.history_window)

    def on_load_profile(self):
        re_role = User.un_convert(
            self.user_connect.role
        )
        # Конвертация роли в русский вариант
        self.login_value_label.setText(self.user_connect.login)
        self.name_value_label.setText(self.user_connect.name)
        self.role_value_label.setText(re_role)

        self.profile_filling_processing_by_role(self.user_connect.role)
        # Заполнение индивидуальных полей роли

    def profile_filling_processing_by_role(
            self, role: str
    ):
        profile = SearchDB.get_profile_by_id(
            self.user_connect.id_profile, role
        )
        if role == "writer":
            date = profile['date_of_born']
            self.user_connect.date_of_born = date
            self.date_value_label.setText(str(date))
            self.additional_btn.setText("Написать новый пост")
            self.additional_btn.clicked.connect(self.open_make_composition_w)
        elif role == "reader":
            date = profile['date_of_born']
            self.user_connect.date_of_born = date
            self.date_value_label.setText(str(date))
            self.additional_btn.setText("Открыть избранные произведения")
            self.additional_btn.clicked.connect(self.open_compositions)
        elif role == "offer":
            self.date_value_label.setText(str("Совершеннолетний"))
            self.additional_btn.setText("Открыть записку")
            self.additional_btn.clicked.connect(self.open_note)

    def back_window(self):
        self.new_window = AuthWindow()
        self.new_window.show()
        self.close()

    def content_window(self):
        self.new_window = ContentWindow(
            self.user_connect
        )
        self.new_window.load_content()
        self.new_window.show()
        self.close()

    def edit_window(self):
        self.new_window = EditProfileWindow(self.user_connect)
        self.new_window.show()
        self.close()

    def history_window(self):
        pass

    def open_make_composition_w(self):
        self.new_window = MakeCompositionWindow(
            self.user_connect
        )
        self.new_window.on_load_age_limit()
        self.new_window.show()
        self.close()

    def open_note(self):
        pass

    def open_compositions(self):
        pass

    def error(self, error: str):
        QtWidgets.QMessageBox.information(
            self, 'Error', error
        )


class EditProfileWindow(
    QtWidgets.QMainWindow, EditProfile.Ui_EditProfileWindow
):
    def __init__(self, user_connect):
        super().__init__()
        self.setupUi(self)
        self.new_window = None
        self.user_connect = user_connect
        self.edit_btn.clicked.connect(self.send_edit_data)
        self.back_btn.clicked.connect(self.profile_window)

    def send_edit_data(self):
        login = self.login_value.text()
        password = self.password_value.text()
        name = self.name_value.text()
        date = self.date_value.date().toPyDate()

        response = self.validate_data_for_relevance(
            login, password, name, date
        )
        success = None

        if response == "Невозможный логин":
            self.error(response)
        else:
            secret_code = self.secret_code_value.text()
            success = SearchDB.check_user_by_secret_code(
                secret_code, self.user_connect.role
            )

        if success:
            print("Замена успешна")
        else:
            self.error("Неверный секретный ключ")

    def profile_window(self):
        self.new_window = ProfileWindow(
            self.user_connect
        )
        self.new_window.on_load_profile()
        self.new_window.show()
        self.close()

    def validate_data_for_relevance(
            self, login: str,
            password: str, name: str,
            date
    ) -> str:

        try:
            date_of_born = self.user_connect.date_of_born
            list_values = []

            if SearchDB.check_user_by_login(
                    login, self.user_connect.role
            ):
                if len(login) >= 6:
                    list_values.append("login")
                if len(password) >= 8:
                    list_values.append("password")
                if len(name) >= 3:
                    list_values.append("name")
                if date != date_of_born:
                    list_values.append("date")

                return ", ".join(list_values)
            else:
                return "Невозможный логин"
        except Exception as e:
            print(e)

    def error(self, error: str):
        QtWidgets.QMessageBox.information(
            self, 'Error', error
        )


class ContentWindow(QtWidgets.QMainWindow, Content.Ui_ContentWindow):
    def __init__(self, user_connect):
        super().__init__()
        self.setupUi(self)
        self.new_window = None
        self.label_composition = None
        self.user_connect = user_connect
        self.content_btn.clicked.connect(self.profile_window)

    def profile_window(self):
        self.new_window = ProfileWindow(
            self.user_connect
        )
        self.new_window.on_load_profile()
        self.new_window.show()
        self.close()

    def load_content(self):
        try:
            compositions = SearchDB.get_compositions()
            for composition in compositions:
                name_writer = SearchDB.get_name_by_id(
                    composition['id_writer']
                )
                name_writer = "Автор: " + name_writer
                genre = "Основной жанр: " + composition["main_genre"]
                left_label = "\n".join([
                    name_writer, genre
                ])
                # Левая колонка блока поста
                name = "Название произведения: " + composition['name_composition']
                age = "Ограничение возраста: " + SearchDB.get_age_limit_by_id(
                    composition['id_age_limit']
                )
                composition = composition['text_composition']
                text_area = "\n".join([
                    name, age, composition
                ])
                # Правая колонка блока поста
                item_widget = ItemClass.Item(
                    left_label, text_area,
                    self.user_connect, composition['id_writer']
                )
                # Создание цельного блока для каждого поста автора
                item_layout = QtWidgets.QVBoxLayout()
                item_layout.addWidget(item_widget)
                self.item.addLayout(item_layout)
                # Добавление созданных экземпляров в основное окно
            self.item.setAlignment(Qt.AlignTop)
            self.scroll_area_widget_contents.setLayout(self.item)
        except Exception as e:
            self.error(str(e))

    def error(self, error: str):
        QtWidgets.QMessageBox.information(
            self, 'Error', error + "\nОшибка загрузки"
        )


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AuthWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
