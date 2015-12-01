import json
import glob
import csv

dir_name = raw_input('Enter directory name: ')
print dir_name

i = 0
total_on_content_load = 0.0
total_on_load = 0.0
files = glob.glob(str(dir_name+"/*.har"))
for f in files:
	with open(f) as data_file:
		data = json.load(data_file)

		print 'Start Time: ', data["log"]["pages"][0]["startedDateTime"]
		print 'Title: ', data["log"]["pages"][0]["title"]
		print '---- Page Timings ----'
		print '\t onContentLoad', data["log"]["pages"][0]["pageTimings"]["onContentLoad"]
		print '\t onLoad: ', data["log"]["pages"][0]["pageTimings"]["onLoad"]
		i = i + 1
		title = data["log"]["pages"][0]["title"]
		total_on_content_load += float(data["log"]["pages"][0]["pageTimings"]["onContentLoad"])
		total_on_load += float(data["log"]["pages"][0]["pageTimings"]["onLoad"])

with open('names.csv', 'w') as csvfile:
    fieldnames = ['Site', 'Iterations', 'Avg Content Load Time', 'Avg On Load Time']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'Site': title, 'Iterations': i, 'Avg Content Load Time': float(total_on_content_load/i), 'Avg On Load Time' : float(total_on_load/i)})
print '---------------PAGE LOAD TIMES over', i, ' Iterations-----------'
print 'On Content Load : ', float(total_on_content_load/i)
print 'On Load : ', float(total_on_load/i)
