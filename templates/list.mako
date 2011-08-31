# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Task's List</h1>

% if error:
	<h5 class="error">Error: ${error}</h5>
	
% else:

<ul id="tasks">
% if tasks:
  % for task in tasks:
  <li>
    <span class="name">${task['name']}</span>
    <span class="actions">
      [ <a href="${request.route_url('close', id=task['id'])}">close</a> ]
    </span>
  </li>
  % endfor
% else:
  <li>There are no open tasks</li>
% endif
  <li class="last">
    <a href="${request.route_url('new')}">Add a new task</a>
  </li>
</ul>

% endif