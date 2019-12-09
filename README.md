# Sending email usign python smtplib

it gives feature to send mail anonymously or with authentication depending upon out host.

### For sending anonymous email

Suppose that you want to send a fake email to nkpro@meow.com.

Firstly, using "nslookup" command to find the exchange server of "meow.com" (`set type=mx`)
> dig mx meow.com

Coz SMTP protocol doesn't authorize on exchange server, you can directly send MIME format E-mail to the exchange server.


> Tips: Testing it on your own email to make sure your E-mail won't be sent to Trash.
