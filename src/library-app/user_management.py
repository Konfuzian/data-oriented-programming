import pydash as py_
from toolz.dicttoolz import assoc_in


def login(user_management_data, login_info):
	pass

def add_member(user_management_data, member):
	email = member['email']
	existing_members = py_.get(user_management_data, ['membersByEmail'], {})

	if email in existing_members:
		raise Exception('Member already exists')

	return assoc_in(user_management_data, ['membersByEmail', email], member)

def block_member(user_management_data, member_id):
	pass

def unblock_member(user_management_data, member_id):
	pass

def is_librarian(user_management_data, email):
	return email in user_management_data['librariansByEmail']

def is_vip_member(user_management_data, email):
	return py_.get(user_management_data, ['membersByEmail', email, 'isVIP'], False)

def is_super_member(user_management_data, email):
	return py_.get(user_management_data, ['membersByEmail', email, 'isSuper'], False)
