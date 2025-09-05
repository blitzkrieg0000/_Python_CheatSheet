from __future__ import annotations
from abc import ABC


class IMediator(ABC):
    """
    Mediator interfacesi, componentleri bilgilendirmek için kullanılan bir metodu bildirir.
    Mediator gelen olaylara tepki verebilir ve yürütmeyi diğer componentlere aktarır.
    """
    def Notify(self, sender: object, event: str) -> None:
        pass


class Mediator(IMediator):
    def __init__(self, component1: Component1, component2: Component2) -> None:
        """
            Mediator tüm bağımlılıkları bilmelidir. Belirli bir yerden sonra tüm sorumlulukları mediatora yüklemek,
            Mediator'un god object olmasına yol açar ve Single Responsibility çiğnenmiş olur.
        """
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def Notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator => A")
            self._component2.WorkC()
        elif event == "D":
            print("Mediator => D")
            self._component1.WorkB()
            self._component2.WorkC()


class BaseComponent():
    def __init__(self, mediator: IMediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> IMediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: IMediator) -> None:
        self._mediator = mediator



class Component1(BaseComponent):
    def WorkA(self) -> None:
        print("Component 1 => Work A.")
        self.mediator.Notify(self, "A")

    def WorkB(self) -> None:
        print("Component 1 => Work B.")
        self.mediator.Notify(self, "B")


class Component2(BaseComponent):
    def WorkC(self) -> None:
        print("Component 2 => Work C.")
        self.mediator.Notify(self, "C")

    def WorkD(self) -> None:
        print("Component 2 => Work D.")
        self.mediator.Notify(self, "D")



if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = Mediator(c1, c2)

    print("Client A.")
    c1.WorkA()

    print()

    print("Client B.")
    c2.WorkD()