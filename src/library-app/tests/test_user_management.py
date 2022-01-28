import pytest

import user_management as UserManagement


def test_add_member_with_empty_state():
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

	assert result == expected

def test_add_member_with_nonexistent_member():
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

	assert result == expected

def test_add_member_with_existent_member():
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

	pytest.raises(Exception, lambda _: UserManagement.add_member(state_before, member))
