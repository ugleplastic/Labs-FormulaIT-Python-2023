# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class Pizza: # класс - пицца, аттрибуты - количество томатов и есть ли соус
    def __init__(self, quantity_tomato: int, is_sauce: bool):
        # проверка чтобы количество томатов на пицце было числом
        if not isinstance(quantity_tomato, int):
            raise TypeError
        if quantity_tomato > 20: # проверка на максимальное количество томатов на пицце
            raise ValueError
        # присваивание количества томатов
        self.quantity_tomato = quantity_tomato

        # проверка чтобы наличие соуса было типом bool
        if not isinstance(is_sauce, bool):
            raise TypeError
        # присваивание есть ли соус
        self.is_sauce = is_sauce

    # метод добавления соуса
    def add_sauce(self):
        # если он уже есть выводится предупреждение
        if self.is_sauce is True:
            print("Соус уже добавлен")
        else:
            # присвание атрибуту наличия соуса значение True и вывод сообщения о выполнении
            self.is_sauce = True
            print("Соус теперь добавлен")

    # метод добавления томатов
    def add_tomatoes(self, addition: int):
        # проверка чтобы переменная была числом
        if not isinstance(addition, int):
            raise TypeError
        # проверка может ли пицца выдержать столько томатов
        if addition + self.quantity_tomato > 20:
            print("Нельзя добавить так много томатов, потому что в сумме будет больше чем наш ресторан позволяет")
        else:
            # добавление томатов в случае нужного количества и вывод сообщения
            self.quantity_tomato += addition
            print(f"Теперь у вас {self.quantity_tomato} томатов на пицце")


class Pelmeni: # класс - тарелка пельменей, атрибуты - количество пельменей, есть ли сметана
    def __init__(self, quantity: int, is_smetana: bool):
        # проверка не является ли это числом и на максимальное количество в тарелке
        if not isinstance(quantity, int):
            raise TypeError
        if quantity > 40:
            raise ValueError
        self.quantity = quantity

        # проверка является яли наличие сметаны bool
        if not isinstance(is_smetana, bool):
            raise TypeError
        self.is_smetana = is_smetana

    # метод добавления пельменей в тарелку
    def add_quantity(self, addition: int):
        # проверка является ли это числом
        if not isinstance(addition, int):
            raise TypeError
        # проверка можно ли столько уместить в тарелке
        if addition + self.quantity > 40:
            print("Мы не можем добавить столько пельменей, ваша тарелка не выдержит")
        else:
            # если можно, то добавление и вывод сообщения об успехе
            self.quantity += addition
            print(f"Теперь у вас в тарелке {self.quantity} пельменей")

    # метод добавления сметаны
    def add_smetana(self):
        # если сметана уже есть вывод сообщения
        if self.is_smetana is True:
            print("Ваша сметана уже на столе, посмотрите получше")
        else:
            # если сметаны нет атрибуту присваивается значение True и выводится сообщение об успехе
            self.is_smetana = True
            print("Сметана была добавлена к вашим пельменям")


class Pasta: # класс - паста, атрибуты - вегетарианская ли она и есть ли в ней соус
    def __init__(self, is_vegan: bool, is_sauce: bool):
        # проверка является ли переменная is_vegan bool
        if not isinstance(is_vegan, bool):
            raise TypeError
        # присвоение атрибуту значения
        self.is_vegan = is_vegan

        # проверка является ли переменная is_sauce bool
        if not isinstance(is_sauce, bool):
            raise TypeError
        # присвоение атрибуту значения
        self.is_sauce = is_sauce

    # метод добавления соуса
    def add_sauce(self):
        # если он уже есть выводится сообщение
        if self.is_sauce is True:
            print("Соус уже в пасте")
        else:
            # если соуса нет он добавляется и выводится сообщение об успехе
            self.is_sauce = True
            print("Теперь ваша паста с соусом")

    # метод добавления мяса в пасту
    def add_meat(self):
        # если в пасте уже есть мясо выводится сообщение
        if self.is_vegan is False:
            print("Ваша паста уже с мясом, вам достаточно")
        else:
            # если паста была вегетарианской, то добавляется мясо и выводится сообщение об успехе
            self.is_vegan = False
            print("Теперь в вашей пасте есть мясо")


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
