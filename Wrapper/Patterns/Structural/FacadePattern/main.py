from __future__ import annotations


class Facade():
    """
        Facade bir ya da bir kaç alt sisteme temel bir interface sağlar.
        Facade, istemci isteklerini alt sistem içindeki uygun nesnelere devreder.
        Facade ayrıca yaşam döngülerinin yönetilmesinden de sorumludur. 
        Bütün bunlar istemciyi alt sistemin istenmeyen karmaşıklığından korur.
    """

    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        """
            Uygulamanızın ihtiyaçlarına bağlı olarak Facade'e mevcut alt sistem nesnelerini sağlayabilir
            veya Facade'i bunları kendi başına oluşturmaya zorlayabilirsiniz.        
        """
        self._subsystem1 = subsystem1 or Subsystem1()
        self._subsystem2 = subsystem2 or Subsystem2()


    def Operation(self) -> str:
        """
            Facade'in yöntemleri, alt sistemlerin gelişmiş işlevselliğine yönelik kullanışlı kısayollardır.
            Ancak istemciler bir alt sistemin yeteneklerinin yalnızca küçük bir kısmına sahip olurlar
        """
        results = []
        results.append("Facade subsystem leri başlatır:")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation1())
        results.append("Facade subsystems lere görev emri verir:")
        results.append(self._subsystem1.operation_n())
        results.append(self._subsystem2.operation_z())
        return "\n".join(results)


class Subsystem1():
    """
        Subsystemler, istekleri doğrudan cepheden veya clienttan kabul edebilir.
        Her durumda, Alt Sistem için Cephe başka bir istemcidir ve Alt Sistemin bir parçası değildir.
    """

    def operation1(self) -> str:
        return "Subsystem1: Hazır!"

    # ...

    def operation_n(self) -> str:
        return "Subsystem1: İleri!"


class Subsystem2():
    """
        Bazı facade'ler aynı anda birden fazla alt sistemle çalışabilmektedir.
    """

    def operation1(self) -> str:
        return "Subsystem2: Hazır ol!"

    # ...

    def operation_z(self) -> str:
        return "Subsystem2: Ateş!"


def HQ(facade: Facade) -> None:
    """
        İstemci kodu, Facade tarafından sağlanan basit bir arayüz aracılığıyla karmaşık alt sistemlerle çalışır.
        Bir facade subsystem in yaşam döngüsünü yönettiğinde client alt sistemin varlığından bile haberdar olmayabilir.
        Bu yaklaşım karmaşıklığı kontrol altında tutmanıza olanak tanır
    """
    print(facade.Operation(), end="")


if __name__ == "__main__":
    # Facade'in yeni nesneler oluşturmasına izin vermek yerine varolan nesneleri kullanması istenebilir.
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)

    HQ(facade)
