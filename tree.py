import sublime, sublime_plugin
from .lib.common import *
from .lib.sublime import View
from pyparser.tool.extensiontreeprinter import ExtensionTreePrinter

class SublimepyparserTree(sublime_plugin.TextCommand):
    def run(self, edit):
        self.myView = View(self.view)
        if not self.myView.isValid():
            return
        self.className = self.myView.getSelectedText() or self.myView.getClassNameUnderCaret()
        if not self.className:
            self.myView.getWindow().setStatusMessage('**** Cannot detect a class name')
        tree = ExtensionTreePrinter(self.myView.getPyParserConfig(), self.className, self.onComplete, self.onError)
        sublime.status_message('Calculating tree for ' + self.className + '...')

    def onComplete(self, tree):
        self.myView.getWindow().setStatusMessage('Completed tree calculation for ' + self.className)
        viewToPrintResults = sublime.active_window().new_file()
        viewToPrintResults.set_name('ClassTree_' + self.className + '.txt')
        viewToPrintResults.set_scratch(True)
        viewToPrintResults.run_command("editor_view_writer", {"text": tree.get()})

    def onError(self, err):
        self.myView.getWindow().setStatusMessage('**** Error finding tree for ' + self.className + '. See console for details.')
        raise err


