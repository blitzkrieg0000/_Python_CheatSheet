from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):
    """
        Temel Component class'ı, bir işin hem basit hem de karmaşık nesneleri için ortak işlemleri bildirir.
    """
    @property
    def parent(self) -> Component:
        return self._parent

    @parent.setter
    def parent(self, parent: Component):
        """
            İsteğe bağlı olarak, temel Component(Bileşen), bir ağaç yapısındaki bileşenin üst öğesinin ayarlanması ve bu öğeye erişim için bir interface bildirebilir.
            Ayrıca bu yöntemler için bazı varsayılan uygulamaları da sağlayabilir.
        """

        self._parent = parent


    """
        Bazı durumlarda alt yönetim işlemlerini doğrudan temel Component sınıfında tanımlamak yararlı olabilir.
        Bu şekilde, nesne ağacı derlemesi sırasında bile herhangi bir somut bileşen sınıfını client koduna maruz bırakmanıza gerek kalmaz.
        *Dezavantajı ise bu yöntemlerin yaprak düzeyindeki bileşenler için boş olmasıdır.
    """
    def add(self, component: Component) -> None:
        ...


    def remove(self, component: Component) -> None:
        ...


    def IsComposite(self) -> bool:
        """
            Client kodunun bir bileşenin çocuk yaratıp yaratmayacağını anlamasına olanak tanıyan bir yöntem sağlayabilirsiniz.
        """
        return False


    @abstractmethod
    def Operation(self) -> str:
        """
            Temel Bileşen bazı varsayılan davranışları uygulayabilir veya bunu somut sınıflara bırakabilir
            (davranışı içeren yöntemi "abstract" olarak bildirerek).
        """
        ...



class Leaf(Component):
    """
        Leaf(Yaprak) sınıfı bir kompozisyonun son nesnelerini temsil eder. Bir yaprağın çocuğu olamaz.
        !Genellikle asıl işi yapanlar Leaf nesneleridir, oysa Composite nesneler yalnızca alt bileşenlerine yetki verir.
        ? Ancak Compositeler de iş yapabilir.
    """

    def Operation(self) -> str:
        return "Leaf"


class Composite(Component):
    """
        Composite sınıfı, çocukları olabilecek karmaşık componentleri(bileşenleri) temsil eder
        Genellikle, Bileşik nesneler asıl işi çocuklarına devreder ve ardından sonucu "özetler".
    """
    def __init__(self) -> None:
        self._children: List[Component] = []


    """
        Composite(Bileşik) bir nesne, alt listesine başka bileşenler (hem basit hem de karmaşık) ekleyebilir veya çıkarabilir.
    """
    def add(self, component: Component) -> None:
        self._children.append(component)
        component.parent = self


    def remove(self, component: Component) -> None:
        self._children.remove(component)
        component.parent = None


    def IsComposite(self) -> bool:
        return True


    def Operation(self) -> str:
        """
            Bileşik birincil mantığını belirli bir şekilde yürütür.
            Tüm alt öğelerini yinelemeli olarak dolaşır, sonuçlarını toplar ve toplar.
            Composite'in (bileşimin) çocukları bu çağrıları kendi çocuklarına vb. ilettiğinden, sonuç olarak tüm nesne ağacı dolaşılır.
        """
        results = []
        for child in self._children:
            results.append(child.Operation())
        return f"Branch({'+'.join(results)})"


def ClientCode(component: Component) -> None:
    """
        Client kodu, temel arayüz aracılığıyla tüm bileşenlerle çalışır.
    """
    print(f"RESULT: {component.Operation()}", end="")


def ClientCode2(component1: Component, component2: Component) -> None:
    """
        Alt yönetim işlemlerinin Temel Component sınıfında bildirilmesi sayesinde client kodu,
        somut sınıflarına bağlı olmaksızın basit veya karmaşık herhangi bir component(bileşenle) çalışabilir.
    """
    if component1.IsComposite():
        component1.add(component2)

    print(f"RESULT: {component1.Operation()}", end="")


if __name__ == "__main__":
    # Bu şekilde istemci kodu basit yaprak bileşenlerini destekleyebilir...
    simple = Leaf()
    print("Client: Temel bir bileşenim var:")
    ClientCode(simple)
    print("\n")

    # ...aynı zamanda karmaşık composite'ler(bileşenler).
    tree = Composite()

    branch1 = Composite()
    branch1.add(Leaf())
    branch1.add(Leaf())

    branch2 = Composite()
    branch2.add(Leaf())

    tree.add(branch1)
    tree.add(branch2)


    print("Client: Composite Ağacım var.")
    ClientCode(tree)
    print("\n")


    print("Client: Ağacı yönetirken bile bileşen(component) sınıflarını kontrol etmeme gerek yok:")
    ClientCode2(tree, simple)