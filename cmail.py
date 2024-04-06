import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('sumapriyaperla@gmail.com','gtgm vwex zsda oedg')
    msg=EmailMessage()
    msg['From']='sumapriyaperla@gmail.com'
    msg['To']=to
    msg['Subject']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
    
