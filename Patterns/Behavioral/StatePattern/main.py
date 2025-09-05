from __future__ import annotations

from abc import ABC, abstractmethod


class Context():
    _state = None

    def __init__(self, state: State) -> None:
        self.ChangeBehaviourTo(state)

    def ChangeBehaviourTo(self, state: State):
        """
            Context, runtime'da state nesnesinin değiştirilmesine izin verir.
        """
        print(f"Context Değiştiriliyor: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def Work1(self):
        self._state.Handle1()

    def Work2(self):
        self._state.Handle2()



class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def Handle1(self) -> None:
        pass

    @abstractmethod
    def Handle2(self) -> None:
        pass



class StateA(State):
    def Handle1(self) -> None:
        print("StateA => Work1")
        print("StateA Contexi şunla değiştirmek istiyor: StateB")
        self.context.ChangeBehaviourTo(StateB())

    def Handle2(self) -> None:
        print("StateA => Work2")



class StateB(State):
    def Handle1(self) -> None:
        print("StateB => Work1")

    def Handle2(self) -> None:
        print("StateB => Work2")
        print("StateB Contexi şunla değiştirmek istiyor: StateA")
        self.context.ChangeBehaviourTo(StateA())


if __name__ == "__main__":
    # Bir context nesnesi oluştur ve "StateA" ile işe başla
    context = Context(StateA())

    # StateA, Work 1'i gerçekleştir ve StateB ye contex'i değiştir.
    context.Work1()

    # StateB, Work 2'yi gerçekleştir ve StateA ya contex'i değiştir.
    context.Work2()



