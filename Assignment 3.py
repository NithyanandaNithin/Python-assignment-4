import smtplib
import random 

def read_data_send_mail():
  
  try:
    f=open("students_mails.txt","r")
    students_mails=f. read()
    students_mails=students_mails.split(",")
    print(students_mails)
  except:
    print("file not available")
    
  sender_mail="nithyanandanithin5@gmail.com"
  for i in students_mails:
    OTP=random.randint(000000,999999)
    print(OTP)
    s=smtplib.SMTP('smtp.gmail.com', 587)
    s.startls()
    s.login("nithyanandanithin5@gmail.com","hfom cyli atpt tpji")
    message=f"Hi your order arrived,Please share this OTP:{OTP} with agent"
    
    try:
      s.sendmail(nithyanandanithin5@gmail.com,i, message)
      print("mail sent successfully")
    except:
      print("mail not sent")
      
read_data_send_mail()