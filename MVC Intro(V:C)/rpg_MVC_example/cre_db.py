import sqlite3

conn = sqlite3.connect('new.db')

conn.execute(
	"""
	CREATE TABLE player
	id INTEGER PRIMARY KEY,
	name TEXT,
	job TEXT,
	health INTEGER,
	attack INTEGER,

	"""

	"""
	CREATE TABLE monster
	id INTEGER PRIMARY KEY,
	type TEXT,
	health INTEGER,
	attack INTEGER,

	"""
);