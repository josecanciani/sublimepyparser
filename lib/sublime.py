import os
import sublime
from dto import Dto
from config import Config
from pyparser.file.pfile import fromFile

class View(object):
    def __init__(self, sublimeView):
        self.view = sublimeView
        self.config = Config(self)
    def getFileName(self):
        return self.view.file_name()
    def getWindow(self):
        return Window(self.view.window())
    def getPyParserConfig(self):
        return self.config.getPyParserConfig()
    def isValid(self):
        return self.config.isValid()
    def getSelectedText(self):
        sel = self.view.sel()
        if sel:
            region = sel[0]
            return self.view.substr(region)
        return None
    def getClassNameUnderCaret(self):
        return self._getUnderText(sublime.CLASS_WORD_START | sublime.CLASS_WORD_END | sublime.CLASS_PUNCTUATION_START | sublime.CLASS_PUNCTUATION_END | sublime.CLASS_LINE_START | sublime.CLASS_LINE_END | sublime.CLASS_EMPTY_LINE)
    def _getUnderText(self, sublimePointClasses):
        region = self.view.expand_by_class(
            self.view.sel()[0].begin(),
            sublimePointClasses
        )
        return self.view.substr(region)

class Window(object):
    def __init__(self, sublimeWindow):
        self.window = sublimeWindow
    def setStatusMessage(self, message):
        self.window.status_message(message)
    def getFolders(self):
        return self.window.folders()
    def getSymbols(self, symbol, lang):
        symbols = []
        for results in self.window.lookup_symbol_in_index(symbol):
            splitted = os.path.splitext(results[0])
            if splitted and len(splitted) == 2 and splitted[1][1:] == lang:
                symbolDto = Symbol()
                symbolDto.symbol = symbol
                symbolDto.fullPath = results[0]
                symbolDto.shortPath = results[1]
                symbolDto.line = results[2][0]
                symbolDto.col = results[2][1]
                symbols.append(symbolDto)
        return symbols
    def getClassSymbols(self, className, lang):
        classes = []
        for symbol in self.getSymbols(className, lang):
            file = fromFile(symbol.fullPath)
            for pclass in file.getClasses():
                if pclass.getName() == className:
                    classes.append(symbol)
        return classes


class Symbol(Dto):
    def __init__(self):
        super(Symbol, self).__init__({
            'symbol': None,
            'fullPath': None,
            'shortPath': None,
            'line': None,
            'col': None
        })
