import sublime
import sublime_plugin
import os

class SetBashSyntaxForDotFilesCommand(sublime_plugin.EventListener):
    def on_load_async(self, view):
        # Load settings
        settings = sublime.load_settings("DotFilesSyntaxSetter.sublime-settings")
        excluded_files = settings.get('excluded_files', [])

        file_name = view.file_name()
        if file_name:
            base_name = os.path.basename(file_name)
            if base_name.startswith('.') and base_name not in excluded_files:
                # Set the syntax to Bash for dotfiles
                view.set_syntax_file('Packages/ShellScript/Shell-Unix-Generic.sublime-syntax')
