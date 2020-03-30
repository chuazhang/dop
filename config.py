import os

workers = int(os.environ.get('GUNICORN_PROCESSES', '3'))
threads = int(os.environ.get('GUNICORN_THREADS', '1'))

forwarded_allow_ips = '*'
secure_scheme_headers = { 'X-Forwarded-Proto': 'https' }

#basedir = os.path.abspath(os.path.dirname(__file__))
class Config(object):
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	'sqlite:///' + os.getcwd()+'/gt_database.db' ##USE THIS FOR SQLITE

	#USE THIS FOR AWS RDS
	# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
	#username: user_name
	#password: pa55word
	#db name: bulldatabase
	#application.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://user_name:pa55word@databaseinstance.csrlgpbei105.us-west-2.rds.amazonaws.com:3306/bulldatabase'

	#^this will be replaced with  (if using sqlite)
	#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+'/home/webappname/deploy/gt_database.db'
	#when uploaded to pythonanywhere.com

	SQLALCHEMY_TRACK_MODIFICATIONS = False