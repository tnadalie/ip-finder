#!/bin/bash
# put some logs and usage
sudo -H pip install pygeoip wget

python findip.py $1
