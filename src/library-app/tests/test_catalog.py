import pytest

import catalog as Catalog


def test_author_names():
	""" Functions on the 'inside' require lots of tests, but the data is simple. """
	# TODO: don't use freeze here, pyrthon should convert it to a pyrsistent map on its own
	catalog_data = {
		"authorsById": {
			"alan-moore": {
				"name": "Alan Moore"
			},
			"dave-gibbons": {
				"name": "Dave Gibbons"
			}
		}
	}

	# empty ids or catalog
	assert Catalog.author_names(catalog_data, []) == []
	assert Catalog.author_names({}, []) == []
	assert Catalog.author_names({}, ['alan-moore']) == [None]
	# existent ids
	assert Catalog.author_names(catalog_data, ['alan-moore']) == ['Alan Moore']
	assert Catalog.author_names(catalog_data, ['alan-moore', 'dave-gibbons']) == ['Alan Moore', 'Dave Gibbons']
	# nonexistent ids
	assert Catalog.author_names(catalog_data, ['alan-moore', 'albert-einstein']) == ['Alan Moore', None]
	assert Catalog.author_names(catalog_data, ['albert-einstein']) == [None]

def test_book_info():
	catalog_data = {
		"authorsById": {
			"alan-moore": {
				"name": "Alan Moore"
			},
			"dave-gibbons": {
				"name": "Dave Gibbons"
			}
		}
	}

	book = {
		"isbn": "978-1779501127",
		"title": "Watchmen",
		"publicationYear": 1987,
		"authorIds": ["alan-moore", "dave-gibbons"]
	}

	expected = {
		"authorNames": ["Alan Moore", "Dave Gibbons"],
		"isbn": "978-1779501127",
		"title": "Watchmen",
	}

	result = Catalog.book_info(catalog_data, book)

	assert result == expected

def test_search_books_by_title():
	catalog_data = {
		"booksByIsbn": {
			"978-1779501127": {
				"isbn": "978-1779501127",
				"title": "Watchmen",
				"publicationYear": 1987,
				"authorIds": ["alan-moore", "dave-gibbons"]
			}
		},
		"authorsById": {
			"alan-moore": {
				"name": "Alan Moore",
				"bookIsbns": ["978-1779501127"]
			},
			"dave-gibbons": {
				"name": "Dave Gibbons",
				"bookIsbns": ["978-1779501127"]
			}
		}
	}

	book_info = {
		"isbn": "978-1779501127",
		"title": "Watchmen",
		"authorNames": ["Alan Moore", "Dave Gibbons"]
	}

	assert Catalog.search_books_by_title(catalog_data, "Watchmen") == [book_info]
	assert Catalog.search_books_by_title(catalog_data, "watchmen") == [book_info]
	assert Catalog.search_books_by_title(catalog_data, "Batman") == []
