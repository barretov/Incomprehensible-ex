import sublime
import sublime_plugin
import os
import subprocess

class iconExtesions (sublime_plugin.EventListener):

    print("* Incomprehensible Extensions Started ...")

    # listeners
    def on_load_async(self, view):
        if (sublime.active_window().extract_variables()['file_extension'] == 'docx'):
            self.handle_active(view)

    def on_pre_close(self, view):
        if (sublime.active_window().extract_variables()['file_extension'] == 'ofdsc'):
            self.deleteTemp(view)

    def on_post_save(self, view):
        if (sublime.active_window().extract_variables()['file_extension'] == 'ofdsc'):
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
            out = os.path.join(self.path, self.file[:-6])
            ext = "docx"
            self.convert(self, inp, out, ext)
        except Exception as error:
            print(error)

    # Function to convert file
    def convert(self, view, inp, out, ext):
        try:
            result, errors = subprocess.Popen('pandoc -o '+out+' -w '+ext+' '+inp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
        except Exception as error:
            print(error)

    # Function for process the file
    def handle_active(self, view):
        try:
            self.initVariables(view)
            sublime.active_window().run_command('close')

            # verificar se está marcado somente como visualizaçao
            if (False):

                # set file paths to input and output
                inp = os.path.join(self.path, self.file)
                out = os.path.join(self.target, self.file)
                ext = "plain"
                # # convert file
                self.convert(self, inp, out, ext)

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
                out = os.path.join(self.path, self.file+'.ofdsc')
                ext = "plain"
                # convert file
                self.convert(self, inp, out, ext)
                # open new file
                sublime.active_window().open_file(os.path.join(self.path, self.file)+'.ofdsc')
        except KeyError as error:
            print(error)
