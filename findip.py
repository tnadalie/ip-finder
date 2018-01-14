#/usr/bin/en python
from argv_parser import findip_argparser
from requests import get
import pygeoip
import socket
import tools
import json
import wget
import sys

host = ''
gip = ''
gapikey=''
db_url='http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'

def gethostbyname():
    try:
        print "[*] Converting Host Name [%s] to IP ..." % (host)
        hostip = socket.gethostbyname(host)
        print "[*] IP is %s" % (host)
    except Exception, e:
    	print("[*] Bad Host Name.")
    	print("[*] Application Shutting Down.")
    	sys.exit(1)
    return hostip

def get_address_details(gip):
    rec = gip.record_by_addr(host)

    if rec is None:
    	print("[*] Can't retrieve data from MaxMind DB.")
    	print("[*] Application Shutting Down.")
    	sys.exit(1)
    lat = str(rec.get('latitude'))
    lng = str(rec.get('longitude'))

    for key,val in rec.items():
        print " [->] %s: %s" % (key,val)

    isGoogle = raw_input("\n[*] Do you want to use Google Maps services to get a precise address [Y/N]: ")

    if isGoogle in ['y', 'yes', 'Y']:
        if tools.isFileExists('./apikey.txt') != True:
            gapikey = tools.create_google_apikey()
        gapikey = tools.read_apikey()
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

try:
    if len(sys.argv) == 1:
    	host = user_input("[*]","Enter Host Target IP Address/Host Name")
    else:
        args = findip_argparser()
        if args.ip is None:
            host = args.domain
            host = gethostbyname()
            print host
        else:
            host = args.ip[0]


    get_address_details(pygeoip.GeoIP('./' + tools.getdatabase()))
except KeyboardInterrupt:
	print("\n\n[*] User Requested An Interrupt.")
	print("[*] Application Shutting Down.")
	sys.exit(1)
