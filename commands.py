import sublime
import sublime_plugin

from EvalSelection import eval_selection
from FolderFiles.folder_files import FolderFiles

class EvalSelection(sublime_plugin.TextCommand):
  def run(self, edit):
    eval_selection.run(self.view, edit)

class ShowEvalSelectionHistory(sublime_plugin.TextCommand):
  def run(self, edit):
    path, name = eval_selection.get_history_path(), [['eval_selection', self]]
    FolderFiles(path, None, False, 'EvalSelection', callers = name).show()