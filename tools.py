#/usr/bin/en python
import wget
import sys
import os
import re

apikey_filename = 'google-apikey'
path = os.path.dirname(os.path.realpath(__file__))

def create_google_apikey():
    try:
        if os.path.isdir(path + "/conf") is False:
            os.mkdir(os.path.join(path, "conf"))
        apikey  = open(os.path.join(path, "conf", apikey_filename), "w")
        key = user_input("[*]", "Enter your Google Maps API-KEY")
        apikey.write(key)
        apikey.close()
    except Exception, e:
        print("[*] Cannot create google-apikey file: " + str(e))
        print("[*] Application Shutting Down.")
        sys.exit(1)

def read_apikey():
    apikey  = open(os.path.join(path, "conf", apikey_filename), "r")
    return apikey.read()

def user_input(prompt, msg):
    res = raw_input("\n" + prompt + " " + msg +": ")
    return res

def getdatabase():
    print("\n[*] Downloading the Database ...")

    db_filename='GeoLiteCity.dat'
    db_url='http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz'

    if isFileExists('./' + db_filename) != True:
        filename = wget.download(db_url)
        print "\n[*] Uncompressing the Database ..."
        os.system('gzip -d ' + filename)
    else:
        print("[*] Database already exists ...\n")
    return db_filename

def isFileExists(filename):
    if os.path.exists(filename):
        return True
    return None

def isAlpha(string):
    tester = re.compile("\D")
    return tester.match(string)
