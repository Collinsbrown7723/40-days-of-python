import smtplib
from email.message import EmailMessage
from pathlib import Path

mail_content = Path("index.html").read_text()
print(mail_content)

email = EmailMessage() #build an email object
email['from'] = 'Python <masterpythonprogramming@gmail.com>'
email['to'] = 'andrei.cma@protonmail.com'
email['subject'] = 'Good job Python!'
email.set_content(mail_content,"html")
with smtplib.SMTP(host="yourmail.com",port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    
    smtp.send_message(email)


import smtplib
from email.message import EmailMessage
from pathlib import Path

html_content = Path('test_email.html').read_text()

email = EmailMessage()
email['from'] = 'Python <masterpythonprogramming@gmail.com>'
email['to'] = 'andrei.cma@protonmail.com'
email['subject'] = 'Good job Python!'


# email.set_content('Wow! Congratulations!')
# email.set_content(html_content, 'html')


# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.ehlo()

#     smtp.login('masterpythonprogramming@gmail.com', 'GdSRJMsAS7')
#     smtp.send_message(email)
#     print('The mail was sent!')
