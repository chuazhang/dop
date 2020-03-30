from flask_mail import Mail, Message

def Asynchronously_Send_Email_Through_SMTP(app, email):
	mail_settings = {
		"MAIL_SERVER": 'smtp.gmail.com',
		"MAIL_PORT": 465,
		"MAIL_USE_TLS": False,
		"MAIL_USE_SSL": True,
		"MAIL_USERNAME": 'zhangchuangxin@gmail.com',
		"MAIL_PASSWORD": 'L98hg*BV'
	}
	app.config.update(mail_settings)
	mail = Mail(app)
	with app.app_context():
		msg = Message(subject="You are invited to use ISDOP",
			sender=app.config.get("MAIL_USERNAME"),
			recipients=[email],
			body="You are invited to use ISDOP!")
		mail.send(msg)
