#!/bin/bash
# put some logs and usage
echo -e "[*] Starting ...\n"

echo -e "[*] Installing dependencies ...\n"
sudo -H pip install pygeoip wget

python findip.py $1 $2 $3 $4
echo -e "\n[*] Script finished ..."
