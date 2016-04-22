from practice_view import View

class Phone_Book:
	def __init__(self):
		self.view = View()
		self.model = Model()
	def return_or_new(self):
		answer = self.view.return_or_new()
		if answer == "Yes":
			info = self.view.welcome_back()
			check = self.model.return_check(info[0],info[1])
			counter = 0
			while counter < 3 and check == False:
				info = self.view.welcome_back()
				check = self.model.return_check(info[0],info[1])
				counter += 1
			if check == True:
				self.search_db()
			else:
				self.gather_info()
		else:
			self.gather_info()
	def gather_info(self):
		info = self.view.gatherer()
		check = self.model.check_username(info[0])
		while check != None:
			info = self.view.gatherer2()
			check = self.model.check_username(info[0])
		else:
			self.contact_info(info[0],info[1])

	def contact_info(self,username,password):
		contact_info = self.view.contact_info()
		self.model.save_info(contact_info[0],contact_info[1],contact_info[2],username,password)
		self.view.info_saved()
		self.search_db()

	def search_db(self):
		self.view.logged_on()

new = Phone_Book()
new.return_or_new()