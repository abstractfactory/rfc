"""
Convert Abstract Factory RFC markdown-file into
jekyll-compatible markdown.

File is written to a /jekyll parent directory:
    from    -- /spec1.md
    to      -- /jekyll/1.md

"""

import sublime, sublime_plugin
import rfc_to_jekyll_impl as impl


class ToJekyllCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.run_command('save')
        source_file = self.view.file_name()

        return impl.generate_jekyll_document(source_file)