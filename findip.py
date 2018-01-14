#/usr/bin/en python
from requests import get
import pygeoip
import socket
import json
import wget
import sys
import os

host = ''
gip = ''
gapikey='AIzaSyDjl0muK7MOEJLN2vv3NnVQNOquI_0zGGI'
db_url='http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'
db_filename='GeoLiteCity.dat'

def getdatabase():
    print("\n[*] Dowloading the Database ...")
    if os.path.isfile('./' + db_filename) != True:
        filename = wget.download(db_url)
        print "\n[*] Uncompressing the Database ..."
        os.system('gzip -d ' + filename)
    else:
        print("[*] Database already exists ...\n")

def gethostbyname(host):
    try:
        print "[*] Converting Host Name [%s] to IP ..." % (host)
        hostip = socket.gethostbyname(host)
        print "[*] %s's IP is %s" % (host, hostip)
    except Exception, e:
    	print("[*] Bad Host Name.")
    	print("[*] Application Shutting Down.")
    	sys.exit(1)
    return hostip

def get_address_details(gip):
    rec = gip.record_by_addr(host)
    lat = str(rec.get('latitude'))
    lng = str(rec.get('longitude'))

    for key,val in rec.items():
        print " [->] %s: %s" % (key,val)

    try:
        isGoogle = raw_input("\n[*] Do you want to use Google Maps services to get a precise address [Y/N]: ")
    except KeyboardInterrupt:
    	print("\n\n[*] User Requested An Interrupt.")
    	print("[*] Application Shutting Down.")
    	sys.exit(1)

    if isGoogle in ['y', 'yes', 'Y']:
        url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng=' + lat + ',' + lng + '&key=' + gapikey
        response  = get(url)
        json = response.json()

        if json['results']:
            data = json['results'][0]
            print " [->] address: %s" % (data.get('formatted_address', None))
        else:
        	print("[*] Can't retrieve data from Google Maps API.")
        	print("[*] Application Shutting Down.")
        	sys.exit(1)
    return

if len(sys.argv) == 1:
    try:
    	host = raw_input("\n[*] Enter Host Target IP Address/Host Name: ")
    except KeyboardInterrupt:
    	print("\n\n[*] User Requested An Interrupt.")
    	print("[*] Application Shutting Down.")
    	sys.exit(1)
else:
    host = sys.argv[1]

if host.endswith(('.com','.fr','.org','.net','.mx','.ca')):
    host = gethostbyname(host)

getdatabase()
get_address_details(pygeoip.GeoIP('./' + db_filename))
