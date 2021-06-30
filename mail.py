import smtplib
def mail(receiver, subject, msg):  
    sender = "otter18"
    
    message = 'From: {}\nTo: {}\nSubject: {}\n\n{}'.format(sender,
                                                           receiver,
                                                           subject,
                                                           msg)
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("---", "---")
    
    server.sendmail("----", receiver, message)
    server.quit()
mail("----", "subject", "main text")
