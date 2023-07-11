import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from twilio.rest import Client
from whatsapp_api import WhatsApp

class Mail:
    """
        Class containing functions for user operation.
    """
    def __init__(self):
        self.ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        self.sender_email = "patilchanagouda1995@gmail.com"
        self.recipient_email = "hemantgautam50@gmail.com;chanagouda.18p@gmail.com;sharmahs981@gmail.com"

        # SMTP server
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 465
        self.smtp_username = "patilchanagouda1995@gmail.com"
        self.smtp_password = "prnocexkybdxwkqg"

    def send_success_mail(self):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.recipient_email
        message["Subject"] = "Ended Not OK Images"

        # Path to the folder containing the images
        folder_path = self.ROOT_DIR+ r"\Ended_Not_OK_Images"

        # Get the list of image files in the folder
        image_files = [f for f in os.listdir(folder_path) if f.endswith(".png")]

        # Attach each image to the email
        for image_file in image_files:
            file_path = os.path.join(folder_path, image_file)
            with open(file_path, "rb") as f:
                image_data = f.read()
            image = MIMEImage(image_data, name=os.path.basename(file_path))
            part2 = MIMEText((image_file.split(".")[0]) + "<br/>", "html")
            message.attach(part2)
            message.attach(image)

        # Connect to the SMTP server and send the email using SMTP_SSL
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_username, self.smtp_password)
            server.send_message(message)
        return True


    def send_exception_mail(self, error):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = self.recipient_email
        message["Subject"] = "Alert: Monitoring Automation Exception"
        body = 'This exception occured during monitoring automation: {0}'.format(error)
        body = MIMEText(body) # convert the body to a MIME compatible string
        message.attach(body) # attach it to your main message
        # message.attach(error)

        # Connect to the SMTP server and send the email using SMTP_SSL
        with smtplib.SMTP_SSL(self.smtp_server, self.smtp_port) as server:
            server.login(self.smtp_username, self.smtp_password)
            server.send_message(message)
        return True


