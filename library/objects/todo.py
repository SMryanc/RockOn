class TodoObject(object):
		
		id = 0
		name = ''
		closed = 0
		
		def __init__(self, params = []):
			for key, value in params:
				self.key = value
