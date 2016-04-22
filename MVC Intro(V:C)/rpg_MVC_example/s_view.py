class View:
  def __init__(self):
    pass

  def greeting(self):
    hello = input("Hello, do you want to add a contact or find a contact?")
    return hello

  def search_how(self):
    how = input("Do you want to search by name or number?  ")
    return how

  def name_search(self):
    name = input("Please enter the name:  ")
    return name

  def number_search(self):
    number = input("Please enter the number:  ")

  def add_info(self):
    name = input("What is the name:  ")
    number = input("What is the number:  ")
    email = input("What is the email:  ")
    cool = input("Does the contact like Mexican food:  ")
    return (name, number, email, cool)