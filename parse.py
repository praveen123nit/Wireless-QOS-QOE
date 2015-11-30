import json
import glob
from pprint import pprint

dir_name = raw_input('Enter directory name: ')
print dir_name

files = glob.glob(str(dir_name+"/*.har"))
for f in files:
        with open(f) as data_file:
            data = json.load(data_file)

        print 'Start Time: ', data["log"]["pages"][0]["startedDateTime"]
        print 'Title: ', data["log"]["pages"][0]["title"]
        print '---- Page Timings ----'
        print '\t onContentLoad', data["log"]["pages"][0]["pageTimings"]["onContentLoad"]
        print '\t onLoad: ', data["log"]["pages"][0]["pageTimings"]["onLoad"]
