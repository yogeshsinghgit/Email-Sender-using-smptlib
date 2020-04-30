
import smtplib
from plyer import notification

class LogicMail():
    def __init__(self,sender_email,sender_password):

        self.sender_email = sender_email
        self.sender_password = sender_password

    def send(self,receiver_email,subject,text_message):
        self.receiver = receiver_email
        self.subject = subject
        self.message = text_message
        self.receiver = self.receiver.split(',')

        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        self.server.login(self.sender_email, self.sender_password)
        self.server.sendmail(self.sender_email,
                             self.receiver,
                             "Subject: " + str(self.subject) + "\n\n" + str(self.message))
        self.server.quit()

        notification.notify(title="Sender Says",message=" Mail is sent",timeout=5)


