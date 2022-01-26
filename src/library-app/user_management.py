import pydash as py_
from toolz.dicttoolz import assoc_in


class UserManagement:

	@classmethod
	def login(cls, user_management_data, login_info):
		pass

	@classmethod
	def add_member(cls, user_management_data, member):
		email = member['email']
		existing_members = py_.get(user_management_data, ['membersByEmail'], {})

		if email in existing_members:
			raise Exception('Member already exists')

		return assoc_in(user_management_data, ['membersByEmail', email], member)

	@classmethod
	def block_member(cls, user_management_data, member_id):
		pass

	@classmethod
	def unblock_member(cls, user_management_data, member_id):
		pass

	@classmethod
	def is_librarian(cls, user_management_data, email):
		return email in user_management_data['librariansByEmail']

	@classmethod
	def is_vip_member(cls, user_management_data, email):
		return py_.get(user_management_data, ['membersByEmail', email, 'isVIP'], False)

	@classmethod
	def is_super_member(cls, user_management_data, email):
		return py_.get(user_management_data, ['membersByEmail', email, 'isSuper'], False)
