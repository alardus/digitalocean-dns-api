import json
import urllib.parse
import urllib.request
from requests import get
from defaultenv import env


def addhost(subdomain, ip):
    if ip == '':
        ip = '127.0.0.1'
    headers = {'Authorization' : (env('TOKEN'))}
    values = {'name' : subdomain,
              'type' : 'A',
              'ttl' : '1800',
              'data' : ip}
    url = 'https://api.digitalocean.com/v2/domains/' + (env('DOMAIN')) + '/records'

    data = json.dumps(values)
    data = data.encode()
    req = urllib.request.Request(url, data, headers)
    urllib.request.urlopen(req)

def listhosts(subdomain):
    headers = {'Authorization' : (env('TOKEN'))}
    url = 'https://api.digitalocean.com/v2/domains/' + (env('DOMAIN')) + '/records?type=A&per_page=200'

    req = urllib.request.Request(url, headers = headers)
    request = urllib.request.urlopen(req)

    data = json.loads(request.read().decode(request.info().get_param('charset') or 'utf-8'))
    for i in (data['domain_records']):
        for k, v in i.items():
            if v == subdomain:
                recid = (i['id'])
                return recid


def updatehost(subdomain, ip):
    if ip == '':
        ip = '1.1.1.1'

    recid = str(listhosts(subdomain))

    headers = {'Authorization' : (env('TOKEN'))}
    values = {'data' : ip}
    url = 'https://api.digitalocean.com/v2/domains/' + (env('DOMAIN')) + '/records/' + recid

    data = json.dumps(values)
    data = data.encode()
    req = urllib.request.Request(url, data, headers, method='PUT')
    urllib.request.urlopen(req)


def delhost(subdomain):
    recid = str(listhosts(subdomain))

    headers = {'Authorization' : (env('TOKEN'))}
    values = {}
    url = 'https://api.digitalocean.com/v2/domains/' + (env('DOMAIN')) + '/records/' + recid

    data = json.dumps(values)
    data = data.encode()
    req = urllib.request.Request(url, data, headers, method='DELETE')
    urllib.request.urlopen(req)
