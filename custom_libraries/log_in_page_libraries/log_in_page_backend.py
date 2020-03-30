from flask import render_template, request, redirect, url_for,session

from create_and_migrate_db import All_Users_Information_Table_Class

def Log_In_Page_Backend(bcrypt):
	if request.method== 'GET':
		return render_template('log_in_page.html')

	if request.method== 'POST':
		if request.form['log_in_page_button']=='Log In':
			user_name=request.form['user_name']
			password=request.form['password']

			user_name=user_name.lower()
			
			if (user_name=='admin') and (password=='isdopadmin'):
				session['admin']='yes'
				session['logged_in'] = True
				session['user_name']= user_name
				return redirect(url_for('Admin_Page'))
			else:
				logged_in_user_object=All_Users_Information_Table_Class.query.filter(All_Users_Information_Table_Class.user_name==user_name).first()

				if logged_in_user_object is None:
					return "Incorrect username or password"

				else:
					password_boolean=bcrypt.check_password_hash(logged_in_user_object.hashed_password,password)
					if password_boolean==True:
						session['logged_in'] = True
						session['user_name']=user_name
						return redirect(url_for('Home_Page',user_name=session.get('user_name')))
						
					else:
						return "Incorrect password"