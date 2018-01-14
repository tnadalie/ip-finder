# ip-finder

*Python module used to retrieve a postal address from an IP or a Domain Name*
*Working on Debian


### Prerequisites

The following packages are required to be able download the project and install its dependencies:

**apt-get**
```
apt-get -y install sudo python wget unzip
```

**yum**
```
yum -y install sudo python wget unzip
```

Download the project's archive from the github repository and then unzip it:
```
wget https://github.com/tnadalie/ip-finder/archive/master.zip
unzip master.zip
```


### Installing

Firstly, run **configure.sh**:
```
bash configure.sh
```

Then you can simply run **ipfinder.sh** to test your environment:
```
bash ipfinder.sh
```

Run **ipfinder.sh**  with the **--help** parameter to get the script usage:
```
bash ipfinder.sh --help
```

If you want to use the Google Maps API, you'll need to enter your API-KEY when promted by the script. They key will be locally stored into the file **google-apikey** under **./conf/**.

Please refer to the following [official documentation](https://developers.google.com/maps/documentation/embed/get-api-key) to create your API-KEY.

Example:

```
[*] Starting ...

facebook.com
[*] Converting Host Name [facebook.com] to IP ...
[*] IP is 31.13.66.36

[*] Downloading the Database ...
[*] Database already exists ...

 [->] city: None
 [->] region_code: None
 [->] area_code: 0
 [->] time_zone: Europe/Dublin
 [->] dma_code: 0
 [->] metro_code: None
 [->] country_code3: IRL
 [->] latitude: 53.3472
 [->] postal_code: None
 [->] longitude: -6.2439
 [->] country_code: IE
 [->] country_name: Ireland
 [->] continent: EU

[*] Do you want to use Google Maps services to get a precise address [Y/N]: Y

[*] Enter your Google Maps API-KEY: MYGOOGLEMAPS-APIKEY
```

## Authors

* **Thomas Nadalie** - *Initial work* - [tnadalie](https://github.com/tnadalie)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
