# plots.py

class StyleIterator:
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
    
    def next_style(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result
