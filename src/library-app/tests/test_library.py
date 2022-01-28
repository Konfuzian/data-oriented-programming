import json
import pytest
from functools import partial

import library as Library


def test_search_book_by_title_json():
	""" Functions more on the 'outside' require fewer tests, but the data is more complex. """
	library_data = {
		"catalog": {
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
	}

	book_info = {
		"isbn": "978-1779501127",
		"title": "Watchmen",
		"authorNames": ["Alan Moore", "Dave Gibbons"]
	}

	search = partial(Library.search_books_by_title_json, library_data)

	assert json.loads(search("Watchmen")) == [book_info]
	assert json.loads(search("Batman")) == []

def test_add_member():
	jessie = {
		"email": "jessie@gmail.com",
		"password": "my-secret"
	}

	franck = {
		"email": "franck@gmail.com",
		"password": "my-top-secret"
	}

	state_before = {
		"userManagement": {
			"membersByEmail": {
				"franck@gmail.com": {
					"email": "franck@gmail.com",
					"password": "my-top-secret"
				}
			}
		}
	}

	expected = {
		"userManagement": {
			"membersByEmail": {
				"jessie@gmail.com": {
					"email": "jessie@gmail.com",
					"password": "my-secret"
				},
				"franck@gmail.com": {
					"email": "franck@gmail.com",
					"password": "my-top-secret"
				}
			}
		}
	}

	result = Library.add_member(state_before, jessie)
	assert result == expected
