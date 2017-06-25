from helpers.session import SessionGoogle
from terminaltables import SingleTable

session = SessionGoogle('mail', 'password')
notes = session.googleKeep_formatNotes(session.googleKeep_getNotes())


data = []

for note in reversed(notes):
	data.append(['not have title' if note['title'] == "" else note['title']])
	data.append([note['text']])
	table = SingleTable(data)
	table.inner_heading_row_border = False
	print(table.table)

	data = []

