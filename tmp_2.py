class StringIterator:
    def __init__(self, string_to_iterate):
        self.string = string_to_iterate
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position >= len(self.string):
            raise StopIteration
        char = self.string[self.position]
        self.position += 1
        return char

class ElementOne:
    def accept(self, visitor):
        visitor.visit_element_one(self)

class ElementTwo:
    def accept(self, visitor):
        visitor.visit_element_two(self)

class MyVisitor:
    def visit_element_one(self, element):
        print("Посетили первый элемент")

    def visit_element_two(self, element):
        print("Посетили второй элемент")

print("Итератор:")
my_string = StringIterator("Привет")
for letter in my_string:
    print(letter)

print("\nПосетитель:")
elements = [ElementOne(), ElementTwo()]
visitor = MyVisitor()

for element in elements:
    element.accept(visitor)

