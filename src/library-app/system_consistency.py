import pydash as py_
from deepdiff import DeepDiff
from mergedeep import merge
from functools import reduce

class SystemConsistency:
	@classmethod
	def information_paths(cls, obj, path = []):
		def information_path(acc, v, k):
			if isinstance(v, dict):
				return acc + cls.information_paths(v, path + k)
			return acc + [path + k]

		return reduce(information_path, obj, [])  # TODO: is the initializer necessary?

	@classmethod
	def have_path_in_common(cls, diff1, diff2):
		return not py_.intersection(cls.information_paths(diff1), cls.information_paths(diff2))

	@classmethod
	def three_way_merge(cls, current_state, prev_state, next_state):
		prev_to_current = cls.diff(prev_state, current_state)
		prev_to_next = cls.diff(prev_state, next_state)
		if not cls.have_path_in_common(prev_to_current, prev_to_next):
			raise Exception('Conflicting concurrent mutations')
		return merge(current_state, prev_to_next)

	@classmethod
	def reconcile(cls, current_state, prev_state, next_state):
		if current_state == prev_state:
			return next_state
		return cls.three_way_merge(current_state, prev_state, next_state)

	@classmethod
	def diff(cls, old_data, new_data):
		try:
			return DeepDiff(old_data, new_data, view='tree')['values_changed']
		except KeyError:
			return {}
