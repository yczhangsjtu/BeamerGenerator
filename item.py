class Item:

    def __init__(self):
        pass

class TextItem(Item):

    def __init__(self,text):
        self.type = "text"
        self.text = text

    def generate(self):
        texts = self.text.split("\n")
        return "  " + "\n  ".join(texts) + "\n"

class ItemLoader:

    def __init__(self,data):
        if data["type"] == "text":
            self.item = TextItem(data["text"])
        else:
            self.item = None

