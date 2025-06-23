class Singleton:
    # A class variable that holds the single instance
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print(" Creating a new instance")
            cls._instance = super(Singleton, cls).__new__(cls)
        else:
            print("📦 Returning existing instance")
        return cls._instance

    def __init__(self, value):
        self.value = value


class MyClass:
    class_variable = "I'm at class level"

    def __init__(self, item: str):
        self.__box = item

    def instance_method(self):

        print(MyClass.class_variable)

    def print_box(self):
        print("The box contains:", self.__box)

obj = MyClass("flower")
obj.instance_method()
obj.print_box()
