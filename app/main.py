import flask
import requests
import requests, ssl
from apscheduler.schedulers.background import BackgroundScheduler

import time
import smtplib
app = flask.Flask(__name__)
cron = BackgroundScheduler()
def job_function():
    print("HOla")
    url = 'https://infovisa.ibz.be/ResultFr.aspx?place=HAV&visumnr=17125'
    response = requests.get(url)
    if response.text.__contains__("ACCORD"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "shaniafiallo@gmail.com",
                   "SIIIIIIII",
                   "Nos fuimos pa belgica pingaaaaaaaa")
        return "NOS FUIMOS PA BELGICA PINGAAAAAA"
    elif response.text.__contains__("REJET"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "cristiansori2@gmail.com",
                   "APELAR",
                   "De pinga hay que Apelar")
        cron.pause()
        job.remove()
        return "De pinga hay que APELAR"
    elif response.text.__contains__("Octroi du visa sur production"):
        port = 465  # For SSL
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login("cristiansori2@gmail.com", "cryipomrjfssklkf")
            server.sendmail("cristiansori2@gmail.com",
                   "shaniafiallo@gmail.com",
                   "SIIIIIIII",
                   "Nos fuimos pa belgica pingaaaaaaaa pero hay que presentar papeles,pero no importaaaaaaaaa.")
        return "NOS FUIMOS PA BELGICA PINGAAAAAA"
    elif response.text.__contains__("En traitement"):
      return "sdd"
app.config["DEBUG"] = False
job = cron.add_job(job_function, 'interval', minutes=5)
cron.start()
job.resume()

#job.remove()



