# ALPRservice

Simple API REST to process image from url and scan for car plates using openalpr

> A port scan or portscan can be defined as a process that sends client requests to a range of server port addresses on a host, with the goal of finding an active port. While not a nefarious process in and of itself, it is one used by hackers to probe target machine services with the aim of exploiting a known vulnerability of that service,[1] however the majority of uses of a port scan are not attacks and are simple probes to determine services available on a remote machine.

## Description

EyesEgger is just a micro service covering IPv6 port scan functionality over an API/JSON interface.

### Installation

#### Install openalpr (Debian):

Devs tools

```sh
$ sudo apt-get install libpng12-dev libjpeg62-turbo-dev libtiff5-dev zlib1g-dev

$ sudo apt-get install build-essential

$ sudo apt-get install autoconf automake libtool

$ sudo apt-get install git-core

$ sudo apt-get install cmake
```

Prerequisites

```sh
$ sudo apt-get install libopencv-dev libtesseract-dev git cmake build-essential libleptonica-dev

$ sudo apt-get install liblog4cplus-dev libcurl3-dev
```

If using the daemon, install beanstalkd

```sh
$ sudo apt-get install beanstalkd
```

Clone the latest code from GitHub

```sh
$ git clone https://github.com/openalpr/openalpr.git
```

Setup the build directory

```sh
$ cd openalpr/src

$ mkdir build

$ cd build
```

Setup the compile environment

```sh
$ cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_INSTALL_SYSCONFDIR:PATH=/etc ..
```

Compile

```sh
$ make
```

Install the binaries/libraries to your local system (prefix is /usr)

```sh
$ sudo make install
```

Test

```sh
$ wget http://plates.openalpr.com/h786poj.jpg -O lp.jpg

$ alpr -c eu -j lp.jpg
```

To avoid “libdc1394 error: Failed to initialize libdc1394” line

```sh
sudo ln /dev/null /dev/raw1394
```

#### Install ALPRservice

Get last version from Github repo:

```sh
$ git clone https://github.com/ffr4nz/eyesegger.git
```

You need some requeriment installed:

```sh
$ pip install -r requirements.txt
```

After pip install all libraries service can start using:

```sh
$ python sixcansrv.py -p 4343
```
Consume API service using */plate/* endpoint

**http://alprservice.server.domain:service-port/plate/TopN/Country/URL/**

**http://alprservice.server.domain:service-port/plate/10/esu/https://dgaqgnnkkz5ef.cloudfront.net/uploads/car_picture/image/34034/fullsize_car_1437168106.jpg**
```json
{
  "data_type": "alpr_results", 
  "epoch_time": 1449827429584, 
  "img_height": 513, 
  "img_width": 770, 
  "processing_time_ms": 325.753967, 
  "regions_of_interest": [], 
  "results": [
    {
      "candidates": [
        {
          "confidence": 88.498375, 
          "matches_template": 0, 
          "plate": "3985JCM"
        }, 
        {
          "confidence": 86.127914, 
          "matches_template": 0, 
          "plate": "398SJCM"
        }, 
        {
          "confidence": 81.407692, 
          "matches_template": 0, 
          "plate": "985JCM"
        }, 
        {
          "confidence": 81.051277, 
          "matches_template": 0, 
          "plate": "S985JCM"
        }, 
        {
          "confidence": 80.932816, 
          "matches_template": 0, 
          "plate": "B985JCM"
        }
      ], 
      "confidence": 88.498375, 
      "coordinates": [
        {
          "x": 308, 
          "y": 384
        }, 
        {
          "x": 478, 
          "y": 382
        }, 
        {
          "x": 479, 
          "y": 419
        }, 
        {
          "x": 309, 
          "y": 421
        }
      ], 
      "matches_template": 0, 
      "plate": "3985JCM", 
      "plate_index": 0, 
      "processing_time_ms": 76.103065, 
      "region": "", 
      "region_confidence": 0, 
      "requested_topn": 5
    }
  ], 
  "version": 2
}
```

License
----

GPL

References
----

https://github.com/openalpr/openalpr/wiki/Compilation-instructions-(Ubuntu-Linux)
