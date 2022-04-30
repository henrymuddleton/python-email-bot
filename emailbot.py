import smtplib
from time import sleep
from os import system as s
count = 0
def send_mail(user,password,to,subject,body):
  body = 'From: %s\nTo: %s\nSubject: %s\n\n%s' % (user,', '.join(to),subject,body)

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.ehlo()
  server.login(user, password)
  server.sendmail(user, to, body)
  server.close() 
  print('Email sent!',count)  
mail_user = input('FROM:')
password_user = input('PASSWORD:')
s('clear')
send = []
while True:
  answer = input('TO (Enter 0 when done):')
  if answer == '0':
    break
  else:
    send.append(answer)
topic = input('SUBJECT:')
message = input('MESSAGE:')
repeat_question = int(input('Would you like to repeat?\n1. Yes\n2. No\n'))
if repeat_question == 1:
  repeat = int(input('How many times:'))
  for x in range(0,repeat):
    send_mail(mail_user,password_user,send,topic+str(count),message)
    count+=1
else:
  send_mail(mail_user,password_user,send,topic,message)
