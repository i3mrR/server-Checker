
import json

from pickle import TRUE
import telnetlib
import time
from turtle import done
data= None
import smtplib  
runcode = True
from datetime import datetime



conn =smtplib.SMTP('smtp-mail.outlook.com',587)  

type(conn)  

conn.ehlo()  

conn.starttls()  
#here you put your email to send notification from 
conn.login('your email','email password')




while runcode==True: 
# here to put your json file i will put example you can use
    with open('example.json') as file:
        data=json.load(file)
        file.close()

    for ip, ports in data.items():
        
     for port in ports:
        try:
            
                connectt=telnetlib.Telnet(ip,port)
                response='Success'
                
        except:
            # here the massage send with failing report with ip and port and time
            timeNow=datetime.now().strftime("%H:%M:%S")
            msgg="""From:  Server is down <your email to send notifaction in>


please check {} port number {} to reconect, time of error at {}

""".format(ip,port,timeNow)   
        
        # here emails and list you want to send notification to 
            conn.sendmail('your email want to send notify to',listEmail,msg=msgg)  


            response='Failed'
            

            print(ip,port,response,timeNow)
        
        print(ip,port,response)
        listEmail=['email to sned notify to ','email to sned notify to@outlook.com']
        




        

# the rerun set for 9000 seconed you could change it any time
    time.sleep(9000)
conn.quit()

 
