from turtle import st
import flask
import requests
import requests, ssl
contador=17000
accord=0
tratamiento=0
rejet=0
while contador<18000:
    url = 'https://infovisa.ibz.be/ResultFr.aspx?place=HAV&visumnr='+str(contador)
    response = requests.get(url)
    if response.text.__contains__("ACCORD"):
        accord=accord+1
        print("Aceptados "+str(accord)+" Denegados "+str(rejet)+" Visa "+ str(contador))
    elif response.text.__contains__("REJET"):
        rejet =rejet +1
        print("Aceptados "+str(accord)+" Denegados "+str(rejet)+" Visa "+ str(contador))
    elif response.text.__contains__("Octroi du visa sur production"):
         accord=accord+1
         print("Aceptados "+str(accord)+" Denegados "+str(rejet)+" Visa "+ str(contador))
    contador=contador +1

