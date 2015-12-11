#!/usr/bin/env python
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

__author__ = "ffranz"
__copyright__ = "2015"
__credits__ = ["ffranz"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "ffranz"
__email__ = "ffranz@sinfonier-project.net"
__status__ = "Developing"

import optparse
import datetime
import time
from random import randint
import subprocess
import os
import json
import urllib
from glob import glob
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hide_service():
	abort(404)

@app.route('/about')
def about():
	return 'tuoba'

@app.route('/plate/<path:topn>/<path:country>/<path:url>')
def scan_plate(topn,country,url):
        insert_data ={}
	file_path = "/tmp/"+str(int(time.time()+randint(50,150)))+".jpg"
        try:
		testfile = urllib.URLopener()
		testfile.retrieve(url,file_path)
		cmd_alpr = "alpr -c "+country+" -n "+topn+" -j "+file_path
		launch = subprocess.Popen(cmd_alpr, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		output,err = launch.communicate()
		response = json.loads(output)
                if len(response["results"]) > 0:
                        result = response["results"][0]
                        del response["results"]
                        response["results"] = result
                        response["plate"] = response["results"]["plate"]
                        response["confidence"] = response["results"]["confidence"]
		else:
			response["plate"] = ""
			response["confidence"]
	except Exception as err:
                print('Error! ',err)
		response['status'] = "error"
		response['error_detail'] = err
	try:
		os.remove(file_path)
	except Exception as e:
		print('Error removing file',e)
	return jsonify(response)

def check_alpr():
    cmd_alpr_version = "alpr --version"
    launch = subprocess.Popen(cmd_alpr_version, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output,err = launch.communicate()
    if "command not found" in output: return 1
    return 0

def main():
    parser = optparse.OptionParser(usage="%prog [options]  or type %prog -h (--help)")
    parser.add_option('-p','--port',
		dest='port',
		action='store',
		help='The port to run server on',
		default=4343)
    (options, args) = parser.parse_args()
    port = int(options.port)
    if check_alpr():
	print "Alpr command not found"
	exit(1)
    print 'Starting tornado on port {port}...'.format(port=port)

    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    http_server = HTTPServer(WSGIContainer(app))

    http_server.listen(int(port))
    IOLoop.instance().start()

if __name__ == '__main__':
	main()
