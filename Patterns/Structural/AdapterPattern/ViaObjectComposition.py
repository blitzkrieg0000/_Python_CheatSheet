class Target():
    """
        Target, Client kodu tarafından kullanılan alana özgü arayüzü tanımlar.
    """

    def Request(self) -> str:
        return "Target: Varsayılan hedef davranışı."


class Adaptee:
    """
        Adaptee bazı faydalı davranışlar içeriyor, ancak interface mevcut client koduyla uyumlu değil!
        Adaptee'nin client kodunu kullanabilmesi için bazı uyarlamalara ihtiyacı var.
    """
    def SpecificRequest(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target):
    """
        Adapter, Adaptee'nin interfacesini kompozisyon yoluyla Target'in interfacesi ile uyumlu hale getirir.
    """

    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.adaptee.SpecificRequest()[::-1]}"


def ClientCode(target: Target) -> None:
    """
        Client kodu, Hedef arayüzünü takip eden tüm sınıfları destekler.
    """
    print(target.request(), end="")



if __name__ == "__main__":
    print("Client: Target object si ile sorunsuz çalışıyorum:")
    target = Target()
    ClientCode(target)
    print("\n")


    adaptee = Adaptee()
    print("Client: Adaptee sınıfının tuhaf bir arayüzü var." "Anlamıyorum bak: ")
    print(f"Adaptee: {adaptee.SpecificRequest()}", end="\n\n")


    print("Client: Adapter yardımıyla kolayça çevirdim svbnsbnsjbsj:")
    adapter = Adapter(adaptee)
    ClientCode(adapter)








