class Service:
    def do_something(self):
        pass

class Client:
    def __init__(self, service):
        self.service = service

    def do_something(self):
        self.service.do_something()

class ConcreteService(Service):
    def do_something(self):
        print("ConcreteService: Doing something!")

class Subject:
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def request(self):
        print("Proxy: Checking access prior to firing a real request.")
        self.real_subject.request()

class Component:
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def operation(self):
        results = []
        for child in self.children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"

service = ConcreteService()
client = Client(service)
client.do_something()

real_subject = RealSubject()
proxy = Proxy(real_subject)
proxy.request()

composite = Composite()
composite.add(Leaf())
composite.add(Leaf())
print(composite.operation())

