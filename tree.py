import sublime, sublime_plugin
from .lib.common import *
from .lib.sublime import View
from pyparser.tool.extensiontreeprinter import ExtensionTreePrinter, ExtensionFullTreePrinter

class SublimepyparserTree(sublime_plugin.TextCommand):
    def run(self, edit):
        self.myView = View(self.view)
        if not self.myView.isValid():
            return
        settings = sublime.load_settings('sublimepyparser.sublime-settings').get('tree')
        self.childLimit = settings['childLimit']
        self.processParents = settings['processParents']
        self.className = self.myView.getSelectedText() or self.myView.getClassNameUnderCaret()
        if not self.className:
            self.myView.getWindow().setStatusMessage('**** Cannot detect a class name')
        if self.processParents:
            tree = ExtensionFullTreePrinter(self.myView.getPyParserConfig(), self.className, self.onComplete, self.onError)
        else:
            tree = ExtensionTreePrinter(self.myView.getPyParserConfig(), self.className, self.onComplete, self.onError)
        sublime.status_message('Calculating tree for ' + self.className + '...')

    def onComplete(self, tree):
        self.myView.getWindow().setStatusMessage('Completed tree calculation for ' + self.className)
        viewToPrintResults = sublime.active_window().new_file()
        viewToPrintResults.set_name(self.className + '.txt')
        viewToPrintResults.set_scratch(True)
        viewToPrintResults.run_command("editor_view_writer", {
            "text": self._getHeader() + tree.get() + self._getFooter()
        })

    def _getHeader(self):
        head = "Results for class " + self.className + "\n"
        head += "  Properties (change them in SublimePyParser User Preference file):\n"
        head += "  tree.childLimit: " + str(self.childLimit) + " (max extensions per class to process)\n"
        head += "  tree.processParents: " + ('yes' if self.processParents else 'no') + " (include selected class parents, to build full tree -may take long-)\n"
        return head + "\n\n"


    def _getFooter(self):
        return "\n"

    def onError(self, err):
        self.myView.getWindow().setStatusMessage('**** Error finding tree for ' + self.className + '. See console for details.')
        raise err


