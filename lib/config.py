import os
import sublime
from pyparser.config import Config as PyParserConfig

class Config(object):
    def __init__(self, view):
        self.valid = True
        self.view = view
        if self.view.getFileName():
            self._createPyParserConfig()
        else:
            self.valid = False
            self._markInvalid('Current file is not saved. It needs valid extension (php or js).')

    def isValid(self):
        return self.valid

    def getPyParserConfig(self):
        return self.pyparserConfig

    def _markInvalid(self, statusMessage):
        self.view.getWindow().setStatusMessage('**** ' + statusMessage)
        self.valid = False
        return None

    def _createPyParserConfig(self):
        # get current lang
        splitted = os.path.splitext(self.view.getFileName())
        if not splitted or len(splitted) != 2 or splitted[1][1:] not in ['js', 'php']:
            return self._markInvalid('Cannot detect lang in your current opened file. Be sure it has a valid extension (php or js).')
        lang = splitted[1][1:]
        openedFolders = self.view.getWindow().getFolders()
        if not openedFolders or len(openedFolders) == 0:
            return self._markInvalid('No folder found in current window. This plugin cannot work without one configured.')
        folder = openedFolders[0] # FIXME: support multiple folders
        self.pyparserConfig = PyParserConfig(self._getFileNameFromClassName, folder, lang)

    def _getFileNameFromClassName(self, className, lang, namespace):
        for aclass in self.view.getWindow().getClassSymbols(className, lang):
            return aclass.fullPath
        return None

