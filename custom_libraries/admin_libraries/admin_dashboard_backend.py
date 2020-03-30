from flask import render_template, session, redirect, url_for

def Admin_Dashboard_Backend():
	is_the_user_admin=session.get('admin','no') #if admin session doesn't exist, it creates the admin session and defaults to no
	is_the_user_logged_in=session.get('logged_in',False)
	
	if (is_the_user_admin=='yes') and (is_the_user_logged_in==True):
		return render_template('admin_pages/admin_dashboard_page.html')
	else:
		return redirect(url_for('Log_In_Page'))