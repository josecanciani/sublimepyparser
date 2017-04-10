import sublime, sublime_plugin
from .lib.config import Config
from pyparser.tool.extensiontreeprinter import ExtensionTreePrinter

class SublimepyparserTree(sublime_plugin.TextCommand):
    def run(self, edit):
        self.className = self.getSelectedText() or self.getUnderText()
        if not self.className:
            sublime.status_message('**** Cannot detect a class name')
        config = Config(sublime.active_window(), self.view)
        tree = ExtensionTreePrinter(config.getPyParserConfig(), self.className, self.onComplete, self.onError)
        sublime.status_message('Calculating tree for ' + self.className + '...')

    def onComplete(self, tree):
        sublime.status_message('Completed tree calculation for ' + self.className)
        print(tree.get())

    def onError(self, err):
        sublime.status_message('**** Error finding tree for ' + self.className + '. See console for details.')
        raise err

    def getSelectedText(self):
        sel = self.view.sel()
        if sel:
            region = sel[0]
            return self.view.substr(region)
        return None

    def getUnderText(self):
        region = self.view.expand_by_class(
            self.view.sel()[0].begin(),
            sublime.CLASS_WORD_START | sublime.CLASS_WORD_END | sublime.CLASS_PUNCTUATION_START | sublime.CLASS_PUNCTUATION_END | sublime.CLASS_LINE_START | sublime.CLASS_LINE_END | sublime.CLASS_EMPTY_LINE
        )
        return self.view.substr(region)

