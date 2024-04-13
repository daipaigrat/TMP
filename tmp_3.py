from abc import ABC, abstractmethod

class AbstractCreator(ABC):
    @abstractmethod
    def create_item(self):
        pass

class Creator1(AbstractCreator):
    def create_item(self):
        print("Создание продукта 1...")
        return Item1()

class Creator2(AbstractCreator):
    def create_item(self):
        print("Создание продукта 2...")
        return Item2()

class Item(ABC):
    pass

class Item1(Item):
    def __init__(self):
        print("Продукт 1 создан!")

class Item2(Item):
    def __init__(self):
        print("Продукт 2 создан!")

class Supervisor:
    def __init__(self, builder):
        self._builder = builder

    def construct(self):
        print("Начинаем строительство...")
        self._builder.build_step_a()
        self._builder.build_step_b()
        print("Строительство завершено!")
        return self._builder.object

class Builder(ABC):
    @abstractmethod
    def build_step_a(self):
        pass

    @abstractmethod
    def build_step_b(self):
        pass

class ConcreteBuilder(Builder):
    def __init__(self):
        self.object = Object()

    def build_step_a(self):
        print("Выполняем шаг A...")
        self.object.add("Шаг A")

    def build_step_b(self):
        print("Выполняем шаг B...")
        self.object.add("Шаг B")

class Object:
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def list_steps(self):
        print("Выполненные шаги: ", ", ".join(self.steps))

class Original:
    def request(self):
        return "Запрос от оригинального класса"

class OldClass:
    def specific_request(self):
        return "Запрос от старого класса"

class Adapter(Original):
    def __init__(self, old_class):
        self.old_class = old_class

    def request(self):
        return self.old_class.specific_request()

class Mediator:
    def notify(self, sender, event):
        pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender, event):
        if event == "A":
            print("Посредник реагирует на A и запускает следующие операции:")
            self._component2.do_c()
        elif event == "D":
            print("Посредник реагирует на D и запускает следующие операции:")
            self._component1.do_b()
            self._component2.do_c()

class BaseComponent:
    def __init__(self, mediator=None):
        self._mediator = mediator

    @property
    def mediator(self):
        return self._mediator

    @mediator.setter
    def mediator(self, mediator):
        self._mediator = mediator

class Component1(BaseComponent):
    def do_a(self):
        print("Компонент 1 делает A.")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Компонент 1 делает B.")
        self.mediator.notify(self, "B")

class Component2(BaseComponent):
    def do_c(self):
        print("Компонент 2 делает C.")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Компонент 2 делает D.")
        self.mediator.notify(self, "D")

        
creator1 = Creator1()
item1 = creator1.create_item()

creator2 = Creator2()
item2 = creator2.create_item()

supervisor = Supervisor(ConcreteBuilder())
object = supervisor.construct()
object.list_steps()

old_class = OldClass()
adapter = Adapter(old_class)
print(adapter.request())

c1 = Component1()
c2 = Component2()
mediator = ConcreteMediator(c1, c2)

print("Клиент запускает операцию A.")
c1.do_a()

print("\n")
print("Клиент запускает операцию D.")
c2.do_d()

