#/usr/bin/en python
import os

apikey_filename = 'apikey.txt'
db_filename='GeoLiteCity.dat'

def create_google_apikey():
    apikey  = open(apikey_filename, "w")
    key = user_input("[*]", "Enter your Google Maps API-KEY")
    apikey.write(key)
    apikey.close()

def read_apikey():
    apikey  = open(apikey_filename, "r")
    return apikey.read()

def user_input(prompt, msg):
    res = raw_input("\n" + prompt + " " + msg +": ")
    return res

def getdatabase():
    print("\n[*] Dowloading the Database ...")
    if isFileExists('./' + db_filename) != True:
        filename = wget.download(db_url)
        print "\n[*] Uncompressing the Database ..."
        os.system('gzip -d ' + filename)
    else:
        print("[*] Database already exists ...\n")
    return db_filename

def isFileExists(filename):
    if os.path.isfile(filename):
        return True
    return None
