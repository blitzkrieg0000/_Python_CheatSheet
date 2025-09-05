
"""
    Metaclass tüm özelliklerini child class a aktarır. Obje üzerine bir takım ekleme ve çıkarmalar yapmak mümkündür.
"""
class MyMetaClass(type):
    #! 2
    """
        Objenin instanceını oluşturup döndürür. Ancak metclass type den kalıtıldığı için normal __new__ den biraz farklı olarak 
        sanki type() ile obje oluşturuyormuşçasına sınıf ismi, base classlar ve sınıf metodları üzerinde de kapsamlı bir obje yönetimi sağlar.
    """
    def __new__(cls, name, bases, dct):
        dct['metafunction'] = lambda self: "metafunction"
        _instance = super().__new__(cls, name, bases, dct)
        _instance.data = "Yeni Property"
        return _instance


#! 1
class BaseClass():
    def __init__(self):
        self.metadata="meta"



class MyClass(BaseClass, metaclass=MyMetaClass):
    #! 3
    """
        Objenin instanceını oluşturup döndürür.
    """
    def __new__(cls, *args, **kwargs):
        
        return super().__new__(cls)

    #! 4
    def __init__(self, value):
        super().__init__()
        self.value = value



obj = MyClass(value=42)

# From Base
print(obj.metadata)

# From Metaclass
print(obj.data)

print(obj.metafunction())