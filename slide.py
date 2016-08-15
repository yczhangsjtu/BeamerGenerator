from item import Item, ItemLoader
class Slide:

    def __init__(self,title=None):
        self.title = title
        self.items = []

    def generate(self):
        ret = ""
        ret += "\\begin{frame}\n"
        if self.title:
            ret += "  \\frametitle{%s}\n"%self.title
        for item in self.items:
            ret += item.generate()
        ret += "\\end{frame}\n"
        return ret


class SlideLoader:

    def __init__(self,data):
        if "title" in data:
            title = data["title"]
        else:
            title = None
        self.slide = Slide(title)

        if "items" in data:
            items = data["items"]
            for item in items:
                loader = ItemLoader(item)
                self.slide.items.append(loader.item)

