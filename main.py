class Pizza:  # класс - пицца, аттрибуты - количество томатов и есть ли соус
    def __init__(self, quantity_tomato: int, is_sauce: bool):
        # присваивание количества томатов
        self._quantity_tomato = quantity_tomato
        # присваивание есть ли соус
        self._is_sauce = is_sauce
        # переменная приготовлена ли пицца, которую можно изменить только вызовом метода
        self._is_ready = False
        # переменная есть ли мясо, которую можно изменить только вызовом метода
        self._is_meat = False

    # геттер для количества томатов
    @property
    def quantity_tomato(self) -> int:
        return self._quantity_tomato

    # сеттер для количества томатов
    @quantity_tomato.setter
    def quantity_tomato(self, new_tom: int) -> None:
        if not isinstance(new_tom, int):
            raise TypeError("Количество томатов должно быть типа int")
        if new_tom <= 0 or new_tom > 20:
            raise ValueError("Количество томатов должно быть положительным числом и меньше 20")
        self._quantity_tomato = new_tom

    # геттер для наличия соуса
    @property
    def is_sauce(self) -> bool:
        return self._is_sauce

    # сеттер для наличия соуса
    @is_sauce.setter
    def is_sauce(self, new_sauce: bool) -> None:
        if not isinstance(new_sauce, bool):
            raise TypeError
        self._is_sauce = new_sauce

    # геттер для наличия мяса
    @property
    def is_meat(self) -> bool:
        return self._is_meat

    # геттер для переменной готова ли пицца
    @property
    def is_ready(self) -> bool:
        return self._is_ready

    def __str__(self):
        return f"Пицца с {self.quantity_tomato} томатами. Есть ли соус: {self.is_sauce}. " \
               f"Готова ли: {self._is_ready}. Есть ли мясо: {self._is_meat}"

    def __repr__(self):
        return f"{self.__class__.__name__}(quantity_tomato={self.quantity_tomato!r}, is_sauce={self.is_sauce!r}, " \
               f"is_ready={self._is_ready!r}, is_meat={self._is_meat})"

    # метод прожаривания пиццы, который наследуется без изменений
    def burn(self) -> str:
        # если пицца уже готова, то выводится предупреждение
        if self._is_ready is True:
            return f"Пицца уже приготовлена"
        else:
            # присваивание переменной приготовления пиццы значение True и вывод сообщения о приготовлении
            self._is_ready = True
            return f"Теперь пицца готова"

    # метод добавления мяса
    def add_meat(self) -> str:
        # если в пицце уже есть мясо, то выводится предупреждение
        if self._is_meat is True:
            return f"В пицце уже есть мясо"
        else:
            # присваивание переменной наличия мяса в пицце значение True и вывод сообщения
            self._is_meat = True
            return f"Теперь в пицце есть мясо"


class VeganPizza(Pizza):
    # метод перегружается для упрощения подачи информации так как параметр is_meat всегда будет равен False
    # потому что это пицца для веганов
    def __str__(self):
        return f"Пицца для веганов с {self._quantity_tomato} томатами. Есть ли соус: {self._is_sauce}. " \
               f"Готова ли: {self._is_ready}"

    # метод добавления мяса перегружается так как нельзя добавить мясо к пицце для веганов
    def add_meat(self) -> str:
        return f"Вы не можете добавить мясо к пицце для веганов"


if __name__ == "__main__":
    # Write your solution here
    pass
