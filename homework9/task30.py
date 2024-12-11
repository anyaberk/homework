#  1. Реализовать класс DB - синглтон. Экземляр класса(подключение) к PostgreSQL
#  должно быть единственным.

#  2. Реализовать  фабрику которая создает модели различных производителей

class Car:
    def __init__(self, brand, model):
        """Инициализируйте атрибуты brand и model"""
        self.brand = brand
        self.model = model
    def __repr__(self):
        "Реализуйте логику дандера"
        return f'Бренд: {self.brand}, модель: {self.model}'

class  CarZavod:
    def make_lada(self, model='granta'):
        "реализуйте метод для создания  автомобиля Lada"

        return Car("Lada", model)

    def make_mercedes(self, model='s-class'):
        "реализуйте метод для создания  автомобиля Mercedes"

        return Car("Mercedes", model)

    def make_toyota(self, model='camry'):
        "реализуйте метод для создания создания Toyota"
        return Car("Toyota", model)


factory = CarZavod()
print(factory.make_lada())
print(factory.make_lada('priora'))


    # 3. Реализовать для класса Car абстрактный класс который содержит
    # aбстрактные методы sold, discount

from abc import ABC, abstractmethod

class Car2(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def sold(self):
        pass

    @abstractmethod
    def discount(self):
        pass

    def __repr__(self):
        return f'Бренд: {self.brand}, модель: {self.model}'


class Lada(Car2):
    def __init__(self, model="Granta"):
        super().__init__("Lada", model)

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 5%")


class Mercedes(Car2):
    def __init__(self, model="C-Class"):
        super().__init__("Mercedes", model)

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 55%")


class Toyota(Car2):
    def __init__(self, model="Camry"):
        super().__init__("Toyota", model)

    def sold(self):
        print(f"Автомобиль {self.brand} {self.model} продан")

    def discount(self):
        print(f"На автомобиль {self.brand} {self.model} скидка 12%")

a=Toyota('Prius')

a.discount()
a.sold()