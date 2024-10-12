#  Date & Time 10/06/2024, 08:23 pm.
#  @author Mesfin Haftu
# serialization is done by default method, we dont worry about exception handling
import json
class Who:
	def __init__(self, name, age):
		self.name = name
		self.age = age

class MyEncoder(json.JSONEncoder):
	def default(self, w):
		if isinstance(w, Who):
			return w.__dict__
		else:
			return super().default(self, w)

some_man = Who('John', 42)
print(json.dumps(some_man, cls=MyEncoder))

# to convert json string to python string
jstr = '1.6021766189989e-19'

electron = json.loads(jstr)
print(type(electron))
print(electron)
