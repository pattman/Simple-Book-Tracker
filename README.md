# Simple-Book-Tracker
A short python script to track books you read

# Usage Guide 
This Python script was written to work with a simple SQLite3 database. 
The database for this script as seven columns corresponding to different features of the book: 
Column names: Name, Author, Genre, StartDate, EndDate, Pages, Progress, Finished 
Column Data Types: TEXT, TEXT, INTEGER (DDMMYYYY), INTEGER (DDMMYYYY), INTEGER, INTEGER, INTEGER (0 or 1)

1. To use this script you can import the Python script as a module e.g. import book_tracker 
2. All functions are accesible similar to class methods e.g. book_tracker.show_progress()
3. To begin, start with book_tracker.connect()
4. When finished viewing book stats or editing the db, finish with book_tracker.close()
