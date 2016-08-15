from section import Section, SectionLoader

class Beamer:

    def __init__(self,title):
        self.title = title

        self.author = None
        self.theme = None
        self.institute = None
        self.packages = ["lmodern"]
        self.sections = []

        self.hastable = True

    def generate(self):
        ret = ""
        ret += "\\documentclass{beamer}\n"
        if self.theme:
            ret += "\\usetheme{%s}\n"%self.theme
        for package in self.packages:
            ret += "\\usepackage{%s}\n"%package
        if self.title:
            ret += "\\title{%s}\n"%self.title
        if self.institute:
            ret += "\\institute{%s}\n"%self.institute
        if self.author:
            ret += "\\author{%s}\n"%self.author
        ret += "\\begin{document}\n"
        ret += "\\begin{frame}\n  \\titlepage\n\\end{frame}\n"
        if self.hastable:
            ret += "\\begin{frame}\n  \\frametitle{Outline}\n  \\tableofcontents\n\\end{frame}\n"
        for section in self.sections:
            ret += section.generate(0)
        ret += "\\end{document}\n"

        return ret



class BeamerLoader:

    def __init__(self,data):
        self.beamer = Beamer(data["title"])
        if "author" in data: self.beamer.author = data["author"]
        if "theme" in data: self.beamer.theme = data["theme"]
        if "institute" in data: self.beamer.institute = data["institute"]
        if "packages" in data: self.beamer.packages = data["packages"]
        if "hastableofcontent" in data: self.hastable = data["hastableofcontent"]
        if "sections" in data:
            sections = data["sections"]
            for section in sections:
                loader = SectionLoader(section)
                self.beamer.sections.append(loader.section)
