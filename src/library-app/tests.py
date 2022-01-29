import json
from functools import partial
from unittest import TestCase, main

import library as Library
import catalog as Catalog
import user_management as UserManagement
from system import System, SystemState, SystemConsistency, SystemValidity


class CatalogTestCase(TestCase):
	
	def test_author_names(self):
		""" Functions on the 'inside' require lots of tests, but the data is simple. """
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
		self.assertEqual(Catalog.author_names(catalog_data, []), [])
		self.assertEqual(Catalog.author_names({}, []), [])
		self.assertEqual(Catalog.author_names({}, ['alan-moore']), [None])
		# existent ids
		self.assertEqual(Catalog.author_names(catalog_data, ['alan-moore']), ['Alan Moore'])
		self.assertEqual(Catalog.author_names(catalog_data, ['alan-moore', 'dave-gibbons']), ['Alan Moore', 'Dave Gibbons'])
		# nonexistent ids
		self.assertEqual(Catalog.author_names(catalog_data, ['alan-moore', 'albert-einstein']), ['Alan Moore', None])
		self.assertEqual(Catalog.author_names(catalog_data, ['albert-einstein']), [None])

	def test_book_info(self):
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

		self.assertEqual(result, expected)

	def test_search_books_by_title(self):
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

		self.assertEqual(Catalog.search_books_by_title(catalog_data, "Watchmen"), [book_info])
		self.assertEqual(Catalog.search_books_by_title(catalog_data, "watchmen"), [book_info])
		self.assertEqual(Catalog.search_books_by_title(catalog_data, "Batman"), [])


class UserManagementTestCase(TestCase):
	
	def test_add_member_with_empty_state(self):
		member = {
			"email": "jessie@gmail.com",
			"password": "my-secret"
		}

		state_before = {}

		expected = {
			"membersByEmail": {
				"jessie@gmail.com": {
					"email": "jessie@gmail.com",
					"password": "my-secret"
				}
			}
		}

		result = UserManagement.add_member(state_before, member)

		self.assertEqual(result, expected)

	def test_add_member_with_nonexistent_member(self):
		member = {
			"email": "new@gmail.com",
			"password": "my-secret"
		}

		state_before = {
			"membersByEmail": {
				"jessie@gmail.com": {
					"email": "jessie@gmail.com",
					"password": "my-secret"
				}
			}
		}

		expected = {
			"membersByEmail": {
				"jessie@gmail.com": {
					"email": "jessie@gmail.com",
					"password": "my-secret"
				},
				"new@gmail.com": {
					"email": "new@gmail.com",
					"password": "my-secret"
				}
			}
		}

		result = UserManagement.add_member(state_before, member)

		self.assertEqual(result, expected)

	def test_add_member_with_existent_member(self):
		member = {
			"email": "jessie@gmail.com",
			"password": "my-secret"
		}

		state_before = {
			"membersByEmail": {
				"jessie@gmail.com": {
					"email": "jessie@gmail.com",
					"password": "my-secret"
				}
			}
		}

		self.assertRaises(Exception, lambda _: UserManagement.add_member(state_before, member))


class LibraryTestCase(TestCase):

	def test_search_book_by_title_json(self):
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

		self.assertEqual(json.loads(search("Watchmen")), [book_info])
		self.assertEqual(json.loads(search("Batman")), [])

	def test_add_member(self):
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
		self.assertEqual(result, expected)


class SystemTestCase(TestCase):

	def test_using_persistent_data_structures(self):
		"""
		If pyrthon is not set up correctly, it will not be using
		persistent data structures and this test will fail.
		"""
		with self.assertRaises(TypeError):
			{}['x'] = 'cannot mutate persistent maps'

	def test_add_member(self):
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

		system_state = SystemState()
		system_state.commit(None, state_before)
		System.add_member(system_state, jessie)

		self.assertEqual(system_state.get(), expected)


class SystemStateTestCase(TestCase):
	pass


class SystemConsistencyTestCase(TestCase):
	pass


class SystemValidityTestCase(TestCase):
	pass


if __name__ == '__main__':
	main()
