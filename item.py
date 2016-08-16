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

class FigureItem(Item):

    def __init__(self,path):
        self.type = "figure"
        self.path = path
        self.scale = 1.0

    def generate(self):
        ret = ""
        ret += "  \\begin{figure}\n"
        ret += "    \\scalebox{%f}{\\includegraphics{%s}}\n"%(self.scale,self.path)
        ret += "  \\end{figure}\n"
        return ret

class ItemLoader:

    def __init__(self,data):
        if data["type"] == "text":
            self.item = TextItem(data["text"])
        elif data["type"] == "figure":
            self.item = FigureItem(data["path"])
            if "scale" in data:
                self.item.scale = data["scale"]
        else:
            self.item = None

