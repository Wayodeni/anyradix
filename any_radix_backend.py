'''
В этом файле содержится класс переводчика из одной СС в другую.
Чтобы не засорять фронтенд логикой программы, ее класс вынесен в этот файл.

Конструктор класса принимает на вход число, основание его СС, и СС результирую-
щего числа. Для расчета результата вызывается метод translate(), который возвр-
ащает переменную типа string.
'''
# TODO: Зарефакторить "исключения". Вынести их в отдельный строковый метод.
import string


class Translator():
    def __init__(self, input_number = '0', input_number_radix = 10,
     result_radix = 10):
        '''
        Конструктор класса Translator.
        Задает необходимые атрибуты, которые позже будут обрабатываться внутри 
        метода translate.
        '''
        self.input_number = str(input_number).upper()
        self.input_number_radix = input_number_radix
        self.result_radix = result_radix


    def translate(self) -> str:
        '''
        Метод отвечает за валидацию входных данных и перевод числа.
        Возвращает либо строку с описанием ошибки, либо строку содержащую резу-
        льтат.
        '''

        # Если пустой ввод хотя бы в одном из полей, то в поле результата выво-
        # дим 'Пустое поле ввода'.
        if self.input_number == '' or self.input_number_radix == '' or \
            self.result_radix == '':
            return 'Пустое поле ввода'

        # Если в унарной СС есть лишние символы или в других СС есть лишние 
        # символы, а также если есть лишние символы в полях оснований СС, то в
        # поле результата выводим 'Удалите лишние символы'.
        if (self.input_number.isalnum() == False\
            and set(self.input_number) != {'|'})\
            or str(self.input_number_radix).isdigit() == False\
            or str(self.result_radix).isdigit() == False:
            return 'Удалите лишние символы'

        # После проверки оснований СС на то, что они состоят только из чисел, 
        # можем преобразовать их в int.
        self.input_number_radix = int(self.input_number_radix)
        self.result_radix = int(self.result_radix)

        # Если любое из оснований сс превышает диапазон 1-37, то в поле 
        # результата выводим 'Неверное основание системы счисления'
        if self.input_number_radix not in range(1, 37) or self.result_radix\
            not in range(1, 37):
            return 'Неверное основание системы счисления'

        # Если на вход было подано число в унарной сс, но указана другая сс, 
        # то в поле результата выводим 'Неверная система счисления для унарного
        # числа'
        if set(self.input_number) == {'|'} and self.input_number_radix != 1:
            return 'Неверная система счисления для унарного числа'

        # Если число превышает основание своей сс, то в поле результата выводим
        # 'Введенное число превышает свою систему счисления'
        if Translator.is_exceeds_radix(self.input_number, 
        self.input_number_radix) == True:
            return 'Введенное число превышает свою систему счисления'

        # Нуль во всех сс есть нуль.
        if self.input_number == '0':
            return '0'

        # Перевод введенного числа в 10сс
        if self.input_number_radix == 1:
            input_number_in_10th_radix = self.input_number.count('|')
        elif self.input_number_radix == 10:
            input_number_in_10th_radix = int(self.input_number)
        else:
            input_number_in_10th_radix =\
            Translator.translate_to_10th_radix(self.input_number, 
            self.input_number_radix)
        
        # Формирование результата
        n = input_number_in_10th_radix
        result = ''
        if self.result_radix == 1:
            return input_number_in_10th_radix * '|'
        elif self.result_radix in range(2, 11):
            while n:
                result = str(n % self.result_radix) + result
                n //= self.result_radix
            return result
        else:
            while n:
                result = Translator.number_to_literal(n % self.result_radix)\
                + result
                n //= self.result_radix
            return result


    @staticmethod
    def translate_to_10th_radix(input_number: str, input_number_radix: int) -> int:
        '''
        Создаем статический метод т.к. его можно использовать позже в других 
        модулях для абсолютно любых переводов. После всех проведенных проверок,
        совершаемых на этапе вызова метода translate(), данный метод принимает
        число в строковом виде из поля ввода, его систему счисления и переводит
        его в 10 СС (приведение к стандартному виду).
        '''

        # Для унарной СС
        if input_number_radix == 1:
            number_in_10th_radix = input_number.count('|')
            return number_in_10th_radix
        
        number_in_10th_radix = 0
        power_of_radix = len(input_number) - 1
        if input_number_radix in range(1, 11):
            for numeral in input_number:
                number_in_10th_radix += int(numeral) * input_number_radix**power_of_radix
                power_of_radix -= 1 
        elif input_number_radix in range(11, 37):
            for literal in input_number:
                number_in_10th_radix += int(Translator.literal_to_number(literal))\
                    * input_number_radix**power_of_radix
                power_of_radix -= 1 
        return number_in_10th_radix


    @staticmethod
    def literal_to_number(literal: str) -> int:
        '''
        Данный метод вызывается при поразрядном парсинге числа и переводит
        буквы в числах (СС >= 11) в цифры в 10 СС.
        '''
        # Если на вход пришла цифра не в буквенном виде, то возвращаем ее. 
        if literal.isdigit():
            return int(literal)

        # Генерация словаря, в котором содержится соответствие букв английского
        # алфавита цифрам в 10 СС
        alphabet = {}
        number = 10
        for letter in string.ascii_uppercase:
            alphabet[letter] = number
            number += 1
        
        return alphabet[literal]


    @staticmethod
    def number_to_literal(numeral: int) -> str:
        '''
        Данный метод вызывается при поразрядном парсинге числа и 
        преобразовывает числа от 10 и далее в буквенные разряды для СС
        больше 10.
        '''

        # Если на вход пришла цифра меньше 10, то для нее не будет буквы в 
        # СС > 10. Преобразовываем в str и возвращаем.
        if numeral < 10:
            return str(numeral)

        # Генерация словаря, в котором содержится соответствие цифр буквам 
        # английского алфавита
        alphabet = {}
        number = 10
        for letter in string.ascii_uppercase:
            alphabet[number] = letter
            number += 1

        return alphabet[numeral]


    @staticmethod
    def is_exceeds_radix(input_number: str, input_number_radix: int) -> bool:
        '''
        Данный метод проверяет число на соответствие указанной для него системе
        счисления. Если число содержит цифру, превышающую основание системы 
        счисления, то возвращается True. В противном случае возвращается False.
        '''

        # Для унарной СС
        if set(input_number) == {'|'}:
            return False
        
        if input_number.isdigit():
            if int(max(list(input_number))) >= input_number_radix:
                return True
        else:
            if Translator.literal_to_number(max(input_number)) >= input_number_radix:
                return True

        return False


def main():
    num = input('Введите число для перевода: ')
    num_radix = input('Введите СС числа для перевода: ')
    result_radix = input('Введите основание СС результата: ')
    calc = Translator(num, num_radix, result_radix)
    print(calc.translate())


if __name__ == '__main__':
    main()
