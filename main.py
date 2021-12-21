from PyQt5 import QtWidgets  # Импортируем набор виджетов (элементы интерфейса) Qt5
import any_radix_frontend  # Импортируем файл с "версткой" GUI. (Переконвертированный .ui файл)
from any_radix_backend import Translator  # Импортируем класс с логикой программы
import sys  # Импортируем модуль sys для вызова функции выхода

# Наследуем наш класс AnyRadix от классов QtWidgets.QMainWindow, any_radix_frontend.Ui_MainWindow
# Получаем доступ к методам и атрибутам родительского класса
class AnyRadix(QtWidgets.QMainWindow, any_radix_frontend.Ui_MainWindow):
    def __init__(self):
        super().__init__()  # Вызов конструктора родительского класса
        self.setupUi(self)  # Настройка виджета (В данном случае нашего окна)

        # Привязка методов к кнопкам
        self.translateButton.clicked.connect(self.translate)
        self.clearButton.clicked.connect(self.clear_fields)
        self.fileExitAction.triggered.connect(sys.exit)
        self.aboutAction.triggered.connect(self.info)

    # Вызов метода перевода из класса Translate. Заполнение поля результата
    def translate(self):
        input_num = self.inputNumField.text()
        input_num_radix = self.inputNumRadixField.text()
        result_radix = self.resultRadixField.text()
        calc = Translator(input_num, input_num_radix, result_radix)
        self.resultField.setText(calc.translate())

    # Вызов диалогового окна со справкой
    def info(self):
        QtWidgets.QMessageBox.about(self, 'Автор', 'Программа была написана студентом\nФИО')

    # Метод, очищающий поля
    def clear_fields(self):
        self.inputNumField.setText('')
        self.inputNumRadixField.setText('')
        self.resultRadixField.setText('')
        self.resultField.setText('')

# Создание и показ окна
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AnyRadix()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем,
    main()                  # то запускаем функцию main()
