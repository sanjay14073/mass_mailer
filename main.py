##Lets first import pandas
from dotenv import load_dotenv
import pandas as pd
import redis
from mail_utils import send_mail
import time
import os

load_dotenv()
df=pd.read_excel("mail1.xlsx")

email_series=df["email"]

##Configure your cloud reddis
r = redis.Redis(
  host=os.getenv("REDIS_HOST"),
  port=os.getenv("REDIS_PORT"),
  password=os.getenv("REDIS_PASSWORD"))

##If you are using preconfigured redis queue make sure that this the name doesnt confict
queue_name="mass_mailing_queue"

for email in email_series:
    print(email)
    r.lpush(queue_name,email)

##Adjust the time
timeout_seconds = 2000
start_time = time.time()

while time.time() - start_time < timeout_seconds:
    sender_mail = r.rpop(queue_name)
    try:
        if sender_mail:
            send_mail(sender_mail.decode())
        else:
            break
    except:
        r.lpush(queue_name,sender_mail)
    

    
