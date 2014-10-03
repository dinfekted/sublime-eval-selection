import sublime
import sublime_plugin

from FolderFiles.folder_files import FolderFiles

import os
from os import path
import time

def get_history_path():
  history_path = sublime.packages_path() + '/EvalSelection/history'
  if not path.exists(history_path):
    os.makedirs(history_path)
  return history_path

def add_code_to_history(code):
  filename = get_history_path() + '/' + str(int(time.time())) + '.py'
  io = open(filename, 'w')
  io.write(code)
  io.close()

def run(view, edit):
  for sel in view.sel():
    if sel.size() == 0:
      continue

    code = "import sublime\nimport sublime_plugin\n\n" + view.substr(sel)
    add_code_to_history(code)
    exec(code, {'view': view, 'edit': edit})