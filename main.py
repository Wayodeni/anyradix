from PyQt5 import QtWidgets
import any_radix_frontend
from any_radix_backend import Translator
import sys


class AnyRadix(QtWidgets.QMainWindow, any_radix_frontend.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.translateButton.clicked.connect(self.translate)
        self.clearButton.clicked.connect(self.clear_fields)
        self.fileExitAction.triggered.connect(sys.exit)
        self.aboutAction.triggered.connect(self.info)

    def translate(self):
        input_num = self.inputNumField.text()
        input_num_radix = self.inputNumRadixField.text()
        result_radix = self.resultRadixField.text()
        calc = Translator(input_num, input_num_radix, result_radix)
        self.resultField.setText(calc.translate())

    def info(self):
        QtWidgets.QMessageBox.about(self, 'Автор', 'Программа была написана студентом\nФИО')

    def clear_fields(self):
        self.inputNumField.setText('')
        self.inputNumRadixField.setText('')
        self.resultRadixField.setText('')
        self.resultField.setText('')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AnyRadix()
    window.show()
    app.exec_()


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем,
    main()                  # то запускаем функцию main()
