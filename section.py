from slide import Slide, SlideLoader
class Section:
    
    def __init__(self,title=None):
        self.title = title
        self.slides = []
        self.sections = []

    def generate(self,level):
        ret = ""
        if level == 0:
            label = "section"
        elif level == 1:
            label = "subsection"
        elif level == 2:
            label = "subsubsection"
        else:
            return ""
        if self.title:
            ret += "\\%s{%s}\n"%(label,self.title)
        for slide in self.slides:
            ret += slide.generate()
        if self.title:
            for section in self.sections:
                ret += section.generate(level+1)
        return ret



class SectionLoader:

    def __init__(self,data):
        if "title" in data:
            title = data["title"]
        else:
            title = None
        self.section = Section(title)

        if "slides" in data:
            slides = data["slides"]
            for slide in slides:
                loader = SlideLoader(slide)
                self.section.slides.append(loader.slide)

        if "sections" in data:
            sections = data["sections"]
            for section in sections:
                loader = SectionLoader(section)
                self.section.sections.append(loader.section)
