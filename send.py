# coding: UTF-8

import smtplib
import os
import base64
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 


def send_mail(mail_host, mail_port, mail_from, mail_to, msg, auth= None):
	# connect smtp server, set debug to see reply information
	smtp = smtplib.SMTP()
	smtp.connect(mail_host, mail_port)
	smtp.set_debuglevel(1)
	# authentication
	if auth :
		smtp.starttls()
		smtp.login(*auth)
	# send mail
	smtp.sendmail(mail_from, mail_to, msg.as_string())
	# quit
	smtp.quit()

def get_massage(mail_from, mail_to, subject, body, files=[], infiles=[]):
	msg = MIMEMultipart('alternative')
	# from, to, subject
	msg["From"] = mail_from
	msg["To"] = ";".join(mail_to)
	msg['Subject'] = subject
	# infiles as base64 string
	inb64s = []
	for infile in infiles :
		file_ = open(infile,'rb')
		b64 = "<p>#File:"+os.path.split(infile)[-1]+"<br>"
		b64 += base64.b64encode(file_.read()).decode()+"</p>"
		file_.close()
		inb64s.append(b64)
	# html
	html = """\
	<html>
		<head><meta charset="UTF-8"></head>
		<body>
			<p>"""+body+"</p>\n\t\t\t"+'\n\t\t\t'.join(inb64s)+"""
		</body>
	</html>
	"""
	content = MIMEText(html, 'html', 'UTF-8')
	msg.attach(content)
	# attach
	for file_ in files :
		attach = MIMEText(open(file_, "rb").read(), "base64", "UTF-8")
		attach['Content-Type'] = 'application/octet-stream'
		attach['Content-Disposition'] = 'attachment; filename=%s' % os.split(file_)[-1]
		msg.attach(attach)
	# end
	return msg

if __name__ == "__main__":
	# host:port 
	mail_host = "host"
	mail_port = 587
	# mail from and mail to
	mail_from = "from_address"
	mail_to = ["to_address"]
	# authentication
	auth = ("from_address","password") # None for anonymous
	# subject
	subject = "Subject"
	# body
	body = "Body"
	# attachment
	attachments = []
	# inline attachment
	inline_attachments = []
	# massage
	msg = get_massage(mail_from, mail_to, subject, body, attachments, inline_attachments)
	# send
	send_mail(mail_host, mail_port, mail_from, mail_to, msg, auth)
