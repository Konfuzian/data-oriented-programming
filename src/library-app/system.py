
from library import Library
from system_state import SystemState

class System:

	@classmethod
	def add_member(cls, system_state, member):
		prv = SystemState.get()
		nxt = Library.add_member(prv, member)
		SystemState.commit(prv, nxt)
