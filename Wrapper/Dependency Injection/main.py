class TextFile:
    def SaveText(self):
        print("Dosya Kaydedildi.")


class SaveDatabase:
    def SaveText(self):
        print("Dosya Kaydedildi.")


class Window():
    def __init__(self, storage:TextFile):
        self.text = ""
        self._storage = storage


    def WriteText(self, text):
        self.text += text


    #! Text Gösterme işlemi yapıyor.
    def ShowWindow(self):
        print("\n<- Metin ->\n")
        print(self.text)


    #! Dosya işlemi yapıyor
    def SaveText(self):
        self._storage.SaveText(self.text)



if '__main__' == __name__:
    storage = TextFile()
    w = Window(storage)

    #! Dependecy Injection ile aynı işi farklı şekilde yapan obje ile çalıştık.
    # database = SaveDatabase()
    # w = Window(database)


    w.WriteText("Merhaba")

    w.ShowWindow()

    w.SaveText()