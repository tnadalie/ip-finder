#!/bin/bash
echo -e "[*] Starting ...\n"
echo -e "[*] Installing dependencies ...\n"
sudo -H apt-get install python-pip python-dev build-essential
sudo -H pip install --upgrade pip setuptools
sudo -H pip install pygeoip wget requests
echo -e "\n[*] Script finished ..."
