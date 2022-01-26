import json
from pydash import py_


class Catalog:
	
	@classmethod
	def search_books_by_title(cls, catalog_data, query):
		books = catalog_data['booksByIsbn'].values()
		matching_books = filter(lambda book: query.lower() in book['title'].lower(), books)
		return [cls.book_info(catalog_data, book) for book in matching_books]

	@classmethod
	def book_info(cls, catalog_data, book):
		return {
			'title': book['title'],
			'isbn': book['isbn'],
			'authorNames': cls.author_names(catalog_data, book['authorIds']),
		}

	@classmethod
	def author_names(cls, catalog_data, author_ids):
		return [py_.get(catalog_data, ['authorsById', author_id, 'name']) for author_id in author_ids]

	@classmethod
	def get_book_lendings(cls, catalog_data, user_id, member_id):
		pass

	@classmethod
	def add_book_item(cls, catalog_data, book_item_info):
		pass

	@classmethod
	def checkout_book(cls, catalog_data, user_id, book_item_id):
		pass

	@classmethod
	def return_book(cls, catalog_data, user_id, book_item_id):
		pass
