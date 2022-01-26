
from system_consistency import SystemConsistency
from system_validity import SystemValidity

class SystemState:

	system_data = None

	@classmethod
	def get(cls):
		return cls.system_data

	@classmethod
	def commit(cls, prev_state, next_state):
		next_system_data = SystemConsistency.reconcile(cls.system_data, prev_state, next_state)
		if not SystemValidity.validate(prev_state, next_system_data):
			raise 'The system data to be committed is not valid!'
		cls.system_data = next_system_data
