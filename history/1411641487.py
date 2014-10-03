import sublime
import sublime_plugin

print(sublime.find_resources("*.sublime-keymap")[:10])