import json
from pydash import py_


def search_books_by_title(catalog_data, query):
	books = catalog_data['booksByIsbn'].values()
	matching_books = filter(lambda book: query.lower() in book['title'].lower(), books)
	return [book_info(catalog_data, book) for book in matching_books]

def book_info(catalog_data, book):
	return {
		'title': book['title'],
		'isbn': book['isbn'],
		'authorNames': author_names(catalog_data, book['authorIds']),
	}

def author_names(catalog_data, author_ids):
	return [py_.get(catalog_data, ['authorsById', author_id, 'name']) for author_id in author_ids]

def get_book_lendings(catalog_data, user_id, member_id):
	pass

def add_book_item(catalog_data, book_item_info):
	pass

def checkout_book(catalog_data, user_id, book_item_id):
	pass

def return_book(catalog_data, user_id, book_item_id):
	pass
