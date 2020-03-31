import smtplib

def Asynchronously_Send_Email_Through_SMTP(app, email):
	host = "smtp.network.lan"
	server = smtplib.SMTP(host, 25)
	server.set_debuglevel(1)
	FROM = "chuazhang@suncor.com"
	MSG = "Subject: Welcome to use ISDOP\n\nWelcome to use ISDOP!"
	server.sendmail(FROM, email, MSG)
	server.quit()
