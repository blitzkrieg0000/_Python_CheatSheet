from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Context():
    """
        Clientların ilgilendiği contexi tanımlar.
    """
    def __init__(self, strategy: Strategy) -> None:
        """
            Genellikle context objesi stratejileri bir constructor yardımıyla tanımlar ya da runtime da setter ile değiştirir.
        """
        self._strategy = strategy


    @property
    def strategy(self) -> Strategy:
        """
        Context, Strateji nesnelerinden birinin referansı yönetir.
        Context objesi diğer stratejilerden haberdar değildir. 
        Sadece bir interface yardımı haberdar olduğu strateji objelerinin metodunu çalıştırır.
        """
        return self._strategy


    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Context objesi runtime da stratejiyi değiştirebilir.
        """

        self._strategy = strategy


    def DoWork(self) -> None:
        """
            Bağlam, bazı işleri Strateji nesnesine devreder.
            algoritmanın birden fazla versiyonunu kendi başına uygular.
        """
        print("Context: Strateji bilinmeksizin context verilen işi yapıyor. Strateji runtimeda değişebilir.")
        result = self._strategy.XAlgorithmWork(["a", "b", "c", "d", "e"])
        print(",".join(result))



class Strategy(ABC):
    """
        Strateji arayüzü, desteklenen tüm sürümlerde bazı algoritmaların ortak olan işlemlerini bildirir.
        Context, Stratejiler tarafından tanımlanan algoritmayı çağırmak için bu arayüzü kullanır.
    """
    @abstractmethod
    def XAlgorithmWork(self, data: List):
        pass


"""
    Somut Strateji Classları, temel Stratejiyi takip ederken algoritmayı uygular.
    Arayüz, bunları Context'te değiştirilebilir hale getirir.
"""
class StrategyA(Strategy):
    def XAlgorithmWork(self, data: List) -> List:
        return sorted(data)


class StrategyB(Strategy):
    def XAlgorithmWork(self, data: List) -> List:
        return reversed(sorted(data))


if __name__ == "__main__":
    """
        Client bir yöntem belirleyerek Contexi ayağa kaldırır.
    """

    context = Context(StrategyA())
    context.DoWork()
    
    print()

    # Runtime da yeni bir strateji ile benzer işi gerçekleştiriyoruz.
    # Dikkat edilirse context objesindeki değişkenler aynı ancak metodun yapıldığı ve benzer iş farklı bir classta tanımlanıyor.
    context.strategy = StrategyB()
    context.DoWork()