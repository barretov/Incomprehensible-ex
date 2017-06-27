import os
import sublime
import subprocess
import sublime_plugin

class IncomprehensibleEx (sublime_plugin.EventListener):

    print("** Incomprehensible Extensions Started **")

    # known extensions
    extensions = ['docx', 'epub', 'odt']
    # mode
    editMode = True

    # load Inconprehensible Ex user settings
    fileSettings = sublime.load_settings('incomprehensibleex.sublime-settings')

    # set Inconprehensible Ex user settings if removed
    if not fileSettings.has('extensions'):
        fileSettings.set('extensions', extensions)
    else:
        extensions = fileSettings.get('extensions')

    if not fileSettings.has('edit_mode'):
        fileSettings.set('edit_mode', editMode)
    else:
        editMode = fileSettings.get('edit_mode')

    sublime.save_settings('incomprehensibleex.sublime-settings')

    # listeners
    def on_load(self, view):
        if sublime.active_window().extract_variables()['file_extension'] in self.extensions:
            self.handle_active(view)

    def on_pre_close(self, view):
        if not (view.is_scratch()):
            if sublime.active_window().extract_variables()['file_extension'] == 'inex':
                self.deleteTemp(view)

    def on_post_save(self, view):
        if not (view.is_scratch()):
            if sublime.active_window().extract_variables()['file_extension'] == 'inex':
                self.saveTemp(self)

    # function to set the variables
    def initVariables(self, view):
        self.path = sublime.active_window().extract_variables()['file_path']
        self.file = sublime.active_window().extract_variables()['file_name']
        self.ext = sublime.active_window().extract_variables()['file_extension']
        self.target = os.path.join(os.path.realpath(sublime.packages_path()), "User")

    # Function for delete temporary file
    def deleteTemp(self, view):
        self.initVariables(view)
        # delete temp file
        os.remove(os.path.join(self.path, self.file))

    # Function to save the temp file in original file
    def saveTemp(self, view):
        try:
            self.initVariables(view)
            # set file paths to input and output
            inp = os.path.join(self.path, self.file)
            out = os.path.join(self.path, self.file[:-5])
            # set original extension
            ext = self.file.find('.')
            ext = self.file[ext+1:-5]
            # convert file
            self.convert(self, inp, out, ext)
        except Exception as error:
            print(error)

    # Function to convert file
    def convert(self, view, inp, out, ext):
        try:
            result, errors = subprocess.Popen('pandoc -s -o '+out+' -w '+ext+' '+inp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        except Exception as error:
            print(error)

    # Function for process the file
    def handle_active(self, view):
        try:
            # set common variables
            self.initVariables(view)
            # close original docx file opened
            sublime.active_window().run_command('close')

            # verify if it's editable
            if not self.editMode:

                # set file paths to input and output
                inp = os.path.join(self.path, self.file)
                out = os.path.join(self.target, self.file)
                # convert file
                self.convert(self, inp, out, 'plain')

                # create new file to recive the text
                output_view = sublime.active_window().new_file()
                output_view.set_name(self.file)
                output_view.set_scratch(True)

                # open,read and close the file converted
                file = open(os.path.join(self.target, self.file), 'r')
                text = file.read()
                file.close()

                # remove converted file
                os.remove(os.path.join(self.target, self.file))
                #  past data in the new file
                output_view.run_command("insert",{"characters": text})
                #  move the cursor to the top of the page
                output_view.run_command("move_to",{"to": "bof"})
            else:
                # set file paths to input and output
                inp = os.path.join(self.path, self.file)
                out = os.path.join(self.path, self.file+'.inex')
                # convert file
                self.convert(self, inp, out, 'plain')
                # open new file
                sublime.active_window().open_file(os.path.join(self.path, self.file)+'.inex')
        except KeyError as error:
            print(error)

class IncomprehensibleExEditModeOnCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        try:
            IncomprehensibleEx.editMode = True
            IncomprehensibleEx.fileSettings.set('edit_mode', True)
            sublime.active_window().status_message("Incomprehensible Ex | Edit Mode ON")
        except Exception as e:
            print(e)

class IncomprehensibleExEditModeOffCommand(sublime_plugin.ApplicationCommand):

    def run(self):
        try:
            IncomprehensibleEx.editMode = False
            IncomprehensibleEx.fileSettings.set('edit_mode', False)
            sublime.active_window().status_message("Incomprehensible Ex | Edit Mode OFF")
        except Exception as e:
            print(e)
