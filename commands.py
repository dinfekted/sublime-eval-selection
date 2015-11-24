import sublime
import sublime_plugin

try:
  from EvalSelection import eval_selection
  from FolderFiles.folder_files import FolderFiles
except ImportError as error:
  sublime.error_message("Dependency import failed; please read readme for " +
   "EvalSelection plugin for installation instructions; to disable this " +
   "message remove this plugin; message: " + str(error))
  raise error


class EvalSelection(sublime_plugin.TextCommand):
  def run(self, edit):
    eval_selection.run(self.view, edit)

class ShowEvalSelectionHistory(sublime_plugin.TextCommand):
  def run(self, edit):
    path, name = eval_selection.get_history_path(), [['eval_selection', self]]
    FolderFiles(path, None, False, 'EvalSelection', callers = name).show()