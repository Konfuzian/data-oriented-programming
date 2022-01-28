import json
from toolz.dicttoolz import assoc_in

import user_management as UserManagement
import catalog as Catalog


def search_books_by_title_json(library_data, query):
	return json.dumps(Catalog.search_books_by_title(library_data['catalog'], query))

def get_book_lendings(library_data, user_id, member_id):
	def is_allowed():
		return UserManagement.is_librarian(library_data['userManagement'], user_id) \
			or UserManagement.is_super_member(library_data['userManagement'], user_id)

	if not is_allowed():
		raise Exception('Not allowed to get book lendings')
	return Catalog.get_book_lendings(library_data['catalog'], member_id)

def add_book_item(library_data, book_item_info):
	def is_allowed():
		return UserManagement.is_librarian(library_data['userManagement'], user_id) \
			or UserManagement.is_super_member(library_data['userManagement'], user_id)

	if not is_allowed():
		raise Exception('Not allowed to add a book item')
	return Catalog.add_book_item(library_data['catalog'], book_item_info)

def checkout_book(library_data, user_id, book_item_id):
	pass

def return_book(library_data, user_id, book_item_id):
	pass

def login(library_data, login_info):
	pass

def add_member(library_data, member):
	next_user_management = UserManagement.add_member(library_data['userManagement'], member)
	return assoc_in(library_data, ['userManagement'], next_user_management)

def block_member(library_data, member_id):
	pass

def unblock_member(library_data, member_id):
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
