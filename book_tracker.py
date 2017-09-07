# -*- coding: utf-8 -*-
'''
Column names: Name, Author, Genre, StartDate, EndDate, Pages, Progress
, Finished 

'''
from __future__ import division
import sqlite3 as sql 


########################################################
# 		     DATA VIEWING 			#
########################################################


def connect():
	global db, cursor
	db = sql.connect('/Users/machine/Desktop/book_app/books.db')
	cursor = db.cursor()

def show_books():
	cursor.execute('select Name from books')
	for i in cursor.fetchall():
		print(i)

def show_authors():
	cursor.execute('select Author from books')
	for i in cursor.fetchall():
		print(i)

def show_genres():
	genres = []
	cursor.execute('select Genre from books')
	# Use the set to avoid repeats 
	for i in cursor.fetchall():
		genres.append(i)
	genres = set(genres)
	print(genres)


def show_finished(): 
	cursor.execute('select Name from books where Finished = 1')
	print('Finished books:')
	for i in cursor.fetchall():
		print(i)
	cursor.execute('select Name from books where Finished = 0')
	print('Unfinished books: ')
	for i in cursor.fetchall():
		print(i)

def show_progress():
	books_dict = {}
	titles = []
	progress = []
	pages = []
	totals = []

	cursor.execute('select Name from books where Finished = 0')
	# get the values out of the tuples! 
	titles = cursor.fetchall()
	# Change to a list of unicodes
	titles = [i[0] for i in titles] 
	# Change to a list of strings 
	titles = [i.encode('UTF8') for i in titles]
	
	cursor.execute('select Progress from books where Finished = 0')
	progress = cursor.fetchall()
	# Convert progress from list of tuples to list of ints 
	progress = [i[0] for i in progress]

	cursor.execute('select Pages from books where Finished = 0')
	pages = cursor.fetchall()
	# See above comment
	pages = [i[0] for i in pages]
	
	# Divide the progress by pages x 100 to get percentage complete
	# Zip them into a dictionary for easy printing  	
	for i in progress:
		for j in pages:
			val = (i/j) * 100 
			totals.append(val)

	for (k,v) in zip(titles, totals):
		v = round(v, 2)
		books_dict[k] = v

	print('Book Progress (%):')
	print(books_dict)

def close():
	try:
		cursor.close()
		db.commit()
		db.close()
	except:
		print('Error closing!')
		raise

########################################################
# 		  DATA MANIPULATION 			#
########################################################
# A reminder of the column order 
def reminder():
	print('Column names: Name, Author, Genre, StartDate, EndDate, Pages, Progress, Finished')
	print('types: string, string, string, int, int (DDMMYYYY), int (DDMMYYYY), int, (0 or 1)')

# Add a new book to the database 
def insert_book(Name, Author, Genre, StartDate, EndDate, Pages, 
	Progress, Finished):
	query = '''
	insert into books
	(Name, Author, Genre, StartDate, EndDate, Pages, Progress, Finished)
	values (?, ?, ?, ?, ?, ?, ?, ?) '''
	cursor.execute(query, (Name, Author, Genre, StartDate, 
		EndDate, Pages, Progress, Finished))
	db.commit()

# Update an existing book 
def update_book():
	name = raw_input('What book have you read? ')
	progress = int(raw_input('How many pages have you read? ')) 
	query = ''' update books set Progress = ? where Name = ? '''
	cursor.execute(query, (progress, name))
	db.commit()

