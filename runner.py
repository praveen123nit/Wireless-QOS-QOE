import csv
import os
import argparse
from multiprocessing import Pool

sites = ['NDTV', '9GAG', 'Airbnb', 'BBC', 'ESPN', 'Google', 'Netflix', 'reddit', 'Snapdeal', 'StackOverflow', 'TOI', 'YouTube']

def run(iters, outfile, host):
	log_dir = os.path.dirname(os.path.realpath(outfile)) 
	print ("Logging directory :", log_dir)
	
	''' Threading
	threads = 4
	p = Pool(processes=int(threads))
        site = ''	
	for res in p.imap_unordered(os.system, (('python har_file_generator.py --url http://' + str(host) + '/' + site + '/ --logdir ' + pw_dir + '/output_' + site + '/ ' + '--outfile ' +outfile + ' --iters ' + str(iters)) for site in sites), chunksize = 10):
		print 'Done with site:', site
	'''
	
	for site in sites:
		os.system('python har_file_generator.py --url http://' + str(host) + '/' + site + '/ --logdir ' + log_dir + '/output_' + site + '/ ' + '--outfile ' + outfile + ' --iters ' + str(iters))

def main():
	parser = argparse.ArgumentParser(description="Open webpages and trigger net export ")
	parser.add_argument('--outfile', help = "output file to write the page load time")
	parser.add_argument('--iters', help = "number of reloads of the page to find avg. page load time")
	parser.add_argument('--host', help = "Wifi hosts IP address")
	args = parser.parse_args()
	try:
		os.remove(args.outfile)
	except:
		a = 1
	with open(args.outfile, 'a+') as csvfile:
		fieldnames = ['Site', 'Iterations', 'Avg Content Load Time', 'Avg On Load Time']
		writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
		writer.writeheader()

	run(int (args.iters), args.outfile, args.host)

if __name__ == "__main__":
	main()
