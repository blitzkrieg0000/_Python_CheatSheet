from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List



# =================================================================================================================== #
#! Publisher = Subject = Streamer = EventManager                                                                      #
# =================================================================================================================== #
class IPublisher(ABC):
    @abstractmethod
    def Attach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def Detach(self, observer: IObserver) -> None:
        pass

    @abstractmethod
    def Publish(self) -> None:
        pass


class Publisher(IPublisher):
    # Tutulan önemli bir değer olsun
    _state: int = None

    # Abone olan Observer(Gözlemci) listesi
    _observers: List[IObserver] = []

    # Gelen gözlemciyi abone listesine ekle
    def Attach(self, observer: IObserver) -> None:
        print("Publisher: Bir gözlemci abone edildi.")
        self._observers.append(observer)


    # Gelen gözlemciyi abone listesinden çıkar
    def Detach(self, observer: IObserver) -> None:
        self._observers.remove(observer)


    # Eğer tutulan önemli değerde(_state) değişiklik olursa tüm abonelerin update metodunu çağırarak, aboneleri bilgilendir.
    def Publish(self) -> None:
        print("Publisher: Gözlemciler bilgilendiriliyor...")
        for observer in self._observers:
            observer.Update(self)


    # Çeşitli işlemler yapılıyor...
    def DoAWork(self) -> None:
        print("\nPublisher: Önemli işler yapıyor... _state'i güncelliyor.")
        self._state = randrange(0, 10)

        print(f"Publisher: Herkese _state'in değiştirildiği duyuruluyor: {self._state}")
        self.Publish()



# =================================================================================================================== #
#! Observer = Client = Subscriber = Gözlemci                                                                          #
# =================================================================================================================== #
class IObserver(ABC):
    """
        Observer interface, kullanıcılar tarafından kullanılan güncelleme yöntemini bildirir.
        Her gözlemcinin(observer) update metoduna sahip olması gerekliliğini sağlar.
    """
    @abstractmethod
    def Update(self, publisher: Publisher) -> None:
        """
        Receive update from subject.
        """
        pass


# Gözlemci 1
class ObserverA(IObserver):
    def Update(self, publisher: Publisher) -> None:
        print("\n=> Observer A :\n",
            publisher._state
        )

# Gözlemci 2
class ObserverB(IObserver):
    def Update(self, publisher: Publisher) -> None:
        print("\n=> Observer B :\n",
            publisher._state
        )


if __name__ == "__main__":
    publisher = Publisher()

    observer_a = ObserverA()
    observer_b = ObserverB()
    publisher.Attach(observer_a)
    publisher.Attach(observer_b)

    publisher.DoAWork()
    publisher.DoAWork()

    publisher.Detach(observer_a)

    publisher.DoAWork()