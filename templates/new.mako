# -*- coding: utf-8 -*- 
<%inherit file="layout.mako"/>

<h1>Add a new task</h1>

% if error:
	<h5 class="error">Error: ${error}</h5>
% endif

<form action="${request.route_url('new')}" method="post">
  <input type="text" maxlength="100" name="name">
  <input type="submit" name="add" value="ADD" class="button">
</form>