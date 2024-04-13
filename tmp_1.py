from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute_algorithm(self):
        pass

class ConcreteStrategyA(Strategy):
    def execute_algorithm(self):
        return "Алгоритм A"

class ConcreteStrategyB(Strategy):
    def execute_algorithm(self):
        return "Алгоритм B"

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute_algorithm()

class AbstractClass(ABC):
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()

    def base_operation1(self):
        return "Базовая операция1"

    def base_operation2(self):
        return "Базовая операция2"

    @abstractmethod
    def required_operations1(self):
        pass

    def hook1(self):
        pass

class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        return "Операция1 класса1"

    def hook1(self):
        return "Перехват1 класса1"

class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        return "Операция1 класса2"

    def hook1(self):
        return "Перехват1 класса2"

context = Context(ConcreteStrategyA())
print(context.execute_strategy())  

context.set_strategy(ConcreteStrategyB())
print(context.execute_strategy())  

concrete_class = ConcreteClass1()
concrete_class.template_method()

concrete_class = ConcreteClass2()
concrete_class.template_method()
