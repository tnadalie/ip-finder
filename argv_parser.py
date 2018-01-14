#/usr/bin/en python
import argparse

def findip_argparser():
    parser = argparse.ArgumentParser(prog='./ipfinder.sh', description='Python module to retrieve postal address from IP/Domain Name.')

    parser.add_argument('-d', '--domain', nargs='?', help='Host Target Domain Name')
    parser.add_argument('-i', '--ip', nargs='?', help='Host Target IP')
    args = parser.parse_args()
    return args
