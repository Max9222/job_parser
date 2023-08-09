from abc import ABC, abstractmethod
import requests
import json
import time
import os


def getEmployers():
    req = requests.get('https://api.hh.ru/employers')
    data = req.content.decode()
    req.close()
    count_of_employers = json.loads(data)['found']
    employers = []
    i = 0
    j = count_of_employers
    while i < j:
        req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        try:
            employers.append([jsObj['id'], jsObj['name']])
            i += 1
            print([jsObj['id'], jsObj['name']])
        except:
            i += 1
            j += 1
        if i % 200 == 0:
            time.sleep(0.2)
    return employers


employers = getEmployers()