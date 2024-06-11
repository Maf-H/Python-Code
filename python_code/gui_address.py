# @author Mesfin Haftu && Paul Dietel
# Date and Time 14/04/2024, 11:44 pm.
# Inserts into, updates and searches a database
from tkinter.messagebox import *

import MySQLdb
from tkinter import *
import Pmw

class AddressBook(Frame):
	""" GUI Database Address Book Frame """

	def __init__(self):
		"""Address Book constructor"""
		Frame.__init__(self)
		Pmw.initialise()
		self.pack(expand = YES, fill = BOTH)
		self.master.title("Address Book Database Application")
		# buttons to execute commands
		self.buttons = Pmw.ButtonBox(self, padx = 0)
		self.buttons.grid(columnspan = 2)
		self.buttons.add("Find", command = self.find_address)
		self.buttons.add("Add", command = self.add_address)
		self.buttons.add("Update", command = self.update_address)
		self.buttons.add("Clear", command = self.clear_contents)
		self.buttons.add("Help", command = self.help, width = 14)
		self.buttons.alignbuttons()
		# list of fields in an address record
		fields = ["id", "first_name", "last_name",
				  "address", "city", "state", "postal_code",
				  "country", "email", "phone"]

		# dictionary with Entry components for values, keyed by
		# corresponding addresses table field names
		self.entries = {}
		self.IDEntry = StringVar()
		# current address id text
		self.IDEntry.set("")
		# create entries for each field
		for i in range(len(fields)):
			label = Label(self, text = fields[i] + ":")
			label.grid(row = i + 1, column = 0)
			entry = Entry(self, name = fields[i].lower(), font = "Courier 12")
			entry.grid(row = i + 1, column = 1, sticky = W + E + N + S, padx = 5)

			# user cannot type in ID field
			if fields[i] == "id":
				entry.config(state = DISABLED, textvariable = self.IDEntry, bg = "gray")
			# add entry field to dictionary
			key = fields[i]
			# key = key.upper()
			self.entries[key] = entry

	def add_address(self):
		"""Add address record to database"""
		if self.entries["first_name"].get() != "" or self.entries["last_name"].get() != "":
			# create INSERT query command
			query = """INSERT INTO addresses (
                    first_name, last_name, address, city,
                    state, postal_code, country,
                    email, phone)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""
			values = (
				self.entries["first_name"].get(),
				self.entries["last_name"].get(),
				self.entries["address"].get(),
				self.entries["city"].get(),
				self.entries["state"].get(),
				self.entries["postal_code"].get(),
				self.entries["country"].get(),
				self.entries["email"].get(),
				self.entries["phone"].get()
			)

			# open connection, retrieve cursor and execute query
			try:
				connection = MySQLdb.connect(host = "localhost",
											 user = "root", passwd = "@Fmhtrtsaqyl24", db = "address_book")
				cursor = connection.cursor()
				cursor.execute(query, values)
				connection.commit()
				showinfo("Success", "Address added to database.")
			except MySQLdb.OperationalError as message:
				errorMessage = "Error: %d: \n%s" % (message[0], message[1])
				showerror("Error", errorMessage)
			finally:
				cursor.close()
				connection.close()
				self.clear_contents()
		else:  # user has not filled out first/last name fields
			showwarning("Missing fields", "Please enter a first and last name.")

	def find_address(self):
		"""Find address record in database and display it"""
		if self.entries["first_name"].get() != "":
			# create SELECT query command
			query = """SELECT * FROM addresses 
   				WHERE first_name = '%s';""" % (self.entries["first_name"].get())
			# open connection, retrieve cursor and execute query
			try:
				connection = MySQLdb.connect(host = "localhost",
											 user = "root", passwd = "@Fmhtrtsaqyl24", db = "address_book")
				cursor = connection.cursor()
				cursor.execute(query)
				connection.commit()
			except MySQLdb.OperationalError as message:
				errorMessage = "Error: %d: \n%s" % (message[0], message[1])
				showerror("Error", errorMessage)
				self.clear_contents()
			else:  # process results
				showinfo("Success", "Address found in database.")
				# `result` is a list of tuples, where each tuple represents a row of data.
				# Each row is a tuple of values, where each value corresponds to a column in the result set.
				# `fields` is a list of `Field` objects, where each `Field` object represents a column in the result set.
				# Each `Field` object has attributes like `name`, `type_code`, and `display_size` that provide information about the column.
				result = cursor.fetchall()
				fields = cursor.description

				if not result:  # no result for this person
					showinfo("Not found", "Non existing record.")
				else:  # display results
					self.clear_contents()
					for i in range(len(fields)):
						if fields[i][0] == "id":
							self.IDEntry.set(str(result[0][i]))
						else:
							self.entries[fields[i][0]].insert(
									INSERT, str(result[0][i]))
			finally:
				cursor.close()
				connection.close()
		else:  # user has not filled out last name field
			showwarning("Missing fields", "Please enter a last name.")

	def update_address(self):
		"""Update address record in database"""
		if self.entries["id"].get():
			entryItems = self.entries.items()
			query = "UPDATE addresses SET "
			for key, value in entryItems:
				if key != "id":
					query += "%s = '%s', " % (key, value.get())

			query = query[:-2] + " WHERE id = %s" % int(self.IDEntry.get())

			# open connection, retrieve cursor and execute query
			try:
				connection = MySQLdb.connect(host = "localhost",
											 user = "root", passwd = "@Fmhtrtsaqyl24", db = "address_book")
				cursor = connection.cursor()
				cursor.execute(query)
				connection.commit()
			except MySQLdb.OperationalError as message:
				errorMessage = "Error: %d: \n%s" % (message[0], message[1])
				showerror("Error", errorMessage)
			else:
				showinfo("database updated", "Record updated in database.")
			finally:
				cursor.close()
				connection.close()
		else:  # user has not specified an ID
			showwarning("No ID specified", """
                        You may only update an existing record.
                        Use Find to locate the record,
                        then modify the information and press Update.""")

	def clear_contents(self):
		"""Clear contents of Entry fields"""
		for entry in self.entries.values():
			entry.delete(0, END)
		self.IDEntry.set("")

	def help(self):
		"""Display help message to user."""
		showinfo("Help", """Click Find to locate a record.
                            Click Add to insert a new record.
                            Click Update to update the information in a record.
                            Click Clear to empty the Entry fields.\n""")

def main():
	AddressBook().mainloop()

if __name__ == "__main__":
	main()
