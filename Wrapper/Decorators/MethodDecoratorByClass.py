class NewMethodDecorator():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):        # __call__, pythonda, sınıf instance'ının metod gibi kullanılmasını sağlar.
        print("Method Decorator Class")
        return self.func(self, *args, **kwargs)



class MyClass():
    def __init__(self, value):
        self.value = value

    @NewMethodDecorator
    def Work(self):
        print("Mevcut metot.")



obj = MyClass(72)
obj.Work()