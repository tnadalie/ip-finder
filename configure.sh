#!/bin/bash
echo -e "[*] Starting ...\n"

# check if distrib is centos
OS=[[ command -v yum ]]

echo -e "[*] Installing dependencies ...\n"
if [ ${#OS} -ge 1 ]; then
  sudo -H yum install -y epel-release
  sudo -H yum update -y
  sudo -H yum install -y python-pip python-dev build-essential
  sudo -H pip install --upgrade pip setuptools
  sudo -H pip install pygeoip wget requests
else
  sudo -H apt-get update -y & sudo -H apt-get upgrade -y
  sudo -H apt-get install -y python-pip python-dev build-essential
  sudo -H pip install --upgrade pip setuptools
  sudo -H pip install pygeoip wget requests
fi
echo -e "\n[*] Script finished ..."
