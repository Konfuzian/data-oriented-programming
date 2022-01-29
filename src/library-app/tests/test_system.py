import pytest

from system import System, SystemState


def test_using_persistent_data_structures():
	"""
	You have to use run_tests.sh (e.g. in Git Bash) to run the tests,
	otherwise you won't be using persistent data structures and this test will fail.
	"""
	x = {}
	with pytest.raises(TypeError):
		x['a'] = 'cannot mutate persistent maps'

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

	system_state = SystemState()
	system_state.commit(None, state_before)
	System.add_member(system_state, jessie)

	assert system_state.get() == expected