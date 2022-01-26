import json
from toolz.dicttoolz import assoc_in

from user_management import UserManagement
from catalog import Catalog

class Library:
	
	@classmethod
	def search_book(cls, library_data, search_query):
		pass

	@classmethod
	def search_books_by_title_json(cls, library_data, query):
		return json.dumps(Catalog.search_books_by_title(library_data['catalog'], query))

	@classmethod
	def get_book_lendings(cls, library_data, user_id, member_id):
		def is_allowed():
			return UserManagement.is_librarian(library_data['userManagement'], user_id) \
				or UserManagement.is_super_member(library_data['userManagement'], user_id)

		if not is_allowed():
			raise Exception('Not allowed to get book lendings')
		return Catalog.get_book_lendings(library_data['catalog'], member_id)

	@classmethod
	def add_book_item(cls, library_data, book_item_info):
		def is_allowed():
			return UserManagement.is_librarian(library_data['userManagement'], user_id) \
				or UserManagement.is_super_member(library_data['userManagement'], user_id)

		if not is_allowed():
			raise Exception('Not allowed to add a book item')
		return Catalog.add_book_item(library_data['catalog'], book_item_info)

	@classmethod
	def checkout_book(cls, library_data, user_id, book_item_id):
		pass

	@classmethod
	def return_book(cls, library_data, user_id, book_item_id):
		pass

	@classmethod
	def login(cls, library_data, login_info):
		pass

	@classmethod
	def add_member(cls, library_data, member):
		next_user_management = UserManagement.add_member(library_data['userManagement'], member)
		return assoc_in(library_data, ['userManagement'], next_user_management)

	@classmethod
	def block_member(cls, library_data, member_id):
		pass

	@classmethod
	def unblock_member(cls, library_data, member_id):
		pass


# function setImmutable(map, path, v) {
#   var modifiedNode = v;
#   var k = path[0];
#   var restOfPath = path.slice(1);
#   if (restOfPath.length > 0) {
#     modifiedNode = setImmutable(map[k], restOfPath, v);
#   }
#   var res = Object.assign({}, map); //
#   res[k] = modifiedNode;
#   return res;
# }