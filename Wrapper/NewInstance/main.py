import datetime
import time


class Singleton():
    _instance = None
    time = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls.time = datetime.datetime.utcnow()

        return cls._instance


    def __init__(self, *args, **kwargs):
        self.time = datetime.datetime.utcnow()



# safe block(main)
if "__main__" == __name__:
    
    s1 = Singleton()
    print(s1.time)

    s2 = Singleton()
    print(s1.time)
    print(s2.time)


    print(Singleton.time)


