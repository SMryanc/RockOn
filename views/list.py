from pyramid.view import view_config
from rockon.library.accessors.todo import TodoAccessor
from rockon.library.objects.todo import TodoObject

@view_config(route_name='list', renderer='rockon:templates/list.mako')

class TodoView(object):
	
    def __init__(self, request):
		self.request = request
		
    def __call__(self):
	    return self.list_view()

    def list_view(self):
		try:
			obj = TodoAccessor()
			tasks = obj.loadAllTodos(self.request)
			return {'tasks': tasks}
		except Exception as e:
			return {'tasks': [], 'error': e}
			pass
