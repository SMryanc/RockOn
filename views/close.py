from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from rockon.library.accessors.todo import TodoAccessor

@view_config(route_name='close')

class CloseTodo(object):
	
	def __init__(self, request):
		self.request = request
		
	def __call__(self):
		return self.close_view()

	def close_view(self):
		try:
			task_id = int(self.request.matchdict['id'])
			obj = TodoAccessor()
			obj.deleteTodo(self.request, task_id)
			self.request.session.flash('Task was successfully closed!')
		except Exception as e:
			self.request.session.flash('Unable to delete the item!')
			pass
		return HTTPFound(location=self.request.route_url('list'))