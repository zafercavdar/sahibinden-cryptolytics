import urllib
import time
import json

domain = "https://devakademi.sahibinden.com"


def date_transform(epoch):
    return time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(epoch))


def get_current_value():
    endgate = "{}/ticker".format(domain)
    res = urllib.request.urlopen(endgate).read()
    res = json.loads(res.decode('utf-8'))
    return res['value']


def get_history():
    endgate = "{}/history".format(domain)
    res = urllib.request.urlopen(endgate).read()
    res = json.loads(res.decode('utf-8'))
    for i in range(0, len(res)):
        res[i] = res[i]['value']
    indices = [x for x in range(0, len(res))]
    return list(zip(indices, res))
