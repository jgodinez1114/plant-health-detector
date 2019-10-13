#! /usr/bin/env python
# -*- coding: utf8 -*-

# Joel Godinez
# 12 October 2019

import smtplib
from email.mime.multipart import MIMEMultipart # multipurpose internet mail extension
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import os
import time
import sys



def send_email_file(subject, attachment, recipient):
    # set up the MIME
    message = MIMEMultipart()
    message['Subject'] = subject
    message['From'] = 'planthealthdetector@gmail.com'
    message['To'] = recipient
    message['Reply-to'] = 'planthealthdetector@gmail.com'

    message.preamble = 'Multipart message.\n'

    part = MIMEText("Attached is the plant file")
    message.attach(part)

    part = MIMEApplication(open(attachment, "rb").read())
    part.add_header('Content-Decomposition', 'attachment', filename=attachment)
    message.attach(part)

    # identify gmail server port
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("planthealthdetector@gmail.com", "phd2019.*")

    server.sendmail(message['From'], recipient, message.as_string())
    server.quit()


dir_name = "C://Users//joelg//PycharmProjects//sendEmail"
base_file_name = "unhealthyImage1"
filename_suffix = '.jpg'
fileToSend = os.path.join(dir_name, base_file_name + filename_suffix)
send_email_file("Plant Needs Attention Soon", fileToSend, "planthealthdetector@gmail.com")





