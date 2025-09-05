class Target():
    """
        Target, Client kodu tarafından kullanılan alana özgü arayüzü tanımlar.
    """

    def Request(self) -> str:
        return "Target: Varsayılan hedef davranışı."


class Adaptee():
    """
        Adaptee bazı faydalı davranışlar içeriyor, ancak interface mevcut client koduyla uyumlu değil!
        Adaptee'nin client kodunu kullanabilmesi için bazı uyarlamalara ihtiyacı var.
    """
    def SpecificRequest(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
        Adapter, multiple inheritance yoluyla Adaptee'nin interfacesini, Targetin interface'i ile uyumlu hale getirir.
    """

    def Request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.SpecificRequest()[::-1]}"


def ClientCode(target: Target) -> None:
    """
        Client kodu, Hedef arayüzünü takip eden tüm sınıfları destekler.
    """
    print(target.Request(), end="")



if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    ClientCode(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. " "See, I don't understand it:")
    print(f"Adaptee: {adaptee.SpecificRequest()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    ClientCode(adapter)