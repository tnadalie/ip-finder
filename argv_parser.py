#/usr/bin/en python
import argparse
import sys

def findip_argparser():
    parser = argparse.ArgumentParser(prog='./ipfinder.sh', description='Python module to retrieve postal address from IP/Domain Name.')

    parser.add_argument('-d', '--domain', nargs='?', help='Host Target Domain Name')
    parser.add_argument('-i', '--ip', nargs='?', help='Host Target IP')
    args = parser.parse_args()

    if args.domain is None:
        print("[*] [-d] <-> [--domain] argument requires a value.")
    elif args.ip is None:
        print("[*] [-i] <-> [--ip] argument requires a value.")
    else:
        return args
    print("[*] Application Shutting Down.")
    sys.exit(1)
