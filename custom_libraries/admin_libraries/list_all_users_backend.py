from flask import render_template, request, redirect, url_for, session
from create_and_migrate_db import All_Users_Information_Table_Class

def List_All_Users_Backend():
	if request.method== 'GET':
		is_the_user_admin=session.get('admin','no') #if admin session doesn't exist, it creates the admin session and defaults to no
		is_the_user_logged_in=session.get('logged_in',False)
		
		if (is_the_user_admin=='yes') and (is_the_user_logged_in==True):
			All_Users_Objects=All_Users_Information_Table_Class.query.all()
			return render_template('admin_pages/list_all_users_page.html',All_Users_Objects=All_Users_Objects)
		else:
			return redirect(url_for('Log_In_Page'))