from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from rockon.library.accessors.todo import TodoAccessor

@view_config(route_name='new', renderer='rockon:templates/new.mako')

class NewTodo(object):

    def __init__(self, request):
		self.request = request

    def __call__(self):
		if self.request.method == 'POST':
			if self.request.POST.get('name'):
				return self.new_view()
			else:
				self.request.session.flash('Please enter a name for the task!')
		return {}

    def new_view(self):
		try:
			obj = TodoAccessor()
			obj.insertTodo(self.request, self.request.POST['name'])
			self.request.session.flash('New task was successfully added!')
			return HTTPFound(location=self.request.route_url('list'))
		except Exception as e:
			return {'error':e}
			pass