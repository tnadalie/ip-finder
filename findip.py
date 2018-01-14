#/usr/bin/en python
from argv_parser import findip_argparser
from requests import get
import pygeoip
import socket
import tools
import json
import sys

host = ''
gip = None
gapikey=''

def gethostbyname():
    try:
        print "[*] Converting Host Name [%s] to IP ..." % (host)
        hostip = socket.gethostbyname(host)
        print "[*] IP is %s" % (hostip)
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
        if tools.isFileExists('./conf/google-apikey') != True:
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
    isDomain = None
    if len(sys.argv) == 1:
    	host = tools.user_input("[*]","Enter Host Target IP Address/Host Name")
        if (tools.isAlpha(host)):
            isDomain = True
    else:
        args = findip_argparser()
        if args.ip is None:
            host = args.domain
            isDomain = True
        else:
            host = args.ip[0]

    if isDomain is True:
        host = gethostbyname()
    get_address_details(pygeoip.GeoIP('./' + tools.getdatabase()))
except KeyboardInterrupt:
	print("\n\n[*] User Requested An Interrupt.")
	print("[*] Application Shutting Down.")
	sys.exit(1)
