# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 19:51:15 2018

@author: hrq06

History:
    20181214 Initial version
"""

# Import Python Packages
import os

def main():
    # Find free desk space
    print("This program first line.")
    CurrentFolder = os.getcwd()
    print("CurrentFolder: " + CurrentFolder)
    FreeDeskSpace = ReadDeskProp(CurrentFolder)
    print("Function output - FreeDeskSpace: " + str(FreeDeskSpace))
    #AnotherFolder = "K:\\"
    #AnotherFolderFreeDeskSpace = ReadDeskProp(AnotherFolder)
    #print("AnotherFolderFreeDeskSpace: " + str(AnotherFolderFreeDeskSpace))
    
    # Send a mail
    From = "eik.herbsleb@gmail.com"
    To = From
    Subject = "WARNING - Test mail from LACmusTaskStorageCheck"
    Message = "Free desk space is only: " + str(FreeDeskSpace)
    SendMail(From, To, Subject, Message)
    
def SendMail(From, To, Subject, Message ):    
    ## Building message 
    #from email.mime.text import MIMEText
    #msg = MIMEText(“Server is running out of disk space”)
    #msg[“Subject”] = “Low disk space warning”
    #msg[“From”] = From
    #msg[“To”] = To
    #msg.as_string()
    #‘Content-Type: text/plain; charset=”us-ascii”\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: Low disk space warning\nTo: admin@example.com\nFrom: admin@example.com\nTo: test@gmail.com\n\nServer is running out of disk space’
    ## Connect to SMTP server
    #import smtplib
    #server=smtplib.SMTP(“smtp.gmail.com”, 587)
    #server.ehlo()
    #(250, b’smtp.gmail.com at your service, [54.202.39.68]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nCHUNKING\nSMTPUTF8')
    #server.starttls()
    #(220, b’2.0.0 Ready to start TLS’)
    #server.login(“eik.herbsleb”,”spis98Is”)
    #(235, b’2.7.0 Accepted’)
    #server.sendmail(From,To,msg.as_string())
    #{}
    #server.quit()
    #(221, b'2.0.0 closing connection o76sm39310782pfi.119 - gsmtp')    
    
    # Ref http://naelshiab.com/tutorial-send-email-python/
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("From@mail.adrs", "FromMailAdrsPassword")
    msg = "This is a test message from a Python app LACmusTaskStorageCheck"
    server.sendmail("From@mail.adrs", "to@mail.adrs", msg)
    server.quit()
    
def ReadDeskProp(path):
    """
    Return free disk storage (GB in float) of the given path.
    """
    import psutil
    total, used, free, percent = psutil.disk_usage(path)
    return(float(free/1000000))
    
    

if __name__ == "__main__":
    
    main()
