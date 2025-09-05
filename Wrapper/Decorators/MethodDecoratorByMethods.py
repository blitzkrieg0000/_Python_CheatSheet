# =================================================================================================================== #
#! Parametresiz Decoratorlar                                                                                          #
# =================================================================================================================== #

"""
    Decorator metodu alır ve geriye yeni bir inner metot (wrapper) döndürür.
"""
def MyDecorator(func):

    def wrapper(*args, **kwargs):
        """
            Inner metotta ise gelen argümanlar işlenir ve dışarıdan gelen metot çağırılarak sonucu döndürülür.
        """
        print("Wrapper Metot!")

        #! <Varsayılan metotdan önce>
        result = func(*args, **kwargs) # Varolan metot çağırılır.
        #! <Varsayılan metotdan sonra>

        return result
    
    return wrapper  # Yeni metot(wrapper | inner) çağırılmadan döndürülür.



@MyDecorator
def MyMethod(a, b, c=10):
    print("Mevcut metot!")
    return a*b+c


result = MyMethod(3, 5)
print(result)




print()
# =================================================================================================================== #
#! Parametreli decoratorlar                                                                                           #
# =================================================================================================================== #
"""
    Decorator metodu alır ve geriye yeni bir inner metot (wrapper) döndürür.
"""

def MyDecorator(id):
    print(id)
    def decorator(func):
        def wrapper(*args, **kwargs):
            """
                Inner metotta ise gelen argümanlar işlenir ve dışarıdan gelen metot çağırılarak sonucu döndürülür.
            """
            print("Wrapper Metot!")

            #! <Varsayılan metotdan önce>
            result = func(*args, **kwargs) # Varolan metot çağırılır.
            #! <Varsayılan metotdan sonra>

            return result
        
        return wrapper  # Yeni metot(wrapper | inner) çağırılmadan döndürülür.
    return decorator


@MyDecorator("ID0001")
def MyMethod(a, b, c=10):
    print("Mevcut metot!")
    return a*b+c


result = MyMethod()
print(result)
