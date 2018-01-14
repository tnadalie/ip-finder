#/usr/bin/en python
import argparse

def findip_argparser():
    parser = argparse.ArgumentParser(prog='./ipfinder.sh [-d DOMAIN NAME][-i IP]', description='Python module to retrieve postal address from IP/domain name.')

    parser.add_argument('-d', '--domain', nargs='?', help='Input a domain name')
    parser.add_argument('-i', '--ip', nargs='?', help='Input an IP')
    args = parser.parse_args()
    return args
