# How do ?'s prevent SQL injection?
# Naming conventions?
# Commenting conventions?

from rockon.library.objects.todo import TodoObject

class TodoAccessor(object):
	
	def __init__(self):
		self.data = []
		
	def loadAllTodos(self, request):
		try:
			sql = 'SELECT id, name FROM tasks WHERE closed = 0'
			rs = request.db.execute(sql)
			tasks = [dict(id=row['id'], name=row['name']) for row in rs.fetchall()]
			return tasks
		except Exception:
			raise Exception('Unable to load list')
		
	def deleteTodo(self, request, task_id):
		try:
			sql = 'UPDATE tasks SET closed = ? WHERE id = ?'
			request.db.execute(sql, (1, task_id))
			request.db.commit()
		except Exception:
			raise Exception('Unable to delete item')
		
	def insertTodo(self, request, text):
		try:
			sql = 'INSERT INTO tasks (name, closed) VALUES (?, ?)'
			request.db.execute(sql, [text, 0])
			request.db.commit()
		except Exception:
			raise Exception('Unable to add new item')