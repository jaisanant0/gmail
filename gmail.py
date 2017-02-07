from email.mime.text import MIMEText
import smtplib

def sendmail(usr,pwd,to,sub,text) :
      msg=MIMEText(text)
      msg['From']=usr
      msg['To']=to
      msg['Subject']=sub

      try :
            smtpserver=smtplib.SMTP('smtp.gmail.com',587)
            print("[*] Connecting to Server..")
            smtpserver.ehlo()
            print("[*] Starting secure connection..")
            smtpserver.starttls()
            smtpserver.ehlo()
            print("[*] Logging in..")
            smtpserver.login(usr,pwd)
            print("[*] Sending mail..")
            smtpserver.sendmail(usr,to,msg.as_string())
            print("[*] Mail sent successfuly")
            smtpserver.close

      except :
            print("[-] Error in sending mail")

            
print("[+] Enter your gmail username : ")
usr=str(input())

print("[+] Enter your password : ")
pwd=str(input())

print("[+] Enter the reciver's username : ")
to=str(input())

print("[+] Enter the subject : ")
sub=str(input())

print("[+] Enter the content : ")
text=str(input())

sendmail(usr,pwd,to,sub,text)
