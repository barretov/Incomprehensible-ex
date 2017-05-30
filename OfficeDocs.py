import sublime
import sublime_plugin
import zipfile
import os


class officeDocs (sublime_plugin.EventListener):

	path = 'none'
	file = 'none'

    # show init message
	sublime.active_window().status_message("Office Docs | Started")

    # show console message
	print("............::::::::| Office Docs | Started |::::::::............")

	#  listeners  #
	def on_load_async(self, view):
		# print(view.file_name)

		# view.set_scratch(True)
		self.handle_active(view)
		# view.window().run_command('close')
		# view.erase(view, view.visible_region())
		# print(view.find_all("[\t ]+$"))
		# view.erase(edit, view.find_all("[\t ]+$"))

	def on_clone_async(self, view):
		self.handle_active()

	# def on_new_async(self, view):

	# def on_post_save(self, view):

	# def on_close(self, view):
		# self.handle_active(view)
	# def on_modified(self, view):

	# controller
	def handle_active(self, view):

		try:

			active = sublime.active_window().extract_variables()
			self.path = active['file_path']
			self.file = active['file_name']
			self.ext  = active['file_extension']

			if (active['file_extension'] == 'docx'):

				print(self.path)

				zip_ref = zipfile.ZipFile(os.path.join(self.path, self.file), 'r')
				zip_ref.extractall(os.path.join(self.path, 'tempdoc'))
				zip_ref.close()

				# view.window().new_file()
				# view.window().run_command('close')
				sublime.active_window().run_command('close')
				print(sublime.active_window().open_file('tempdoc'+'/content.xml'))


				# self.original_file['name'] = sublime.active_window().extract_variables()['file_base_name']
				# self.original_file['ext'] = sublime.active_window().extract_variables()['file_extension']
				# print(sublime.active_window().extract_variables()['file_base_name'])
				# print(sublime.active_window().extract_variables()['file_extension'])

		except KeyError as error:
			sublime.active_window().status_message("Erros!")
			# print("CodeTimeTracker | You are working out of project. Make a project")
